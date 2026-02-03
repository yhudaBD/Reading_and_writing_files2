def num_line(file_name_source):
      counter = 0
      with open(file_name_source , "r") as file :
          
         for line in file:
           counter += 1
         return counter
test = num_line("data.txt" )
print(test)