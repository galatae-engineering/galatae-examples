import time
from robot_library import Robot

def main():
  r=Robot('/dev/ttyACM0')
  time.sleep(3)
  r.reset_pos()

  r.close_gripper()
  r.open_gripper()
  r.close_gripper(10)

  r.got_to_foetus_pos()

if __name__ == "__main__":
  main()