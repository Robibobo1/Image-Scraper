import os

destinationPath = "Z:\\Manga\\Jujutsu Kaisen\\chapitres"

for chapterNbr in range(1,149):
    old_name = destinationPath + "/CH" + f"{chapterNbr:04}"
    new_name = destinationPath + "/CH" + f"{chapterNbr:03}"
    try:
        os.rename(old_name, new_name)   
        print(old_name + "-> Success")
    except:
        print(old_name + "-> Error")



