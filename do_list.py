from os import listdir

RACINE = "."
RESSOURCES = ["cuivre", "fer"]
RESSOURCES_LEN = len(RESSOURCES)
IMAGE_OFFSET = 5
PORTE_OFFSET = 50

def check_elements():
    result = list()

    for elem in RESSOURCES:
        for file in listdir(RACINE+"/img/"+elem):
            if file.startswith(elem):
                result.append(RACINE + "/img/" + elem + "/" + file)
    return result