import time
import sys
import math
sys.path.append('../galatae-api/')
from robot import Robot

def place_bottle_top_above_point(x,y,z,angle_rad,R,r):
    y=y+R*math.sin(angle_rad)
    z=z-R*math.cos(angle_rad)
    point=[x,y,z,90,angle_rad*180/math.pi]
    #print(point)
    r.go_to_point(point)

def pour(x_glass,y_glass,z_glass,r,speed):
  N=5
  min_angle=math.pi/4
  max_angle=3*math.pi/4
  R=150
  #pour_duration=10
  
  place_bottle_top_above_point(x_glass,y_glass,z_glass,min_angle,R,r)
  r.set_joint_speed(5)
  for i in range(N):
    angle_rad=min_angle+i*(max_angle-min_angle)/N
    place_bottle_top_above_point(x_glass,y_glass,z_glass,angle_rad,R,r)

  r.set_joint_speed(speed)

def main():
  r=Robot('/dev/ttyACM0')
  speed=25
  r.set_joint_speed(speed)
  r.reset_pos()
  print("start calibration")
  r.calibrate_gripper()
  print("cal ok")

  bottle_point=[200,0]
  glass_point=[350,0]
  h=200

  r.go_to_point(bottle_point+[0,90,0])
  r.close_gripper()
  #time.sleep(30)
  r.go_to_point(bottle_point+[h,90,0])
  r.go_to_point([glass_point[0],glass_point[1]+50,h,90,0])
  r.set_joint_speed(5)
  r.go_to_point([glass_point[0],glass_point[1]+100,h,90,45])
  r.go_to_point([glass_point[0],glass_point[1]+130,h,90,90])
  r.go_to_point([glass_point[0],glass_point[1]+100,h,90,135])
  r.set_joint_speed(speed)

  #pour(glass_point[0],glass_point[1],h,r,speed)
  
  r.go_to_point(bottle_point+[h,90,0])
  r.go_to_point(bottle_point+[0,90,0])
  
  r.open_gripper()
  
  #time.sleep(3)
  r.go_to_foetus_pos()

def test():
  r=Robot('/dev/ttyACM0')
  pour(350,0,150,r)

if __name__ == "__main__":
  main()
  #test()