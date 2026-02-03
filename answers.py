
def Word_test(file_name, new_file_name, Search, exchange):
    with open(file_name, "r") as file, open(new_file_name, "w") as new:
        for line in file:
            words = line.split()
            updated_words = [] 
            
            for word in words:
                if word == Search:
                    updated_words.append(exchange)
                else:
                    updated_words.append(word)
            
          
            final_line = " ".join(updated_words) + "\n"
            new.write(final_line)


Word_test("data.txt", "data_updated.txt", "kodcod", "8200")