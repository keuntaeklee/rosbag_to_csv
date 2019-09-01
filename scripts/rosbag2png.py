# coding:utf-8
#!/usr/bin/python
 
# Extract images from a bag file.
 
#PKG = 'beginner_tutorials'
import roslib;   #roslib.load_manifest(PKG)
import rosbag
import rospy
import cv2
import os, sys
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
 
# Reading bag filename from command line or roslaunch parameter.
#import os
#import sys
 
rgb_path = '/home/klee698/flightgoggles_bags/'

# bag_name = "2019-08-23-12-31-08"

class ImageCreator():
    def __init__(self, bag_name):
        self.bridge = CvBridge()
        with rosbag.Bag(rgb_path + bag_name + ".bag", 'r') as bag: #bag file to be read;
            i = 0
            for topic,msg,t in bag.read_messages():
                if topic == "/uav/camera/left/image_color/compressed": #topic of the image;
                    try:
                        cv_image = self.bridge.compressed_imgmsg_to_cv2(msg,"bgr8")
                    except CvBridgeError as e:
                        print(e)
                    timestr = "%.6f" %  msg.header.stamp.to_sec()
                    image_seq_name = str(i).zfill(16) + ".png" #Image Naming: 0000001.png
                    #%.6f means that there are 6 digits after the decimal point, which can be modified according to the accuracy;
                    image_name = timestr+ ".png" #Image Naming: Timestamp.png
                    cv2.imwrite(rgb_path + bag_name + "/timestamp/"+ image_name, cv_image) #Save;
                    cv2.imwrite(rgb_path + bag_name + "/seq/"+ image_seq_name, cv_image) #Save;
                    i += 1

if __name__ == '__main__':
    files = os.listdir(rgb_path)
    for bag_fullname in files:
        if bag_fullname.endswith('.bag'):
            bag_name = bag_fullname.split(".")[0]
            print(bag_name)
            os.mkdir(rgb_path + bag_name)
            os.mkdir(rgb_path + bag_name + "/seq")
            os.mkdir(rgb_path + bag_name + "/timestamp")
            try:
                image_creator = ImageCreator(bag_name)
            except rospy.ROSInterruptException:
                pass
