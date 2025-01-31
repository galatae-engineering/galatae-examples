import time
import sys

sys.path.append('../galatae-api/')
from robot import Robot

def follow_trajectory(r,points):
  for i in range(len(points)):
    r.go_to_point(points[i])

def lift_point(point):
  new_point=point.copy()
  new_point[2]+=100
  return new_point

def main():
  r=Robot('/dev/ttyACM0')

  r.reset_pos()
  r.calibrate_gripper()
  r.set_joint_speed(10)

  pick=[300,0,200,180]
  place=[0,300,200,180]

  #pick=[200,0,200,180]
  #place=[500,0,200,180]

  points=[lift_point(pick),pick,lift_point(pick),lift_point(place),place,lift_point(place)]
  print(points)

  for i in range(3):
    follow_trajectory(r,points)
  
  print(len(points))
  

  r.go_to_foetus_pos()

if __name__ == "__main__":
  main()
  """
  pick=[300,0,200,180]
  print(pick)
  print(lift_point(pick))
  print(pick)
  """