#!/usr/bin/env python
import subprocess
import gc
import rospy
import os 
from rosgraph_msgs.msg import Clock

popen = subprocess.Popen("gzclient -g libsystem_gui.so".split(),stdout=subprocess.PIPE)	
x =0.0
y = 0.0
z = 0.0
seq = 0

while True:
	for line in iter(popen.stdout.readline,""):
		try:	
			line_s = line.split()
			x = float(line_s[3])
			y = float(line_s[4])
			z = float(line_s [5])
			sec, nsec=listener()
			print(sec, nsec)


			cmd = '''rostopic pub -1 /move_base_simple/goal geometry_msgs/PoseStamped "header: 
  seq: {seq}
  stamp: 
    secs: {sec}
    nsecs: {n_sec}
  frame_id: "map"
pose: 
  position: 
    x: {x}
    y: {y}
    z: 0.0
  orientation: 
    x: 0.0
    y: 0.0
    z: 0.999430043569
    w: -0.0337577844632"'''.format(seq = seq, sec=sec, n_sec = nsec, x=x, y=y)

			
				
			os.system(cmd)
			seq +=1



		except:
			print("no")

	
def listener():

	rospy.init_node('listener', anonymous=True)
	a =rospy.wait_for_message("clock", Clock)
	b = str(a).split(":")
	
	return(b[2], b[3])
	


	
