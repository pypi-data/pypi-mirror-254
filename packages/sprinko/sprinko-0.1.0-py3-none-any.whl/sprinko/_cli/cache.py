import datetime
import os
import shutil
import click
from sprinko.base import caching_dir, CacheEntry, caching_cfg as caching
from sprinko.base.caching import prune_cache
from sprinko.extra.prompt import create_table_selector, TableSelector
from tabulate import tabulate
import humanize
@click.group("cache")
def cacheGroup():
    pass

@cacheGroup.command("list", help="List all the cache entries")
@click.option("--omit-checksum", "-oc", is_flag=True, help="Omit the checksum column")
@click.option("--omit-pull", "-op", is_flag=True, help="Omit the next pull column")
@click.option("--pretty", "-p", is_flag=True, help="Simple output")
def cache_list(omit_checksum, omit_pull, pretty):
    tabdata = [[]]
    if not caching:
        click.echo("Nothing in cache")
        return
    
    tabdata[0].append("Path")
    if not omit_checksum:
        tabdata[0].append("Checksum")
    
    if not omit_pull:
        tabdata[0].append("Last Pull")
        tabdata[0].append("Expected Next Pull")
    
    for k, v in caching.items():
        v : CacheEntry
        
        thistab = []
        
        thistab.append(k)
        
        if not omit_checksum:
            thistab.append(v.get("checksum", "N/A"))
            
        if not omit_pull:
            lastpull = v.get("lastPulled", None)
            updateinterval = v.get("updatableInterval", None)
            
            nextpull = None
            if lastpull is not None and updateinterval is not None:
                lastpull = datetime.datetime.fromisoformat(lastpull)
                nextpull = lastpull + datetime.timedelta(seconds=updateinterval)
            
            thistab.append(humanize.naturaltime(lastpull) if lastpull is not None else "N/A")
            thistab.append(humanize.naturaltime(nextpull) if nextpull is not None else "N/A")
            
        tabdata.append(thistab)
        
    if not pretty:
        print(tabulate(tabdata, headers="firstrow"))
        return
        
    create_table_selector(tabdata)
    
@cacheGroup.command("defer", help="Defer the update interval for a given cache entry")
@click.argument("value", type=click.INT)
@click.option("--path", "-p", help="Path of the cache entry")
@click.option("--unit", "-u", type=click.Choice(["s", "m", "h", "d"]), default="s", help="Unit of the update interval")
@click.option("--relative", "-r", is_flag=True, help="Use relative time")
@click.option("--no-clr-screen", "-n", is_flag=True, help="Don't clear the screen")
def cache_defer(value, path, unit, relative, no_clr_screen):
    if not path:
        choices = list(zip([ i for i in range(len(caching))], caching.keys()))
        choices.insert(0, ("Index", "Path"))
        dialog : TableSelector = create_table_selector(choices, returnDialog=True)
        path = dialog.selected_row_data[1]
        # clear screen
        if not no_clr_screen:
            os.system('cls' if os.name == 'nt' else 'clear')
        
        click.echo(f"Selected {path}")
        
    if path not in caching:
        click.echo(f"Path {path} not in cache")
        return
    
    existingInterval = caching[path].get("updatableInterval", 0)
    if existingInterval:
        existingInterval = int(existingInterval)
    else:
        existingInterval = 0
    
    match (unit, relative):
        case ("s", False):
            targetInterval = value
        case ("m", False):
            targetInterval = value * 60
        case ("h", False):
            targetInterval = value * 60 * 60
        case ("d", False):
            targetInterval = value * 60 * 60 * 24
        case ("s", True):
            targetInterval = existingInterval + value
        case ("m", True):
            targetInterval = existingInterval + (value * 60)
        case ("h", True):
            targetInterval = existingInterval + (value * 60 * 60)
        case ("d", True):
            targetInterval = existingInterval + (value * 60 * 60 * 24)
        case _:
            click.echo(f"Invalid unit {unit}")
            return
    
    click.echo(f"Updated interval for {path} to {targetInterval} seconds")
    
    caching[path]["updatableInterval"] = targetInterval
    caching._save()

@cacheGroup.command("purge", help="Purge the cache")
def cache_purge():
    caching.clear()
    shutil.rmtree(caching_dir, ignore_errors=True)
    os.makedirs(caching_dir, exist_ok=True)
    
    click.echo("Cleared cache")
    
@cacheGroup.command("clear", help="Clear the cache")
def cache_clear():
    cache_purge()    

@cacheGroup.command("prune", help="Prune obsolete cache entries")
def cache_prune():
    prune_cache()