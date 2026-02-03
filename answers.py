def new_file(file_name_source , target_file):
      with open(file_name_source , "r") as file , open(target_file , "w") as target :
          
         for line in file:
          target.write(line)

new_file("data.txt" , "test1.txt")