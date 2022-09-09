#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32



def laser_cb(msg):
    #print (len(msg.ranges))
    left = msg.ranges[118] * 100# LEFT
    mid = msg.ranges[1]  *100#MID
    right = msg.ranges[343] *100#RIGHT
    


    laser_pub_left =rospy.Publisher('/leftLaser', Float32, queue_size =10 )
    laser_pub_mid =rospy.Publisher('/midLaser', Float32, queue_size =10 )
    laser_pub_right =rospy.Publisher('/rightLaser', Float32, queue_size =10 )
    
    laser_pub_left.publish(left)
    laser_pub_mid.publish(mid)
    laser_pub_right.publish(right)

rospy.init_node('laser_readings_node')
laser_sub =rospy.Subscriber('/scan', LaserScan, laser_cb)


rospy.spin()
