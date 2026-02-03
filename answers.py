
def Word_test(file_name , word):
      counter = 0
      with open(file_name , "r") as file :
        for w in file:
            new_word = w.split()
            for i in new_word:
             if i == word:
              counter += 1
        return counter     
test = Word_test("answers.py" , "counter")

