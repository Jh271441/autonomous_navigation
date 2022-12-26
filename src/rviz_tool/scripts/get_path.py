#!/usr/bin/env python
import rospy
from nav_msgs.msg import Path, Odometry
from geometry_msgs.msg import Twist, PointStamped, PoseStamped

def odom_callback(odom):
    global path
    curr_pose = PoseStamped()
    curr_pose.header.frame_id = 'odom'
    curr_pose.header.stamp = rospy.Time.now()
    curr_pose.pose.position = odom.pose.pose.position
    # curr_pose.pose.position.x = pos.x + 2.0
    # curr_pose.pose.position.y = pos.y - 3.0
    # curr_pose.pose.position.z = 0.0
    curr_pose.pose.orientation = odom.pose.pose.orientation
    path.poses.append(curr_pose)
    _pub_path = rospy.Publisher('/path', Path, queue_size=1)
    _pub_path.publish(path)


if __name__ == '__main__':
    rospy.init_node('get_path')
    path = Path()
    path.header.stamp = rospy.Time.now()
    path.header.frame_id = 'odom'
    rospy.Subscriber('/odometry/filtered', Odometry, odom_callback)
    rospy.spin()