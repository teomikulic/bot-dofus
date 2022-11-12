from random import randint
import time
import pyautogui as pg
import do_list as dl
import check_ress as cr

PORTES = ["porte_0.png", "porte_1.png", "porte_2.png", "porte_21.png", "porte_212.png", "porte_212b.png", "porte_211.png", "porte_211b.png", "porte_21b.png", "porte_22.png", "porte_221.png", "porte_221b.png", "porte_22b.png", "porte_2b.png", "porte_1b.png", "porte_0b.png"]
PORTES_LENGHTS = len(PORTES)
nb_map = 0

def check_map():
  global nb_map
  print("Demarrage de la map")
  cr.collect_ressources()
    
  img = pg.locateOnScreen("./img/porte/"+ PORTES[nb_map], confidence=0.88)
  print("Ressources collectées \n"+"Recherche de la porte : "+PORTES[nb_map])
  if img != None:
    print("Porte trouvée")
    time.sleep(3)
    pg.click(img[0]+dl.PORTE_OFFSET, img[1]+dl.PORTE_OFFSET)
    time.sleep(randint(4,6))
    nb_map += 1
    if nb_map >= PORTES_LENGHTS:
      nb_map = 0
  else:
      quit()
