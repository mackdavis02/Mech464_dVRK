#!/usr/bin/env python

# Author: Team3
# Date: 2024-03-08

# This file is for initalization of camera / ECM 

#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from sensor_msgs.msg import JointState
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
# import cv2
import numpy as np
import dvrk 
import sys
from scipy.spatial.transform import Rotation as R
import os
import arm
import camera
import time
import json


if __name__ == '__main__':

    rospy.init_node('topic_publisher')
    rate = rospy.Rate(140)

    ECM = arm.robot('ECM')
    left_cam = camera.camera('left')
    right_cam = camera.camera('right')

    #Get ECM data
    ECM_jp = ECM.get_current_joint_position()
    ECM_ee = ECM.get_current_cartesian_position()
    ECM_Orientation_Matrix = ECM.get_current_orientation_matrix()