'''
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: Axel CAHOREAU(axel.cahoreau.pro@gmail.com) 
Programme.py(Ɔ) 2022
Description : Saisissez la description puis « Tab »
Créé le :  vendredi 11 mars 2022, 9:10:35 
Dernière modification : vendredi 11 mars 2022, 11:07:59
'''

from PyQt6.QtWidgets import QApplication, QWidget
from Ui_IHM import *
from PortSerie import Connecte

class Gestion_fil (QWidget, Ui_Form):
    def __init__(self,parent=None):
        super ().__init__ (parent)
        self.setupUi (self) 
        # Cette procédure est à compléter avec l’initialisation de votre fenêtre.

    # Insérez ici vos récepteurs (slot)
    
    def machin():
        pass
    

app = QApplication ([])
window = Gestion_fil ()
window.show ()
app.exec ()
