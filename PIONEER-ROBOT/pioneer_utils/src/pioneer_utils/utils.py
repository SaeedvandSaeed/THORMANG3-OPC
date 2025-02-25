#!/usr/bin/env python3

import math
import rospy
import numpy as np 

def quaternion_to_euler(x, y, z, w):
    t0      = +2.0 * (w * x + y * z)
    t1      = +1.0 - 2.0 * (x * x + y * y)
    roll    = math.atan2(t0, t1)
    t2      = +2.0 * (w * y - z * x)
    t2      = +1.0 if t2 > +1.0 else t2
    t2      = -1.0 if t2 < -1.0 else t2
    pitch   = math.asin(t2)
    t3      = +2.0 * (w * z + x * y)
    t4      = +1.0 - 2.0 * (y * y + z * z)
    yaw     = math.atan2(t3, t4)
    return [roll, pitch, yaw]

def euler_to_quaternion(roll, pitch, yaw):
    qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    return [qx, qy, qz, qw]