#!/usr/bin/env python3
import os, datetime

def file_or_directory(path):
    for content in os.listdir(path):
        full_name = os.path.join(path, content)
        if os.path.isdir(full_name):
            print("{} is a directory".format(full_name))
        else:
            print("{} is a file".format(full_name)
)            

# file_or_directory("it_env1")

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
    filesize = os.path.getsize(filename)
  return(filesize)

# print(create_python_script("program.py"))


def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(os.path.join(os.getcwd(), directory)) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    pass

  # Return the list of files in the new directory
  return os.listdir(os.getcwd())

# print(new_directory("PythonPrograms", "script.py"))

def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
    relative_parent = os.path.join("..", os.path.relpath(os.getcwd()))

  # Return the absolute path of the parent directory
  # return os.path.abspath(relative_parent)
    return f"'{relative_parent}'"

# print(parent_directory())


def file_date(filename):
  # Create the file in the current directory
  f = open(filename, "w")
  f.close()
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  date = datetime.datetime.fromtimestamp(timestamp).date()
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(date))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd

