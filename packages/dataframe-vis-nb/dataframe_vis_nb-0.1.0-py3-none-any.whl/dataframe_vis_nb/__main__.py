import subprocess, yaml, click, sys

@click.command()
@click.argument('notebook', type=str)
@click.argument('index', type=int)
@click.argument('datavis-command', type=str)
@click.argument('dataframe-file', type=str)
@click.option('--dataframe-var', default='df', help="Name of variable containing pandas DataFrame in data loading cell")
def cli(notebook, index, datavis_command, dataframe_file, dataframe_var):
    cmd = f"""datavis-cli load-dataframe {dataframe_file} {dataframe_var} | nbformat-cli cell add {notebook} {index} --distance 1 &&
    datavis-cli {datavis_command} {dataframe_var} | nbformat-cli cell add {notebook} {index} --distance 2"""

    subprocess.run(cmd, shell=True, text=True, check=True)

if __name__ == "__main__":
    cli()
