import time
import sys
import math
sys.path.append('../galatae-api/')
from robot import Robot

def get_point_in_line_segment(p1,p2,rel_pos):
  p=[]
  for i in range(len(p1)):
    p.append(p1[i]+(p2[i]-p1[i])*rel_pos)
  print(p)
  return p

def dist_between_vectors(p1,p2):
  square_dist=0
  for i in range(len(p1)):
    square_dist+=math.pow(p2[i]-p1[i],2)

  return math.sqrt(square_dist)

def linear_move(p1,p2,r):
  N=math.ceil(dist_between_vectors(p1,p2))
  print(N)
  for i in range(N+1):
    r.go_to_point(get_point_in_line_segment(p1,p2,i/N))

def main():
  r=Robot('/dev/ttyACM0')
  r.set_joint_speed(25)
  r.reset_pos()

  p_up=[300,0,150,180,0]
  p_down=[p_up[0],p_up[1],80,p_up[3],p_up[4]]
  
  r.go_to_point(p_up)
  input()
  linear_move(p_up,p_down,r)
  linear_move(p_down,p_up,r)
  r.go_to_foetus_pos()

def test():
  r=Robot('/dev/ttyACM0')
  linear_move([300,0,0,0,0],[310,0,0,0,0],r)

if __name__ == "__main__":
  main()
  #test()