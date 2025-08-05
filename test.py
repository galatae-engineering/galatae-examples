import sys
sys.path.append('../galatae-api/')
from robot import Robot

def main():
  r=Robot('/dev/ttyACM0',0)
  r.set_joint_speed(10)
  r.linear_move_to_point([200,0,300,90,0,0])
  success=r.linear_probe([500,0,300,90,0,0])
  print(success)
  r.go_to_foetus_pos()

if __name__ == "__main__":
  main()