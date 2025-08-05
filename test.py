import sys
sys.path.append('../galatae-api/')
from robot import Robot

def main():
  r=Robot('/dev/ttyACM0',True)
  r.set_joint_speed(10)

  r.probe([300,0,300,90,0,0])
  print(r.get_tool_pose())
  print(r.get_angles())
  #r.linear_move_to_point([0,300,300,90,0,0])

if __name__ == "__main__":
  main()