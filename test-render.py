#!/usr/bin/env python
from motionrender.util import load_data
from motionrender.render import render_animation

time_series_file = "data/joint-time-series.csv"
joint_graph_file = "data/joint-graph.csv"

movie = "subject-skeleton.mov"

# load and parse the time series and defined joint graph of the data
time_df, joint_graph, joint_names = load_data(time_series_file, joint_graph_file)

# create an animation object of the joint motion capture time series
# NOTE: will take some time to render all 3500+ frames
ani = render_animation(time_df, joint_graph, joint_names)

# save the animation
ani.save(movie)
