import rospy
from std_msgs.msg import String
from rosgraph_msgs.msg import Clock


	
def listener():

	rospy.init_node('listener', anonymous=True)
	a =rospy.wait_for_message("clock", Clock)
	b = str(a).split(":")
	print(int(b[3]))
	print(int(b[2][:5]))
	
	for i in range (len(b)):
		rospy.loginfo(b[i])
	


if __name__ == '__main__':
	listener()
