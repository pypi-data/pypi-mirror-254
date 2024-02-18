import click
import nbformat
import sys
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

@click.group()
def cli():
    """A CLI for nbformat operations."""
    pass

@cli.group()
def notebook():
    """Commands to manipulate the entire notebook."""
    pass

@cli.group()
def cell():
    """Commands to manipulate notebook cells."""
    pass

@cell.command()
@click.argument('notebook_path')
@click.argument('anchor_index', type=int)
@click.option('--distance', default=0, help="Distance from [anchor_index] of added cell")
@click.option('--cell_type', default='code', help="Type of cell to add")
def add(notebook_path, anchor_index, distance, cell_type):
    """Add a new cell to a notebook."""
    try:
        content = sys.stdin.read()
        location = anchor_index + distance
        with open(notebook_path, 'r') as f:
            nb = nbformat.read(f, as_version=4)

        if cell_type == 'code':
            new_cell = new_code_cell(content)
        elif cell_type == 'markdown':
            new_cell = new_markdown_cell(content)
        else:
            raise ValueError("Cell type must be 'code' or 'markdown'")

        nb.cells.insert(location, new_cell)

        with open(notebook_path, 'w') as f:
            nbformat.write(nb, f)

        click.echo(f"Cell added at index {location} in '{notebook_path}'.")

    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    cli()
