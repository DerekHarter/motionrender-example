#!/usr/bin/env python
from motionrender import MotionRender

# example of rendering a captured frame from the standing subject
time_series_file = "data/standing-subject.csv"
joint_graph_file = "data/standing-joint-graph.csv"
figure = "standing-subject.png"

# load and parse the time series and defined joint graph of the data
# and plot the frame captured at the given time stamp
mr = MotionRender(time_series_file, joint_graph_file)
time_stamp = 1636576712852000
mr.render_frame(time_stamp, figure_name=figure)


# example of rendering a frame of the sitting subject
time_series_file = "data/sitting-subject.csv"
joint_graph_file = "data/sitting-joint-graph.csv"
figure = "sitting-subject.png"

# for this subject, demonstrate modifying some of
# the plotting parameters that control how the figure
# is rendered
mr = MotionRender(time_series_file, joint_graph_file)
mr._ax_elevation = -100
mr._ax_azimuth = 70
time_stamp = 1636576712885000
mr.render_frame(time_stamp, figure_name=figure, figsize=(10,20))
