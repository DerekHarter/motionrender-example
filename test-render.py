#!/usr/bin/env python
from motionrender import MotionRender

# render the whole standing subject motion capture
time_series_file = "data/standing-subject.csv"
joint_graph_file = "data/standing-joint-graph.csv"
movie = "standing-subject.mov"

# load and parse data, set render parameter and create movie
mr = MotionRender(time_series_file, joint_graph_file)
mr._animation_progress_interval = 100
mr.render_animation(movie_name=movie)


# render the sitting subject data
time_series_file = "data/sitting-subject.csv"
joint_graph_file = "data/sitting-joint-graph.csv"
movie = "sitting-subject.mov"

# example of cutting out a portion of the full capture, and
# modifying some of the viewing rendering parameters
mr = MotionRender(time_series_file, joint_graph_file)
mr._animation_progress_interval = 10
mr._ax_xlim3d = [-40, 0]
mr._ax_ylim3d = [-100, 30]
mr._ax_elevation = -100
mr._ax_azimuth = 90
mr._ax_animation_frame_interval=25
begin_ts = 1636576699596000
end_ts = 1636576704588000
mr.render_animation(begin_ts=begin_ts, end_ts=end_ts,
                    movie_name=movie, figsize=(10,20))
