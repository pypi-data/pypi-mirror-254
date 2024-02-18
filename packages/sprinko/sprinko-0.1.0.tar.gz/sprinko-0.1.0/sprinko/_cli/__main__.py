import logging
import click
import os
import sys
from tabulate import tabulate

tpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
if tpath not in sys.path:
    sys.path.append(tpath)
from sprinko._cli.cache import cacheGroup
from sprinko._cli.bottle import bottleGroup
from sprinko._cli_bottler.__main__ import bottler, appdata
from sprinko._cli.script import scriptGroup

@click.group(invoke_without_command=True)
@click.option("--debug", "-d", is_flag=True)
@click.pass_context
def bowl_(ctx : click.Context, debug):
    if debug:
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
        
    if ctx.invoked_subcommand is None:
        # give help
        return ctx.invoke(list_all)
    

def print_cmds(c : click.Group, heading =[]):
    ret = []
    for k, v in c.commands.items():
        if not isinstance(v, click.Group):
            res = "/".join(heading + [k])
            #print(f"{res}\t\t{v.help}")
            ret.append((res, v.help,))
        else:
            ret.extend(print_cmds(v, heading + [k]))
        
    return ret    

@bowl_.command("cmd-list", help="List all the commands")
def list_all():
    data = print_cmds(bowl_)
    click.echo(tabulate(data, headers=["Command", "Help"]))

bowl_.add_command(cacheGroup)
bowl_.add_command(bottleGroup)
bowl_.add_command(bottler)
bowl_.add_command(scriptGroup)
bowl_.add_command(appdata)

if __name__ == "__main__":
    bowl_()