import shutil
import os

volumeList = [1,11,13,18,25,35,38,46,56,61,65,76,90,108,111,123,132,140,150,167,178,180]
destinationUrl = "Z:\\Manga\\Solo Leveling\\Chapters"

def VolumeCreator(volumeList,destinationUrl):
    for volumeNbr in range(1,len(volumeList)):
        try: 
            os.makedirs(destinationUrl + "/Volume" + f"{volumeNbr:02}")
        except FileExistsError :
            print("Le dossier Volume" + f"{volumeNbr:02}" + " a déjà été créé")
        for chapterNbr in range(volumeList[volumeNbr-1] , volumeList[volumeNbr]):
            baseChapterPath = destinationUrl + "/CH" + f"{chapterNbr:03}"
            newPath = destinationUrl + "/Volume" + f"{volumeNbr:02}" + "/CH" + f"{chapterNbr:03}"
            try:
                shutil.move(baseChapterPath,newPath)
                print("Fichier " + baseChapterPath + " à été déplacé avec succès !")
            except FileNotFoundError:
                print("CH" + f"{chapterNbr:03}" + " déjà déplacé ou est manquant")
            except:
                print(":(")



def EmptyVolume(volumeList,destinationUrl):
    for volumeNbr in range(1,len(volumeList)):
        try:
            source_dir = destinationUrl + "/Volume" + f"{volumeNbr:02}"
            target_dir = destinationUrl
            file_names = os.listdir(source_dir)
            for file_name in file_names:
                shutil.move(os.path.join(source_dir, file_name), target_dir)
        except:
                print(":(")
