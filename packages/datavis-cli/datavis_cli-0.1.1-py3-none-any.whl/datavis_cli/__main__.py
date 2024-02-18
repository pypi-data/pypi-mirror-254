import click
import os
import yaml
import pandas as pd

@click.group()
def cli():
    """
    CLI tool to output boilerplate code for data loading and visualization
    """
    pass

# Function to create the data loading cell
@click.command()
@click.argument('filename')
@click.argument('dataframe_name')
def load_dataframe(filename, dataframe_name):
    click.echo(f'''
import pandas as pd
import yaml

with open("{filename}", 'r') as file:
    {dataframe_name} = pd.DataFrame(yaml.safe_load(file))
print({dataframe_name}.head())
print({dataframe_name}.describe())
''')

@click.command()
@click.argument('dataframe_name')
def heatmap(dataframe_name):
    """
    Output code to generate Seaborn heatmap
    """
    click.echo(f'''
import seaborn as sns
import matplotlib.pyplot as plt
import colorcet as cc

# Default colormap is perceptually-accurate and colorblind-friendly
# See https://colorcet.com/index.html for details
# Displaying the heatmap using seaborn
# For detailed information on the parameters, visit:
# https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap

sns.heatmap({dataframe_name}, 
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
''')


@click.command()
@click.argument('dataframe_name')
def clustermap(dataframe_name):
    """
    Output code to generate Seaborn clustermap
    """
    click.echo(f'''
import seaborn as sns
import matplotlib.pyplot as plt
import colorcet as cc

# Default colormap is perceptually-accurate and colorblind-friendly
# See https://colorcet.com/index.html for details
# Seaborn clustermap documentation
# https://seaborn.pydata.org/generated/seaborn.clustermap.html
sns.clustermap({dataframe_name}, 
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
''')

cli.add_command(load_dataframe)
cli.add_command(heatmap)
cli.add_command(clustermap)

if __name__ == '__main__':
    cli()
