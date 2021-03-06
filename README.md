# SLAM Project
Project on Simultaneous Localization and Mapping (SLAM) which implements Extended Kalman Filter (EKF) SLAM and FastSLAM (Particle based). This is based on the [SLAM course by Claus Brenner](https://www.youtube.com/playlist?list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm) which uses a LEGO robot in a 2000mm X 2000mm arena with 6 landmarks which serve as map features. The robot is equipped with a LIDAR sensor to generate scan data.

## Requirements
1. Python 3
2. Tkinter
3. Numpy

## Instructions
Run the files for EKF SLAM and FastSLAM in Python.
EKF SLAM:
```shell
$ python EKF_SLAM.py
```
FastSLAM:
```shell
$ python FastSLAM.py
```
These generate the output files ekf_slam_output.txt and fast_slam_output.txt which can be viewed in the logfile viewer
```shell
$ python logfile_viewer.py
```
