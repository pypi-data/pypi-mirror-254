# notebook_vis_cli.py
import click
import nbformat
import os
import yaml
import pandas as pd

# Function to create a new Jupyter notebook or load an existing one
def load_or_create_notebook(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            return nbformat.read(f, as_version=4)
    else:
        return nbformat.v4.new_notebook()

# Function to add a cell to a notebook
def add_cell(notebook, cell_type, content):
    cell = nbformat.v4.new_code_cell(content) if cell_type == 'code' else nbformat.v4.new_markdown_cell(content)
    notebook.cells.append(cell)

# Function to save the notebook
def save_notebook(notebook, filename):
    with open(filename, 'w') as f:
        nbformat.write(notebook, f)

# Function to create the data loading cell
def create_data_loading_cell(filename):
    return f'''
import pandas as pd
import yaml

with open("{filename}", 'r') as file:
    data = yaml.safe_load(file)

df = pd.DataFrame(data)
print(df.head())
print(df.describe())
'''

# Function to create a seaborn heatmap cell
def create_heatmap_cell():
    return '''
import seaborn as sns
import matplotlib.pyplot as plt
import colorcet as cc

# Default colormap is perceptually-accurate and colorblind-friendly
# See https://colorcet.com/index.html for details
# Displaying the heatmap using seaborn
# For detailed information on the parameters, visit:
# https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap

sns.heatmap(df, 
            vmin=None, 
            vmax=None, 
            cmap=cc.cm.CET_CBL1, 
            center=None, 
            robust=False, 
            annot=None, 
            fmt='.2g', 
            annot_kws=None, 
            linewidths=0, 
            linecolor='white', 
            cbar=True, 
            cbar_kws=None, 
            cbar_ax=None, 
            square=False, 
            xticklabels='auto', 
            yticklabels='auto', 
            mask=None, 
            ax=None)

plt.show()
'''

# Function to create a seaborn clustermap cell
def create_clustermap_cell():
    return '''
import seaborn as sns
import matplotlib.pyplot as plt
import colorcet as cc

# Default colormap is perceptually-accurate and colorblind-friendly
# See https://colorcet.com/index.html for details
# Seaborn clustermap documentation
# https://seaborn.pydata.org/generated/seaborn.clustermap.html
sns.clustermap(df, 
               pivot_kws=None, 
               method='average', 
               metric='euclidean', 
               z_score=None, 
               standard_scale=None, 
               figsize=(10, 10), 
               cbar_kws=None, 
               row_cluster=True, 
               col_cluster=True, 
               row_linkage=None, 
               col_linkage=None, 
               row_colors=None, 
               col_colors=None, 
               mask=None, 
               dendrogram_ratio=0.2, 
               colors_ratio=0.03, 
               cbar_pos=(0.02, 0.8, 0.05, 0.18), 
               tree_kws=None, 
               cmap=cc.cm.CET_CBL1)
plt.show()
'''

@click.group()
def cli():
    """
    CLI tool to extend Jupyter notebooks for data visualization.
    """
    pass

@click.command()
@click.argument('filename')
@click.argument('datafile')
def heatmap(filename, datafile):
    """
    Add cells to a notebook for loading data and displaying a heatmap.
    """
    notebook = load_or_create_notebook(filename)
    add_cell(notebook, 'code', create_data_loading_cell(datafile))
    add_cell(notebook, 'code', create_heatmap_cell())
    save_notebook(notebook, filename)

@click.command()
@click.argument('filename')
@click.argument('datafile')
def clustermap(filename, datafile):
    """
    Add cells to a notebook for loading data and displaying a clustermap.
    """
    notebook = load_or_create_notebook(filename)
    add_cell(notebook, 'code', create_data_loading_cell(datafile))
    add_cell(notebook, 'code', create_clustermap_cell())
    save_notebook(notebook, filename)

cli.add_command(heatmap)
cli.add_command(clustermap)

if __name__ == '__main__':
    cli()
