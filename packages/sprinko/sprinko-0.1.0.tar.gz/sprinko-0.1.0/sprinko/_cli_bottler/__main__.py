import os
import click
import sys
tpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
if tpath not in sys.path:
    sys.path.append(tpath)
    
from sprinko.extra.file import touch_file
from sprinko.extra.zip import make_zip

default_updatable_list = [".py"]

@click.group()
def bottler():
    pass

@bottler.command("init", help="Create a new Bottle")
@click.argument("name")
def _init_workplace(name):
    os.makedirs(os.path.join(os.getcwd(), name), exist_ok=True)
    touch_file(os.path.join(os.getcwd(), name, "bottle.toml"))
    click.echo(f"Created {name} bottle")
    
@bottler.command("pack", help="Pack a Bottle")
@click.argument("name")
def _pack(name):
    bottle_path = os.path.join(os.getcwd(), name)
    #bottle_toml = os.path.join(bottle_path, "bottle.toml")
    bottle_zip = os.path.join(bottle_path, "bottle.zip")
    
    #bottle_config = toml.load(bottle_toml)
    
    existing_files = os.listdir(bottle_path)
    # parsing crlf to lf
    for fn in existing_files:
        if not any(fn.endswith(ext) for ext in default_updatable_list):
            continue
        
        
        with open(os.path.join(bottle_path, fn), "r+", encoding="utf-8") as f:
            content = f.read()
            if "\r\n" not in content:
                continue
            
            click.echo(f"Parsing {fn}")
            
            content = content.replace("\r\n", "\n")
            f.seek(0)
            f.write(content)
            f.truncate()
    
    # check if total existing files size exceed 25 mb
    existing_size = sum([os.path.getsize(os.path.join(bottle_path, f)) for f in existing_files])
    if existing_size > 25 * 1024 * 1024:
        return click.echo("Total size of existing files exceed 25mb, aborted packing")
    
    res = make_zip(bottle_path, ["bottle.zip"], targetPath=bottle_zip)
    if not res:
        return click.echo("Everything remains the same, nothing to pack")
    
    click.echo(f"Bottle {name} packed")

@bottler.command("list", help="List all local bottles")
def _list(echo : bool = True):
    ret = []
    for path in os.listdir(os.getcwd()):
        if not os.path.isdir(os.path.join(os.getcwd(), path)):
            continue
        
        if os.path.exists(os.path.join(path, "bottle.toml")):
            ret.append(path)
            if echo:
                click.echo(path)
                
    return ret
    
@bottler.command("packall", help="Pack all local bottles")
@click.option("--cwdpath", "-cp", type=click.Path(exists=True), default=os.getcwd(), help="Path of the Bottle")
def _packall(cwdpath):
    def owclickecho(msg, **kwargs):
        old_click_echo(f"> {msg}", **kwargs) 
    
    os.chdir(cwdpath)
    for path in _list.callback(echo=False):
        click.echo(f"Bottle {path} discovered")
        
        old_click_echo = click.echo
        
        click.echo = owclickecho
        
        _pack.callback(path)
        
        click.echo = old_click_echo
        
@click.command("appdata", help="opens appdata folder")
def appdata():
    os.startfile(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "appdata"))
        
def bottler_cli():
    bottler.add_command(appdata)
    bottler()
        
if __name__ == "__main__":
    bottler.add_command(appdata)
    bottler()