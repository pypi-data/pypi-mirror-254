from functools import cache
import json
import os
import typing
import toml
from sprinko.core.ctx import Ctx, CtxBase
from sprinko.extra.object import SingletonMeta, json_serializable
from sprinko.core.bottle import Bottle
from sprinko.extra.log import logger
from sprinko.base.env import scenarios
import sprinko.extra.misc as misc
    
class Bowl(metaclass=SingletonMeta):
    def getFile(self, name :str, save : bool = False, saveAs : str = None):
        if "/" in name:
            bottleName = (splitted := name.split("/"))[0]
            name = splitted[1]
            
            if bottleName not in Bottle.instances():
                raise KeyError(f"Bottle {bottleName} not found")
            
            return Bottle.instances()[bottleName].getFile(name, save, saveAs)
        
        for bottle in Bottle.instances().values():
            if name in bottle.filelist:
                return bottle.getFile(name, save, saveAs)
            
        raise KeyError(f"File {name} not found")
    
    def getScript(self, name : str, returnBottle : bool = False):
        if "/" in name:
            bottleName = (splitted := name.split("/"))[0]
            name = splitted[1]
            
            if bottleName not in Bottle.instances():
                raise KeyError(f"Bottle {bottleName} not found")
            
            if returnBottle:
                return Bottle.instances()[bottleName].getScript(name), bottleName
            return Bottle.instances()[bottleName].getScript(name)
        
        for bottle in Bottle.instances().values():
            res = bottle.getScript(name)
            if res is not None:
                if returnBottle:
                    return res, bottle.name
                return res
            
        raise KeyError(f"File {name} not found")
    
    @cache
    def parse(self, keys, ctx : CtxBase = None, allowUnsafe = False):
        if ctx is None:
            ctx = Ctx()
        scriptsToRun = {}
        scriptScope = None
        for key in keys:
            match key:
                # is a file path
                case str(key) if os.path.exists(key) and allowUnsafe:
                    scriptStr = open(key, "r").read()
                    scriptId =scriptScope= key
                    scriptsToRun[scriptId] = scriptStr
                # [read:{file}]
                case str(key) if key.startswith("[read:") and key.endswith("]"):
                    name = key[6:-1]
                    ctx.set(key=scriptScope, _d=toml.load(name))
                # [cwd:{path}]
                case str(key) if key.startswith("[cwd:") and key.endswith("]"):
                    name = key[5:-1]
                    os.chdir(name)
                # [a=b, c=d]
                case str(key) if key.startswith("[") and key.endswith("]") and "=" in key:
                    vars = key[1:-1]
                    vars = vars.replace(",", "\n")
                    vars = vars.replace("=", "='")
                    vars = vars.replace("\n", "'\n")
                    varDict = toml.loads(vars)
                    ctx.set(key=scriptScope, **varDict)
                # {dict}
                case str(key) if key.startswith("{") and key.endswith("}"):
                    ctx.set(key=scriptScope, **json.loads(key))
                # is a file path
                case str(key) if os.path.exists(key) and not allowUnsafe:
                    raise KeyError("Current Security Policy forbids running out of bottle scripts")
                # else
                case str(key):
                    scriptScope = key
                    scriptStr, bottle = self.getScript(key, True)
                    scriptId = f"{bottle}/{key}"
                    scriptsToRun[scriptId] = scriptStr
                    
                # direct dict import
                case dict(key):
                    ctx.set(key, scriptScope)
                
        return scriptsToRun, ctx
    
    def gen(self, keys: list, ctx: CtxBase = None, allowUnsafe: bool = False) -> str:
        scriptsToRun, ctx = self.parse(keys, ctx, allowUnsafe)
        
        genFileStr = misc.unpack_dict_to_py_var(ctx.expose())
        
        for id, script in scriptsToRun.items():
            genFileStr += f"#{id}\n"
            genFileStr += misc.unpack_dict_to_py_var(ctx.getScope(id))
            #genFileStr += script
            content = misc.replace_ctx_get_calls(script)
            genFileStr += content
            
            genFileStr += "\n"
    
        return genFileStr
        
    def gen_scenario(self, name: str) -> str:
        seq, globalScope, scopes = self.retrieve_scenario(name)
        
        genFileStr = misc.unpack_dict_to_py_var(globalScope)
        
        for id in seq:
            genFileStr += f"#{id}\n"
            genFileStr += misc.unpack_dict_to_py_var(scopes[id])
            #genFileStr += self.getScript(id).decode("utf-8")
            content = self.getScript(id).decode("utf-8")
            content = misc.replace_ctx_get_calls(content)
            genFileStr += content
            genFileStr += "\n"
            
        return genFileStr
        
    def run(self, *keys, ctx : CtxBase = None, allowUnsafe : bool = False):
        
        scriptsToRun, ctx = self.parse(keys, ctx, allowUnsafe)
        
        for id, script in scriptsToRun.items():
            logger.debug(f"Running script {id}")
            ctx.push(key=id)
            
            exec(script, ctx.expose())
            ctx.pop()
        

    def set_sceanrio(self, name : str, keys : list, override : bool = False):
        if name in scenarios and not override:
            raise KeyError(f"Scenario {name} already exists")
        
        scriptsToRun, ctx = self.parse(keys)
        
        scenarios[name] = {
            "seq" : list(scriptsToRun.keys()),
            "global" : {k : v for k, v in ctx.expose().items() if json_serializable(v)},
            "scopes" : {
                k : ctx.getScope(k) for k in scriptsToRun
            }
        }
        
    def retrieve_scenario(self, name : str):
        if name not in scenarios:
            raise KeyError(f"Scenario {name} not found")
        
        scenarioMeta = scenarios[name]
        seq: list = scenarioMeta["seq"]
        globalScope : dict = scenarioMeta["global"]
        scopes: typing.Dict[str, dict] = scenarioMeta["scopes"]

        return seq, globalScope, scopes
    
    
        
    def run_scenario(self, name : str, ctx : CtxBase = None, allowUnsafe : bool = False):
        
        if ctx is None:
            ctx = Ctx()
        
        seq, globalScope, scopes = self.retrieve_scenario(name)
        
        ctx.set(globalScope)
        for k, s in scopes.items():
            ctx.set(s, k)
        
        for id in seq:
            logger.debug(f"Running script {id}")
            ctx.push(key=id)
            
            if allowUnsafe and os.path.exists(id):
                scriptStr = open(id, "r").read()
            elif (scriptStr := self.getScript(id)) is not None:
                pass
            else:
                raise KeyError(f"Script {id} not found")                
            
            exec(scriptStr, ctx.expose())
            ctx.pop()