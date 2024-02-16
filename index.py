import os
import shutil
def file():
    #  checking the user entered file name or not 
       try:
            file_name= input("enter the File name with extenstion:")
            if(file_name == ""):
                print("~ enter the file Name!")
            elif  os.path.exists(file_name):
                print("~ file is exsiting!")
                print("""~ 0.return || 1.continue""")
                num = int(input("Enter the number:"))
                if(num == 0):
                 return
            file_mode()
       except Exception as e:
           print(e)

    #  checking the user entered file mode or not
       try:
            file_Mode = input("enter the file mode:")
            if(file_Mode == ""):
                print("~ enter the fileMode!")
            if(file_Mode == "r"):
                os.path.exists(file_name)
                print("~ file is Not exsiting!")
                print("""~ 0.return || 1.continue for exsiting the file""")
                num = int(input("Enter the number:"))
                if(num== 0):
                    return
            elif(file_Mode == "r+"):
                os.path.exists(file_name)
                print("~ file is Not exsiting!")
                print("""~ 0.return || 1.continue for exsiting the file""")
                num = int(input("Enter the number:"))
                if(num== 0):
                    return
            
       except Exception as e:
            print(e)

       with open(file_name, file_Mode) as f:
        if(file_Mode == "w"):
            write = input("Write the file:")
            f.write(write)
            
        elif(file_Mode == "r"):
            if os.path.exists(file_name):
             print(f.read())
             
        elif(file_Mode == "a"):
             write = input("Append the file:")
             f.write(write)
             
        elif(file_Mode == "w+"):
             f.seek(0)
             print()
             print("default file:",f.read())
             print()
             write = input("Wirte the file:")
             f.write(write)
             f.seek(0)
             print()
             print("wrote the file:",f.read())
             print()
             
        elif(file_Mode == "r+"):
             print()
             print("default file:",f.read())
             print()
             write = input("Write the file:")
             f.write(write)
             f.seek(0)
             print()
             print("wrote the file:",f.read())
             print()
             
        elif(file_Mode == "a+"):
             f.seek(0)
             print()
             print("default file:",f.read())
             print()
             write = input("Append the file:")
             f.write(write)
             f.seek(0)
             print()
             print("append file:",f.read())
             print()

def creating_file(folder_name):
      
      if(os.path.exists(folder_name)):
            print("~ folder is exsiting!")
            print("""~ 0.return || 1.continue""")
            num = int(input("Enter the number:"))
            if(num == 0):
                return
      a = os.mkdir(folder_name)
      print("Succeful folder created!")
    #  checking the user entered file name or not 
      try:
        file_name= input("enter the File name with extenstion:")
        file_path = os.path.join(folder_name, file_name)
        if(file_name == ""):
            print("Enter the file Name!")
        elif os.path.exists(file_name):
            print("~ file is exsiting!")
            print("""~ 0.return || 1.continue""")
            num = int(input("Enter the number:"))
            if(num== 0):
                return
        file_mode()
      except Exception as e:
          print(e)

    #  checking the user entered file mode or not
      try: 
        file_Mode = input("enter the file mode:")
        if(file_Mode == ""):
                print("enter the fileMode!")
        if(file_Mode == "r"):
            os.path.exists(file_name)
            print("~ file is Not exsiting!")
            print("""~ 0.return || 1.continue for exsiting the file""")
            num = int(input("Enter the number:"))
            if(num== 0):
                return
        elif(file_Mode == "r+"):
            os.path.exists(file_name)
            print("~ file is Not exsiting!")
            print("""~ 0.return || 1.continue for exsiting the file""")
            num = int(input("Enter the number:"))
            if(num== 0):
                return
      except Exception as e:
           print(e)

      with open(file_path, file_Mode) as f:
        if(file_Mode == "w"):
            write = input("Write the file:")
            f.write(write)
            
        elif(file_Mode == "r"):
            print(f.read())
            
        elif(file_Mode == "a"):
             write = input("Append the file:")
             f.write(write)
             
        elif(file_Mode == "w+"):
             f.seek(0)
             print()
             print("default file:",f.read())
             print()
             write = input("Wirte the file:")
             f.write(write)
             f.seek(0)
             print()
             print("wrote the file:",f.read())
             print()
             
        elif(file_Mode == "r+"):
             print()
             print("default file:",f.read())
             print()
             write = input("Write the file:")
             f.write(write)
             f.seek(0)
             print()
             print("wrote the file:",f.read())
             print()
             
        elif(file_Mode == "a+"):
             f.seek(0)
             print()
             print("default file:",f.read())
             print()
             write = input("Append the file:")
             f.write(write)
             f.seek(0)
             print()
             print("append file:",f.read())
             print()

# file modes 
def file_mode():
    print("""
        w -> write the file
        r -> read the file
        a -> append the file
        w+ -> reading and writing the file
        r+ -> wrinting and reading the file
        a+ -> appending and reading the file
        """)
    
# list of the file in current directory
def loop_the_files():
    directory = os.getcwd()
    loop_files = os.listdir(directory)
    print("current directory:", os.getcwd())
    i =1 
    for item in loop_files:
        print(f'{i}. {item}')
        i += 1

# deleting the file
def deleting_file():
    print("file deleting || floder deleting")
    print("""
        1.file delete
        2.folder delete
    """)
    choice = int(input("enter the choice: "))
    if (choice == 1):
        file_path = input("enter file path:")
        os.remove(file_path)
        print("**********file deleted.**********")
    else:
        directory_path = input("enter the folder path:")
        shutil.rmtree(directory_path)
        print("**********folder deleted.**********")

# help guide
def Help():
    print("""
        Welcome to simple files mangement system.
        #this is instrutions for use the sytem ->

        1.New folder -> Create a new folder in current directory.
        2.Continue -> If didn't want folder. then continue with file name with extension this command fire.
        3.Current directory -> check the current directory path.
        4.List the file in directory -> check the current directory files.
        5.Deleting the files and folder -> *****CAUTION***** deleting file or folder correctly enter the PATH. if you file or folder delete.
        6.When file creating than file doesn't existe. the file modes "r" and "r+" doesn't working.
        7.When fire the file at file mode "w" and "w+" file existing time, than re-render the file data.
        8.An append is a file data write at the end of a file line.

        #system point ->
        "~" The meaning of this system point system will warning you for wrong commands, invalid commands.
      
        **********Thanks for Reading**********
""")

print("create a folder || continue")
print("""
        1.new folder
        2.continue
        3.current directory
        4.list the file in directory
        5.deleting the files & folder
        6.Help
""")

try:
    user_choice = int(input("enter the number:"))
    if(user_choice  == 1):
        try:
            folder_name= input("enter the floder Name: ")
            if (folder_name == ""):
                print("~ write the folder name!")
            else:
                creating_file(folder_name)
        except Exception as e:
            print("an error occurred:", e)
    elif(user_choice == 2):
        file()
    elif(user_choice == 3):
        print("current directory:", os.getcwd())
    elif(user_choice == 4):
        loop_the_files()
    elif(user_choice == 5):
        deleting_file()
    elif(user_choice == 6):
        Help()
    else:
        print("~ invaild number")
except Exception as e:
    print("~ enter the number!")
    print(e)
