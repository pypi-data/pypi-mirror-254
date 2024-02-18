Notebook-vis-cli generates jupyter notebooks with two populated cells:
Cell 1) loads a pandas dataframe
Cell 2) code to display it in a specific type of visualization, with defaults explicitly described.

The idea is that data will be generated via an external pipeline, but visualizations need to be tweaked interactively.
It is a hassle to set up the jupyter notebook and boilerplate for the visualization in question,
so notebook-vis-cli does it for you.

