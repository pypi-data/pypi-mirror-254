import click
import pandas as pd
import yaml
import sys
from io import StringIO

@click.group()
def cli():
    pass

def process_dataframe(df, python_command, orient_out, nodump):
    # Execute the provided Python command on the DataFrame 'df'
    local_vars = {'df': df}
    exec(python_command, globals(), local_vars)
    df = local_vars['df']

    # Optionally dump the DataFrame to YAML
    if not nodump:
        click.echo(yaml.dump(df.to_dict(orient=orient_out)))

@cli.command()
@click.argument('python_command', type=str)
@click.option('--orient_out', default='index', help='Sets the output orientation')
@click.option('--nodump', is_flag=True, help="If set, does not dump dataframe to YAML after command execution.")
def from_dict(python_command, orient_out, nodump):
    """ Loads DataFrame from dict. """
    yaml_data = yaml.safe_load(sys.stdin)
    df = pd.DataFrame.from_dict(yaml_data, orient='index')
    process_dataframe(df, python_command, orient_out, nodump)

@cli.command()
@click.argument('python_command', type=str)
@click.option('--orient_out', default='index', help='Sets the output orientation')
@click.option('--nodump', is_flag=True, help="If set, does not dump dataframe to YAML after command execution.")
def from_records(python_command, orient_out, nodump):
    """ Loads DataFrame from records. """
    yaml_data = yaml.safe_load(sys.stdin)
    df = pd.DataFrame.from_records(yaml_data)
    process_dataframe(df, python_command, orient_out, nodump)

@cli.command()
@click.argument('python_command', type=str)
@click.option('--orient_out', default='index', help='Sets the output orientation')
@click.option('--nodump', is_flag=True, help="If set, does not dump dataframe to YAML after command execution.")
def from_items(python_command, orient_out, nodump):
    """ Loads DataFrame from items. """
    yaml_data = yaml.safe_load(sys.stdin)
    df = pd.DataFrame.from_items(yaml_data)
    process_dataframe(df, python_command, orient_out, nodump)

@cli.command()
@click.argument('python_command', type=str)
@click.option('--filepath_or_buffer', type=str, required=True, help='File path or buffer for CSV data.')
@click.option('--orient_out', default='index', help='Sets the output orientation')
@click.option('--nodump', is_flag=True, help="If set, does not dump dataframe to YAML after command execution.")
def from_csv(python_command, filepath_or_buffer, orient_out, nodump):
    """ Loads DataFrame from a CSV file. """
    df = pd.read_csv(filepath_or_buffer)
    process_dataframe(df, python_command, orient_out, nodump)

@cli.command()
@click.argument('python_command', type=str)
@click.option('--orient_out', default='index', help='Sets the output orientation')
@click.option('--nodump', is_flag=True, help="If set, does not dump dataframe to YAML after command execution.")
def dataframe(python_command, orient_out, nodump):
    """ Use the normal DataFrame constructor. """
    yaml_data = yaml.safe_load(sys.stdin)
    df = pd.DataFrame(yaml_data)
    process_dataframe(df, python_command, orient_out, nodump)

if __name__ == "__main__":
    cli()
