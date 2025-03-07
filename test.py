from scipy.spatial.transform import Rotation as R
import numpy as np
import matplotlib.pyplot as plt
import math
def add_vector_to_plot(ax,v):
  ax.plot([0,v[0]],[0,v[1]],[0,v[2]])
  ax.plot([0,v[0]],[0,v[1]],[0,0],'--k')
  ax.plot([v[0],v[0]],[v[1],v[1]],[0,v[2]],'--k')

def plot(ax):
  max_value=2
  ax.set_proj_type('ortho')
  ax.view_init(elev=20, azim=10, roll=0)
  ax.legend()
  ax.set_xlim(0, max_value)
  ax.set_ylim(0, max_value)
  ax.set_zlim(0, max_value)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  plt.show()
 

def sum_vectors(v1,v2):
  s=[]
  for i in range(len(v1)):
    s.append(v1[i]+v2[i])
  return s

def get_tool_abs_coord(robot_arm_coord,tool_rel_coord): #[x,y,z,pitch,roll]
  angle0=math.atan(robot_arm_coord[1]/robot_arm_coord[0])

  r=R.from_euler('zyz',[robot_arm_coord[4],robot_arm_coord[3],angle0])

  rotated_tool_rel_coord=r.apply(tool_rel_coord)

  tool_abs_coord=sum_vectors(robot_arm_coord[:3],rotated_tool_rel_coord)
  return tool_abs_coord

def get_robot_pos_from_tool_pos(tool_pos,tool_def):
  robot_pos=tool_pos

  #print([tool_pos[4],tool_pos[3]])
  r=R.from_euler('zy',[tool_pos[4],tool_pos[3]])
  tool_rel_coord=r.apply(tool_def).tolist()
  print("tool_rel_coord",tool_rel_coord)
  tool_pos_cyl_coord_R=math.sqrt(tool_pos[0]**2+tool_pos[1]**2)
  print("tool_pos_cyl_coord_R",tool_pos_cyl_coord_R)
  
  if(tool_pos_cyl_coord_R==0):
    robot_pos[0]=-tool_rel_coord[0]
    robot_pos[1]=-tool_rel_coord[1]
  else:  
    angle_between_tool_pos_and_robot_pos=math.asin(tool_rel_coord[1]/tool_pos_cyl_coord_R)
    print("angle_between_tool_pos_and_robot_pos",angle_between_tool_pos_and_robot_pos)

    tool_pos_cyl_coord_theta=90
    if(tool_pos[0]!=0):
      tool_pos_cyl_coord_theta=math.atan(tool_pos[1]/tool_pos[0])
    print("tool_pos_cyl_coord_theta",tool_pos_cyl_coord_theta)
    
    robot_pos_cyl_coord_theta=tool_pos_cyl_coord_theta-angle_between_tool_pos_and_robot_pos
    print("robot_pos_cyl_coord_theta",robot_pos_cyl_coord_theta)
    
    robot_pos_cyl_coord_R=math.sqrt(tool_pos_cyl_coord_R**2-tool_rel_coord[1]**2)-tool_rel_coord[0]
    print("robot_pos_cyl_coord_R",robot_pos_cyl_coord_R)
    
    robot_pos[0]=robot_pos_cyl_coord_R*math.cos(robot_pos_cyl_coord_theta)
    robot_pos[1]=robot_pos_cyl_coord_R*math.sin(robot_pos_cyl_coord_theta)
  
  
  
  robot_pos[2]=tool_pos[2]-tool_rel_coord[2]

  return robot_pos


def test():
  
  ax = plt.figure().add_subplot(projection='3d')
  #r=R.from_euler('xyz',[np.pi/2,np.pi/2,np.pi/2])
  r=R.from_euler('zyz',[np.pi/8,np.pi/8,np.pi])

  v1=[1,0,0]

  v2=r.apply(v1)
  
  add_vector_to_plot(ax,v1)
  
  add_vector_to_plot(ax,v2)

  #plot(ax)

  
def main():
  tool_def=[1,0,0]
  print("tool_def",tool_def)
  tool_pos=[0,1,0,0,0]
  print("tool_pos",tool_pos)


  robot_pos=get_robot_pos_from_tool_pos(tool_pos,tool_def)
  print("robot_pos",robot_pos)
  #r=R.from_euler('zy',[0,0])
  #print(r.apply([1,0,0]).tolist())


if __name__ == "__main__":
  main()
  #test()