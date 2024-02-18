
import click

from sprinko.core.bottle import Bottle
from sprinko.core.bowl import Bowl

@click.group("script")
def scriptGroup():
    pass

@scriptGroup.command("list", help="List all installed scripts")
def scriptList():
    for x in Bottle.instances().values():
        click.echo(f"[{x.name}]")
        for y in x.scriptlist.keys():
            click.echo(f"{y}")

@scriptGroup.command("run", help="Run scripts")
@click.argument("script", nargs=-1)
@click.option("--scenario", "-s", help="Save or use as scenario")
@click.option("--unsafe", "-u", is_flag=True, help="Unsafe mode")
def scriptRun(script : list, scenario : str, unsafe : bool):
    if len(script) == 0 and scenario is None:
        raise click.ClickException("Please specify a script")
    
    bowl = Bowl()
    
    if len(script) == 0:
        click.echo("Running scenario: " + scenario)
        return bowl.run_scenario(scenario, allowUnsafe=unsafe)
    
    if scenario:
        bowl.set_sceanrio(scenario, script, override=True)
    bowl.run(*script, allowUnsafe=unsafe)

    click.echo("Done")
    
@scriptGroup.command("gen", help="Generate file")
@click.argument("script", nargs=-1)
@click.option("--scenario", "-s", help="Save or use as scenario")
@click.option("--unsafe", "-u", is_flag=True, help="Unsafe mode")
def scriptGen(script : list, scenario : str, unsafe : bool):
    if len(script) == 0 and scenario is None:
        raise click.ClickException("Please specify a script")
    
    bowl = Bowl()
    
    if len(script) == 0:
        click.echo("Generating scenario: " + scenario)
        res = bowl.gen_scenario(scenario)
        with open(f"{scenario}.py", "w") as f:
            f.write(res)
        return
    
    if scenario:
        bowl.set_sceanrio(scenario, script, override=True)
    
    res = bowl.gen(*script, allowUnsafe=unsafe)
    scenario = scenario if scenario else "script"
    with open(f"{scenario}.py", "w") as f:
        f.write(res)
    
    click.echo("Done")
    