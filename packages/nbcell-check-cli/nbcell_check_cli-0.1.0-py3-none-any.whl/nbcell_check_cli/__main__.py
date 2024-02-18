import click
import nbformat
import re

def read_notebook_cells(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    return [cell['source'] for cell in nb.cells]

@click.group()
def cli():
    pass

@cli.command()
@click.argument('filename')
@click.argument('pattern')
def match(filename, pattern):
    cells = read_notebook_cells(filename)
    matched_indices = [str(i) for i, cell in enumerate(cells) if re.match(pattern, cell)]
    click.echo(' '.join(matched_indices))

@cli.command()
@click.argument('filename')
@click.argument('pattern')
def search(filename, pattern):
    cells = read_notebook_cells(filename)
    matched_indices = [str(i) for i, cell in enumerate(cells) if re.search(pattern, cell)]
    click.echo(' '.join(matched_indices))

@cli.command()
@click.argument('filename')
@click.argument('pattern')
def fullmatch(filename, pattern):
    cells = read_notebook_cells(filename)
    matched_indices = [str(i) for i, cell in enumerate(cells) if re.fullmatch(pattern, cell)]
    click.echo(' '.join(matched_indices))

if __name__ == '__main__':
    cli()
