import nbformat
import os
import re

# Initialize 'notebook' to the current working directory
notebook = None
last = None

def set_notebook(notebook_filename, dir = None):
    global notebook
    if dir is None:
        notebook = f"{os.getcwd()}/{notebook_filename}"
    else:
        notebook = notebook_filename

def read_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        return nbformat.read(f, as_version=4)

def unique(input_str):
    global notebook
    if notebook is None:
        raise ValueError("Notebook not set")

    nb = read_notebook(notebook)
    cell_contents = [cell['source'] for cell in nb.cells]

    num = 0
    unique_str = f"{input_str}{num}"
    while any(unique_str in content for content in cell_contents):
        num += 1
        unique_str = f"{input_str}{num}"

    return unique_str

def lastidx():
    global notebook, last
    if notebook is None:
        raise ValueError("Notebook not set")
    if last is None:
        raise ValueError("sanb.last not set")

    nb = read_notebook(notebook)
    cell_contents = [cell['source'] for cell in nb.cells]

    # Construct a regex pattern that matches a cell starting with 'sanb.last' followed by the value of 'last'
    # It accounts for any syntactically valid whitespace and quotes
    pattern = re.compile(rf"^sanb\.last\s*=\s*[\"']?{re.escape(last)}[\"']?", re.MULTILINE)

    indices = [i for i, content in enumerate(cell_contents) if pattern.match(content)]

    if len(indices) != 1:
        raise ValueError(f"Cell starting with sanb.last = '{last}' is found in {len(indices)} cells, should be in exactly 1")

    return indices[0]

def index(search_last):
    global notebook
    if notebook is None:
        raise ValueError("Notebook not set")

    nb = read_notebook(notebook)
    cell_contents = [cell['source'] for cell in nb.cells]

    pattern = re.compile(rf"^sanb\.last\s*=\s*[\"']?{re.escape(search_last)}[\"']?", re.MULTILINE)

    indices = [i for i, content in enumerate(cell_contents) if pattern.match(content)]

    if len(indices) != 1:
        raise ValueError(f"Cell starting with sanb.last = '{search_last}' is found in {len(indices)} cells, should be in exactly 1")

    return indices[0]