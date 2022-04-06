import rospy
from sensor_msgs.msg import LaserScan


class ObjectDetection():
    def _init_():
        self.laser_sub = self.rospy.Subscriber('/scan',LaserScan,self.laser_callback)

    def laser_callback(data):
        self.laser_data = data.ranges[i]
        self.process_data(self.laser_data)
    
    def process_data(self,laser_ranges):
        for i in ranges(30):
            print('Laser data:',laser_ranges)

            # If the Distance to the obstacle is less than 0.5 meteres, its detected.
            if laser_ranges < 0.5:
                print("obstacle detectecd")    

if __name__=='__main__':
    rospy.init('Obstacle Detection Node',anonymous=True)
    ObjectDetection()
    rospy.spin()
