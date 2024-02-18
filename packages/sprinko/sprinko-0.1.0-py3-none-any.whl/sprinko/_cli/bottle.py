
import datetime
import os
import shutil
import click

from sprinko.core import Bottle
from sprinko.base.env import CacheEntry, caching, caching_dir, BottleEntry
import toml
from sprinko.base.env import bottles
from tabulate import tabulate
from sprinko.extra.hashing import get_hash
from sprinko._cli.cache import cache_defer

@click.group("bottle")
def bottleGroup():
    pass

@bottleGroup.command("list", help="List all installed bottles")
def bottleList():
    for x in Bottle.instances():
        click.echo(x)

@bottleGroup.command("remove", help="Remove a bottle")
@click.argument("name")
def bottleRemove(name):
    Bottle.unreg(name)

@bottleGroup.command("install", help="Install a bottle")
@click.argument("name")
def bottleInstall(name):
    availBottles = Bottle.fullMeta().get("bottle", {})
    if name not in availBottles:
        raise click.ClickException(f"Bottle {name} not found")
    else:
        Bottle.reg(name, availBottles[name]["path"], availBottles[name]["type"])
        
@bottleGroup.command("add", help="Add a bottle")
@click.argument("path", type=click.Path(exists=True, file_okay=False))
@click.option("--skip-zip", "-s", is_flag=True, help="Skip zip")
@click.option("--set-update-interval", "-u", type=click.INT, default=0,  help="Set update interval")
@click.pass_context
def bottleAdd(ctx : click.Context, path : str, skip_zip : bool, set_update_interval : int):
    path = os.path.abspath(path)
    
    if not os.path.exists(os.path.join(path, "bottle.toml")):
        raise click.ClickException(f"{path} is not a valid bottle")
    
    with open(os.path.join(path, "bottle.toml"), "r") as f:
        meta = toml.loads(f.read())
        bottlem = meta.get("bottle", None)
        
    if bottlem is None:
        raise click.ClickException(f"{path} is not a valid bottle")
    
    bottlem : BottleEntry
        
    if bottlem["type"] == "local":
        click.echo("Adding local bottle")
        return Bottle.reg(os.path.basename(path), path, "local")
    
    if not os.path.exists(os.path.join(path, "bottle.zip")) or not skip_zip:
        from sprinko._cli_bottler.__main__ import _packall
        # parent folder
        preserve_cwd = os.getcwd()
        ctx.invoke(_packall, cwdpath=os.path.dirname(path))
        
        click.echo("Finished Packing, restoring to original job")
        os.chdir(preserve_cwd)
        
    bottle_zip_path = os.path.join(path, "bottle.zip")
    bottle_zip_bytes = open(bottle_zip_path, "rb").read()
    bottle_zip_hash = get_hash(bottle_zip_bytes)
    
    #TODO merge with caching for a unified function in the future
    entry : CacheEntry = {
        "checksum": bottle_zip_hash,  
        "lastPulled" :  datetime.datetime.now().isoformat(),
        "type": "gitraw",
    }
    
    if set_update_interval > 0:
        entry["updatableInterval"] = set_update_interval
    
    caching[bottlem["path"]+"/bottle.zip"] = entry
    shutil.copyfile(bottle_zip_path, os.path.join(caching_dir, bottle_zip_hash))
    Bottle.reg(bottlem["name"], bottlem["path"], type_="gitraw", ignoreExists=True)
    
    click.echo(f"Bottle {bottlem['name']} added")        

@bottleGroup.command("index", help="List all available bottles")
def indexBottle():
    tdata = []
    
    bottle_metas : dict = Bottle.fullMeta().get("bottle", {})
    
    bottle_metas.update(bottles)
    
    for k, v in bottle_metas.items():
        data = []
        data.append(k)
        data.append(v["path"])
        data.append(v["type"])
        data.append(k in bottles)
        tdata.append(data)
        
    click.echo(
        tabulate(tdata, headers=("name", "path", "type", "installed"))
    )
    
@bottleGroup.command("update", help="Update all installed bottles")
def updateBottle():
    for x in Bottle.instances().values():
        x.refresh(refetch=True)
        
@bottleGroup.command("default", help="Initializes a default (main) bottle")
def defaultBottle():
    Bottle.reg(
        "main",
        "zackaryw/sprinko/main/bottles/main",
        type_="gitraw",
        ignoreExists=True
    )
    
@bottleGroup.command("set-update", help="Set update interval for a given bottle")
@click.argument("name")
@click.argument("value", type=click.INT)
@click.option("--unit", "-u", type=click.Choice(["s", "m", "h", "d"]), default="s", help="Unit of the update interval")
@click.option("--relative", "-r", is_flag=True, help="Use relative time")
@click.pass_context
def bottleSetUpdate(ctx, name, value, unit, relative):
    if name not in Bottle.instances():
        raise click.ClickException(f"Bottle {name} not found")
    
    bottle = Bottle.instances()[name]
    if bottle.type not in ["local", "gitraw"]:
        raise click.ClickException(f"Bottle {name} is not a gitraw or local bottle")
    
    if bottle.type == "local":
        addr = bottle.addr
    else:
        addr = bottle.addr + "/bottle.zip"
        
    ctx.invoke(cache_defer, path=addr, value=value, unit=unit, relative=relative)
    
@bottleGroup.command("update", help="Update a given bottle")
@click.argument("name")
def bottleUpdate(name):
    if name not in Bottle.instances():
        raise click.ClickException(f"Bottle {name} not found")
    
    bottle = Bottle.instances()[name]
    if bottle.type not in ["local", "gitraw"]:
        raise click.ClickException(f"Bottle {name} is not a gitraw or local bottle")
    
    bottle.refresh(refetch=True)
    click.echo(f"Bottle {name} updated")