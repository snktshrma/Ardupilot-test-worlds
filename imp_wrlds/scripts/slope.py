#!/usr/bin/env python

import rospy
import time
from imp_wrlds.msg import terr_data

rospy.init_node('slope', anonymous=True)

data = terr_data()
data.x = 0
data.z = 0

pub = rospy.Publisher('/steep_terrain/raw', terr_data, queue_size=10)

buf_x = -0
buf_y = 0
def main():
	global buf_y, buf_x
	ar_x = [0,40,253,253]
	ar_y = [0,30,30,0]

	for x in range(len(ar_x)):
		data.x = ar_x[x]
		data.z = ar_y[x]
		pub.publish(data)
		time.sleep(0.5)

if __name__ == '__main__':
	while not rospy.is_shutdown():
		main()