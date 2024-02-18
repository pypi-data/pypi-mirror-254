import click, pandas, yaml, sys, pickle, tabulate

def process_dataframe(df, python_command):
    # Execute the provided Python command on the DataFrame 'df'
    local_vars = {'df': df}
    if python_command is not None:
        exec(python_command, globals(), local_vars)
    return local_vars['df']

@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--python_command')
@click.option('--orient-in', type=click.Choice(['columns', 'index', 'tight']), default='columns')
@click.option('--from_raw_stdin', is_flag = True, default = False, help="Use raw stdin as input to DataFrame.from_dict(), otherwise call yaml.safe_load on it first")
@click.option('--layer', type=str, default = None, help='If DataFrame elements are dicts, replace them with element[layer]. Called after difference.')
def cli(ctx, python_command, orient_in, from_raw_stdin, layer):
    ctx.ensure_object(dict)
    stdin = sys.stdin

    if not from_raw_stdin:
        stdin = yaml.safe_load(stdin)
    df = pandas.DataFrame.from_dict(stdin, orient=orient_in)

    if layer is not None:
        df = df.map(lambda element: element[layer])


    df = process_dataframe(df, python_command)
    ctx.obj["df"] = df

@cli.group(name='to')
@click.pass_context
def to_group(ctx):
    pass

@to_group.command(name='dict')
@click.option('--orient', type=click.Choice(['dict', 'list', 'series', 'split', 'tight', 'records', 'index']), default='dict')
@click.option('--index', is_flag = True, default = True)
@click.option('--yaml', "to_yaml", is_flag = True, default = True)
@click.option('--echo/--no-echo', is_flag=True, default=True)
@click.pass_context
def to_dict(ctx, orient, index, to_yaml):
    df = ctx.obj['df']
    stdout = df.to_dict(orient=orient, index=index)
    if to_yaml:
        stdout = yaml.dump(stdout)
    if echo:
        click.echo(stdout)

@to_group.command(name='pickle')
@click.pass_context
@click.argument('path', type=str)
@click.argument('compression', default='infer')
@click.argument('protocol', default=pickle.HIGHEST_PROTOCOL)
@click.option('--storage_options', type=str)
@click.option('--echo/--no-echo', is_flag=True, default=False)
def to_pickle(ctx, path, compression, protocol, storage_options):
    df = ctx.obj['df']
    storage_options = None if storage_options is None else yaml.safe_load(storage_options)
    df.to_pickle(path, compression=compression, protocol=protocol, storage_options=storage_options)
    if echo:
        click.echo(result)

@to_group.command(name='markdown')
@click.pass_context
@click.option('--buf', default=None)
@click.option('--mode', default='wt')
@click.option('--storage_options', default=None)
@click.option('--kwargs', default='{}')
@click.option('--index', default=True)
@click.option('--echo/--no-echo', is_flag=True, default=True)
def to_markdown(ctx, buf, mode, storage_options, kwargs, index, echo):
    df = ctx.obj['df']
    kwargs = yaml.safe_load(kwargs)
    result = df.to_markdown(buf=buf, mode=mode, index=index, storage_options=storage_options, **kwargs)
    if echo:
        click.echo(result)

@to_group.command(name='clipboard')
@click.pass_context
@click.option('--excel', default=True)
@click.option('--sep', default=None)
@click.option('--kwargs', default='{}')
@click.option('--echo/--no-echo', is_flag=True, default=False)
def to_clipboard(ctx, excel, sep, kwargs, echo):
    df = ctx.obj['df']
    kwargs = yaml.safe_load(kwargs)
    result = df.to_clipboard(excel=excel, sep=sep, **kwargs)
    if echo:
        click.echo(result)

@to_group.command(name='csv')
@click.pass_context
@click.option('--path-or-buf', default=None, help='File path or object, if None is provided the result is returned as a string.')
@click.option('--sep', default=',', help='String of length 1. Field delimiter for the output file.')
@click.option('--na-rep', default='', help='Missing data representation.')
@click.option('--float-format', default=None, help='Format string for floating point numbers.')
@click.option('--columns', default=None, help='Columns to write.')
@click.option('--header', is_flag=True, default=True, help='Write out the column names. If a list of strings is given it is assumed to be aliases for the column names.')
@click.option('--index', is_flag=True, default=True, help='Write row names (index).')
@click.option('--index-label', default=None, help='Column label for index column(s) if desired. If None is given, and header and index are True, then the index names are used.')
@click.option('--mode', default='w', help='Python write mode, default “w”.')
@click.option('--encoding', default=None, help='A string representing the encoding to use in the output file, defaults to ‘utf-8’.')
@click.option('--compression', default='infer', help='Compression mode among the following possible values: {‘infer’, ‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None}.')
@click.option('--quoting', default=None, type=int, help='Control field quoting behavior per csv.QUOTE_* constants. Use one of QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2), or QUOTE_NONE (3).')
@click.option('--quotechar', default='"', help='String of length 1. Character used to quote fields.')
@click.option('--lineterminator', default=None, help='The newline character or character sequence to use in the output file.')
@click.option('--chunksize', default=None, type=int, help='Rows to write at a time.')
@click.option('--date-format', default=None, help='Format string for datetime objects.')
@click.option('--doublequote', is_flag=True, default=True, help='Control quoting of quotechar inside a field.')
@click.option('--escapechar', default=None, help='String of length 1. Character used to escape sep and quotechar when appropriate.')
@click.option('--decimal', default='.', help='Character recognized as decimal separator.')
@click.option('--errors', default='strict', help='Specifies how encoding and decoding errors are to be handled.')
@click.option('--storage-options', default=None, help='Storage options for the file buffer to write to.')
@click.option('--echo/--no-echo', is_flag=True, default=True)
def to_csv(ctx, path_or_buf, sep, na_rep, float_format, columns, header, index,
                         index_label, mode, encoding, compression, quoting, quotechar,
                         lineterminator, chunksize, date_format, doublequote, escapechar,
                         decimal, errors, storage_options, echo):
    df = ctx.obj['df']
    result = df.to_csv(path_or_buf=path_or_buf, sep=sep, na_rep=na_rep, 
                       float_format=float_format, columns=columns, header=header, 
                       index=index, index_label=index_label, mode=mode, 
                       encoding=encoding, compression=compression, quoting=quoting, 
                       quotechar=quotechar, lineterminator=lineterminator, 
                       chunksize=chunksize, date_format=date_format, 
                       doublequote=doublequote, escapechar=escapechar, 
                       decimal=decimal, errors=errors, storage_options=storage_options)
    if echo:
        click.echo(result)

if __name__ == "__main__":
    cli(obj={})
