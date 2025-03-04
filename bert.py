import time
import sys
import math
sys.path.append('../galatae-api/')
from robot import Robot

def get_point_in_line_segment(p1,p2,rel_pos):
  p=[]
  number_of_indexes=min(len(p1),len(p2))

  for i in range(number_of_indexes):
    p.append(p1[i]+(p2[i]-p1[i])*rel_pos)
  print(p)
  return p

def dist_between_vectors(p1,p2):
  square_dist=0
  for i in range(len(p2)):
    print(i)
    square_dist+=math.pow(p2[i]-p1[i],2)

  return math.sqrt(square_dist)

def linear_move(p2,r):
  p1=r.get_position()
  N=math.ceil(dist_between_vectors(p1,p2))
  print(N)
  for i in range(N+1):
    r.go_to_point(get_point_in_line_segment(p1,p2,i/N))

def modify_one_element_in_list(list,index,new_value):
  new_list=list.copy()
  new_list[index]=new_value
  return new_list

def increment_one_element_in_list(list,index,increment):
  return modify_one_element_in_list(list,index,list[index]+increment)

def reach_point_through_safe_height(p,safe_height,r):
  p_above=increment_one_element_in_list(p,2,safe_height)
  
  r.go_to_point(p_above)
  input()
  linear_move(p,r)
  input()
  linear_move(p_above,r)

def main():
  r=Robot('/dev/ttyACM0')
  default_speed=100
  r.set_joint_speed(default_speed)
  r.reset_pos()

  p_clip=[235,0,30,180,0]
  p_above_clips=increment_one_element_in_list(p_clip,2,30)
  bottles_safe_height=230
  p_bottles=[393,3,80,180,0]
  p_above_bottles=modify_one_element_in_list(p_bottles,2,bottles_safe_height)

  time.sleep(5)

  r.go_to_point(p_above_clips)
  #input()
  r.set_joint_speed(10)
  linear_move(p_clip,r)
  time.sleep(3)
  linear_move(p_above_clips,r)
  r.set_joint_speed(default_speed)
  r.go_to_point(modify_one_element_in_list(p_clip,2,bottles_safe_height))
  r.go_to_point(p_above_bottles)
  
  i=1
  #i=input()
  if(i!="n"):
    linear_move(p_bottles,r)
    linear_move(p_above_bottles,r)

  r.go_to_foetus_pos()

def test():
  a=input()
  if(a=="n"):
    print("you dont want ??")

if __name__ == "__main__":
  main()
  #test()