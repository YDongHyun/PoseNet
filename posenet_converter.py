edited_lines = []
folder_name="image/"
with open("images.txt",'r') as f:
    lines=f.readlines()
with open("image.txt", 'w') as f:
    for i, line in enumerate(lines):
        print(i)
        if i>2 and i%2==0:
            list_file = line.split()
            del list_file[0],list_file[7]
            new_line=[folder_name+list_file[7],list_file[0],list_file[1],list_file[2],
                      list_file[3],list_file[6],list_file[5],list_file[4]]
            new_line = ' '.join(new_line)
            print(new_line)
            f.write(new_line+'\n')
