
def add_text(file_name, text1, text2):
    with  open(file_name, "a") as new:
         new.write(f"\n{text1}:{text2}")

add_text("data.txt" , "city" , "bs")         