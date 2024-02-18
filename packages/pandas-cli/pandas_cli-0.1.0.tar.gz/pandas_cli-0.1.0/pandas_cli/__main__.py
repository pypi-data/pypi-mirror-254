import click
import pandas as pd
import yaml
import sys

@click.command()
@click.argument('python_command', type=str)
@click.option('--nodump', is_flag=True, help="If set, does not dump dataframe to YAML in stdout after command execution.")
def cli(python_command, nodump):
    # Read YAML data from stdin
    yaml_data = yaml.safe_load(sys.stdin)

    # Convert the YAML data to a Pandas DataFrame
    df = pd.DataFrame(yaml_data)

    # Execute the provided Python command on the DataFrame 'a'
    local_vars = locals()

    exec(python_command, globals(), local_vars)

    if not nodump:
        click.echo(yaml.dump(local_vars['df'].to_dict(orient='records')))

if __name__ == "__main__":
    cli()
