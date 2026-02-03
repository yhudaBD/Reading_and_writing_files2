def new_file(file_name , text):
      with open(file_name , "w") as file:
         writer =  file.write(text)
         
new_file("test1.txt" , "23523" ) 