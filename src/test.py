#!/usr/bin/python

import rospy
import math
import tf
import geometry_msgs.msg
from std_msgs.msg import String

# runs main functionality 
def run():
	demo_robot_marker = 'ar_marker_4'

	# mapping between each ar_marker ID and object in scene
	map = {'ar_marker_4':'robot', 'ar_marker_0':'cube_1',  'ar_marker_1':'cube_2', 'ar_marker_2':'cube_3'}
	states = dict()
	goal = None

	# transform listener to listen to ar_markers
	tf_listener = tf.TransformListener()

	rate = rospy.Rate(10.0)
	while not rospy.is_shutdown():
		try:
			# lookup transform between the usb_cam adn the demonstrator robot ar tag
			(trans, rot) = listener.lookupTransform('usb_cam', demo_robot_marker, rospy.Time(0))
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException)
			continue

		pt_pose = Pose(Quaternion(0, 0, 0, 1), pt), rospy.Time(0), demo_robot_marker)
		tf_pt_pose = None;
		# transform from ar_marker to usb_cam frame
		tf_listener.transformPose("usb_cam", pt_pose, tf_pt_pose)

		# get xyz of demonstrator robot
		geometry_msgs.Point ro_pt = None
		ro_pt.x = tf_pt_pose.getOrigin().x()
		ro_pt.y = tf_pt_pose.getOrigin().y()
		ro_pt.z = tf_pt_pose.getOrigin().z()	

		rate.sleep()

		'''
		rospy.init_node('listener', anonymous=True)
		rospy.Subscriber("usb_cam/camera_info", String, callback)
		'''

if __name__ == '__main__':
	run()
