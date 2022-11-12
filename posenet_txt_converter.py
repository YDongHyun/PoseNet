# colmap image.txt file to Posenet dataset txt file converter

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
            new_line=[folder_name+list_file[7],list_file[6],list_file[5],list_file[4],
                      list_file[0],list_file[1],list_file[2],list_file[3]]
            new_line = ' '.join(new_line)
            print(new_line)
            f.write(new_line+'\n')
