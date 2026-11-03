from pathlib import Path
# import os 
import shutil

def craete_folder():
    try:
        name = input("Please tell your folder name:- ")
        p = Path(name)
        p.mkdir()
        print('folder create successfully')
    except Exception as err:
        print(f"Sorry an error occured as {err}")

def read_file_folder():
    p = Path('')
    items = list(p.rglob('*')) 
    for i,v in enumerate(items):
        print(f"{i+1} : {v}")

def update_folder():
   try:
      read_file_folder()
      old_name = input("Please tell which folder you want to upadte:- ")
      p = Path(old_name)
      if p.exists() and p.is_dir():
          new_name = input("please tell your new folder name:- ")
          new_p = Path(new_name)
          p.rename(new_p)
          print("your folder name is updated succesfully")
      else:
          print("sorry no such folder exist")
   except Exception as err:
       print(f"An error occurade as {err}")

def delete_folder():
    try:
   
        read_file_folder()
        name = (input("Plese tell which file you want to delate:- "))
        p = Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print("your Folder delete properly")
        else:
            print("No such a folder exist")
    except Exception as err:
        print(f"An erro occurade as {err}")   


def create_file():
    try:
        read_file_folder()
        name =(input("Tell what you want to give name to your file:- ")) 
        p = Path(name)
        if not p.exists():
            with open(name,'w') as fs:
                data = input("Write in file")
                fs.write(data)
            print("file create succefully")
        else:
            print("File already exist")
    except Exception as err:
        print(f"exception occurade an {err}")

def read_file():
    try:
        read_file_folder()
        name = input("Enter name of file yoy want to read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(name,'r') as fs:
                content = fs.read()
                print("your file content:- ")
                print(content)
        else:
            print("Sorry no such file exist")

    except Exception as err:
        print(f"An exception occurade as {err}")

def update_file():
    try:
        read_file_folder()
        name = input("Please tell your life name:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Optaion ")
            print("1. for rename the file")
            print("2. for appending something in the file")
            print("3. for overwriting the file content")
            choice = int(input("please choise your option what you want to do:  "))

            if choice == 1:
                new_name = input("tell your name with extension:- ")
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("your file name is changed successfully")
                else:
                    print("this file name exist alrady please change your Name")\

            if choice == 2:
                with open(name,'a') as fs:
                    data = input("please enter what you want to append in file: ")
                    fs.write(''+data)
                print("Data changed succefully")

            if choice == 3:
                with open(name,'w') as fs:
                    data = input("what you want to overwrite : ")
                    fs.write(data)
                print("Data changed succesfully")

    except Exception as err:
        print(f"exception accurade as {err}")


def delete_file():
    try: 
        read_file_folder()
        name = input("Please tell file name with extension: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("file deleted suceesfully")

        else:
            print("sorry no file exist")

    except Exception as err:
        print("an error oc")
    

while True:
    print("Option:- ")
    print("1.Create a folder")
    print('2.Read file and folders')
    print('3.Upadte the folders')
    print('4.Delete the folders')
    print('5.craete the file')
    print('6.read the file')
    print('7.update the file')
    print("8.delete the file")
    print("0.exist the program")


    chose = int(int(input("Please Chose youe option")))

    if chose == 1:
       craete_folder()

    if chose == 2:
        read_file_folder()

    if chose == 3:
        update_folder()

    if chose == 4:
       delete_folder()

    if chose == 5:
        create_file()

    if chose == 6:
        read_file()

    if chose == 7:
       update_file()

    if chose == 8:
        delete_file() 