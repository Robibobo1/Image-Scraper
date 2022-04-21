import shutil
import os

volumeList = [1,8,18,27]#[1,8,18,27,36,45,54,63,72,81,90,100,109,119,129,138,148,158,168,178,189,201,213,225,236,247,259,268,277,286,296,307,319,329,351]
destinationUrl = "Images"

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