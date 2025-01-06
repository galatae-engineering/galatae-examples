from robot_library import Robot
import time

# TARGET CONFIGURATION
x_pos = 150
y_pos = 150
z_pos = 0
x_final_pos = 130
y_final_pos = 20
z_final_pos = 90 # destination (hauteur du verre)
pressure_force = 20 # extra_degree
bottle_diameter = 75 # pour connaitre la distance d'engagement avant pincer
bottle_grip_hight = 100 # hauteur entre la pince et le bouchon de la bouteille (pour verser dans le verre)
bottle_hight = 170 #hauteur totale de la bouteille
angle_pour = 149 #angle de versage
delta_high_pour = 100
speed_of_gripping = 150


r=Robot('/dev/ttyACM0')
time.sleep(3)
r.set_joint_speed(20)
r.reset_pos()


#point : [x,y,z, ori.pince, vis.pince]
r.go_to_point([x_pos-bottle_diameter,y_pos-bottle_diameter,z_pos,90,0]) #s'approcher de la bouteille
r.go_to_point([x_pos,y_pos,z_pos,90,0]) #s'engager autour de la bouteille
r.set_joint_speed(speed_of_gripping)
r.close_gripper(pressure_force)
r.set_joint_speed(20)
r.go_to_point([x_pos,y_pos,z_final_pos,90,0]) #monter
r.go_to_point([x_final_pos,y_final_pos,z_final_pos,90,0]) #se déplacer vers le verre
r.go_to_point([x_final_pos,y_final_pos,z_final_pos,90,70]) #verser
#r.set_joint_speed(5)
r.go_to_point([x_final_pos,y_final_pos,z_final_pos,90,angle_pour-40]) #verser lentement
time.sleep(6)
r.go_to_point([x_final_pos+5,y_final_pos,z_final_pos+delta_high_pour,90,angle_pour-20]) #verser plus haut
time.sleep(3)
r.set_joint_speed(40)
r.go_to_point([x_final_pos,y_final_pos,z_final_pos+delta_high_pour,90,70]) #redresser
r.set_joint_speed(20)
r.go_to_point([x_pos,y_pos,z_final_pos+delta_high_pour,90,0]) #redresser et placer la bouteille en haut de son spot
r.go_to_point([x_pos,y_pos,z_pos,90,0]) #déposer la bouteille
r.set_joint_speed(speed_of_gripping)
r.open_gripper()
r.set_joint_speed(20)
time.sleep(1)
r.go_to_point([x_pos-bottle_diameter,y_pos-bottle_diameter,z_pos,90,0]) #s'éloigner de la bouteille
r.got_to_foetus_pos()
