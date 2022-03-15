"""
Auteur : Frank SAURET (frank.sauret.prof@gmail.com)
Deuxième fenêtre.py (Ɔ) 2021
Description : Connexion automatique sur le port de la carte si une seule est branchée. Propose un choix ou une connexion multiple.
Créé le :  10 Août 2020 à 15:17 
Dernière modification : 11 septembre 2021
"""

import serial
import serial.tools.list_ports

def Connecte(nomDeLaCarte, Vitesse):
    """Connexion automatique sur le port de la carte si une seule est branchée. Propose un choix ou une connexion multiple.
    Args:
        nomDeLaCarte (string) : Arduino Uno ou micro:bit
        Vitesse (int) : Vitesse en baud
    Returns:
        Liste d'objet Ports séries sélectionnés correspondant type de carte. Si une seule carte est connectée elle est donc à l'index 0.
    """
    """Testé avec une seule arduino pour l'instant"""
    portCartes=[] # liste des ports connectés à une carte
    cartes_series=[] # Objets de liaisons série des cartes
    # Autre VID PID : voir internet. http://www.linux-usb.org/usb.ids.
    VIDPIDArduinoUNO=["2341:0001","2341:0043","2341:0243","2a03:0043","1a86:7523"]
    VIDPIDMicroBit=["0D28:0204"]

    if nomDeLaCarte=="micro:bit":
        VIDPID=VIDPIDMicroBit
    elif nomDeLaCarte=="Arduino Uno"    :
        VIDPID=VIDPIDArduinoUNO
    else:
        print("Ne marche qu'avec « Arduino Uno » ou « micro:bit »")   

    while len(portCartes)<1:
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            for NumProd in range (0,len(VIDPID)):
                if VIDPID[NumProd] in hwid:
                    portCartes.append(port)
                    break
        if len(portCartes)<1:
            print("Pas de carte ",nomDeLaCarte," branchée !")
            Réponse=input("Branchez une carte, attendez qu'elle s'installe puis tapez sur 'Entrée'. Sinon 'q' puis 'Entrée' pour quitter.")
            if Réponse.upper()=="Q":
                quit()

    if len(portCartes)==1:    
        portAOuvrir=portCartes[0]
        cartes_series.append(serial.Serial(portAOuvrir,Vitesse,timeout=0.01))
        nombreDeCartes=1
    else:
        print("Voici la liste des cartes ",nomDeLaCarte," branchées :"+"\n")
        print(portCartes)
        numCarte=256 #nombre de ports max sous windows
        while numCarte>len(portCartes)-1:
            numCartes=input("Tapez 1 pour utiliser la première, 2 pour la deuxième ... x pour toutes (ne fonctionne que pour la lecture)")
            numCartes=numCartes-1
            if numCartes!='x':
                numCarte=int(numCartes)
                if numCarte>len(portCartes)-1:
                    print("ne dépassez pas :"+str(len(portCartes)-1)+"\n")
                else:
                    portAOuvrir=portCartes[numCarte]
                    cartes_series.append(serial.Serial(portAOuvrir,Vitesse,timeout=0.01))
                    numCarte=0
                nombreDeCartes=1
            else:
                for lePort in portCartes:
                    cartes_series.append(serial.Serial(lePort,Vitesse,timeout=0.01))
                    numCarte=0
                    nombreDeCartes=len(portCartes)
    return cartes_series