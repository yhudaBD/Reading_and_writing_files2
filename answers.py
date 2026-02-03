def print_file(file_name):
      with open(file_name , "r") as file:
         reading =  file.read()
         return reading
test = print_file("data.txt") 
print(test)   