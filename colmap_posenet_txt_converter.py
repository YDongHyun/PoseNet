# colmap image.txt file to Posenet dataset txt file converter
import numpy as np
global rot_matrix
 
def quaternion_rotation_matrix(Q):
    global rot_matrix
    # Extract the values from Q
    q0 = float(Q[0])
    q1 = float(Q[1])
    q2 = float(Q[2])
    q3 = float(Q[3])
     
    # First row of the rotation matrix
    r00 = 2 * (q0 * q0 + q1 * q1) - 1
    r01 = 2 * (q1 * q2 - q0 * q3)
    r02 = 2 * (q1 * q3 + q0 * q2)
     
    # Second row of the rotation matrix
    r10 = 2 * (q1 * q2 + q0 * q3)
    r11 = 2 * (q0 * q0 + q2 * q2) - 1
    r12 = 2 * (q2 * q3 - q0 * q1)
     
    # Third row of the rotation matrix
    r20 = 2 * (q1 * q3 - q0 * q2)
    r21 = 2 * (q2 * q3 + q0 * q1)
    r22 = 2 * (q0 * q0 + q3 * q3) - 1
     
    # 3x3 rotation matrix
    rot_matrix = np.array([[r00, r01, r02],
                           [r10, r11, r12],
                           [r20, r21, r22]])
    
    return rot_matrix

new_txt_filename = input("write new_txt_filename (write file format) : ")
image_folder_name = input("write saved image_folder_name : ")
edited_lines = []
folder_name=image_folder_name+"/"
with open("images.txt",'r') as f:
    lines=f.readlines()
with open(new_txt_filename, 'w') as f:
    for i, line in enumerate(lines):
        print(i)
        if i>3 and i%2==0:
            list_file = line.split()
            del list_file[0],list_file[7]
            quaternion_rotation_matrix(list_file)
            mat=rot_matrix
            mat_inverse = np.linalg.pinv(mat)
            R = np.transpose(mat_inverse)
            T= [[float(list_file[4])],[float(list_file[5])],[float(list_file[6])]]
            #print(mat)
            #print(mat_inverse)
            positon=np.dot(-1*R,T)
            print(positon)
            new_line=[folder_name+list_file[7],float(positon[0]),float(positon[1]),float(positon[2]),list_file[0],list_file[1],list_file[2],list_file[3]]
            new_line[1]=str(new_line[1])
            new_line[2]=str(new_line[2])
            new_line[3]=str(new_line[3])
            new_line = ' '.join(new_line)
            print(new_line)
            
            f.write(new_line+'\n')
            
