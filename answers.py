
def Word_test(file_name , file_wirth):
  with open(file_name , "r") as file , open(file_wirth , "w") as wir:
       for line in file :
         wir.write(line)      
          
          
test = Word_test("answers.py" , "test1.txt")
print(test)
