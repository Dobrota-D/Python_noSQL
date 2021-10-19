"""this function will get the url of the file. If the file exist it will be deleted,
if the file doesn't exist it will print an error message. """

import os
number = input("which file do you want to delete ?")
if os.path.exists("users/"+number+".txt"):
   os.remove("users/"+number+".txt")
else:
  print("The file does not exist")