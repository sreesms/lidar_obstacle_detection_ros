#! /usr/bin/env python2
from traceback import print_tb
import rospy
from sensor_msgs.msg import LaserScan

class ObjectDetection:

    def __init__(self):
        rospy.init_node('laser_obstacle',anonymous=True)
        self.laser_sub = rospy.Subscriber('/scan',LaserScan,self.laser_callback)

    def laser_callback(self,data):
        self.scan_data = data
        self.process_data(self.scan_data)
    
    def process_data(self,scan_data):
        self.i = -30        #To get the data from -30deg to 30 degree of laser
        for self.i in range(30):
            
            self.range_data = scan_data.ranges[self.i]
            # print('Laser data:',self.range_data)
            self.i =self.i+1

            # If the Distance to the obstacle is less than 1.0 meteres, its detected.
            if self.range_data < 1.0:
                print("obstacle detectecd")    

if __name__=='__main__':
    ObjectDetection()
    rospy.spin()
