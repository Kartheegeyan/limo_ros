#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from limo_base.msg import LimoStatus    
from limo_status_translator.srv import GetLimoStatus, GetLimoStatusResponse

def callback(data):
    rospy.loginfo("Subscribed to " + data.vehicle_state)

def status_handler(request):
    print("Request received.")
    if (request.vehicle_state == 0):
        return GetLimoStatusResponse("Vehicle is functioning normally.")
    elif (request.vehicle_state == 2):
        return GetLimoStatusResponse("Vehicle is not functioning normally.")


def status_translator_server():
    rospy.init_node('translator_server', anonymous=True)
    rospy.Service('translate', GetLimoStatus, status_handler)

    rospy.Subscriber('limo_status', LimoStatus, callback)
    rospy.spin()

if __name__ == "__main__":
    status_translator_server()
    


