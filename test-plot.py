#!/usr/bin/env python
from motionrender.util import load_data
from motionrender.plot import plot_joint_frame


time_series_file = "data/joint-time-series.csv"
joint_graph_file = "data/joint-graph.csv"

figure = "subject-skeleton.png"


# load and parse the time series and defined joint graph of the data
time_df, joint_graph, joint_names = load_data(time_series_file, joint_graph_file)

# select the 2000th time series frame to plot
joint_frame = time_df.iloc[2000]

# create a figure of the selected time series frame
fig = plot_joint_frame(joint_frame, joint_graph, joint_names)

# save the figure
fig.savefig(figure)
