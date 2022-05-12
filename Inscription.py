import socket
import json
import IA

#On ouvre le fichier"IA.json" contenant les DONNEES DU JOUEUR.(NB: Communication avec le serveur en JSON)
with open("IA.json") as file:
        joueur= file.read()


#FCT PERMETTANT LA CONNEXION AVEC LE SERVEUR
def serveur():
    s= socket.socket()
    Adresse_client = ("0.0.0.0",json.loads(joueur)["port"])
    s.bind(Adresse_client)
    s.listen()

    while True:
        serveur, addresse = s.accept()
        #Réponse du serveur qu'on reçoie en JSON (JSON-->dico: json.loads)
        requete_serveur= json.loads(serveur.recv(2048).decode())

        #2 types de requete_serveur:
        #requete_serveur={"request": "ping"}
        #requete_serveur= {"request": "play","lives": 3,"errors":[] ,"state": []} 				
        #-->state={"players": ["LUR", "OUSS"],"current": 0,"board": [[28, 35],[27, 36]]}         

        if requete_serveur["request"] == "ping": 
            #Réponse du client qu'on envoie en JSON (dico-->JSON: json.dumps)
            reponse = {"response": "pong"}
            serveur.send(json.dumps(reponse).encode())
        
        if requete_serveur["request"]== "play":                    
            reponse = IA.ia1(requete_serveur["state"])
            serveur.send(json.dumps(reponse).encode()) 

        serveur.close()                                        
    

#CLIENT
#Connection + Envoie de données_joueur à envoyer au Serveur 
r= socket.socket()
#"localhost" à changer par l'IP de l'appareil du lanceur de partie à la compétition
adresse_serveur = ("localhost",3000) 
try:
    r.connect((adresse_serveur))
    r.send(joueur.encode())
except OSError:
    print ("Serveur introuvable , connexion impossible .")


#Réponse du serveur qu'on reçoit en JSON (JSON-->dico: json.loads)
reponse_serveur_json= r.recv(2048).decode()
reponse= json.loads(reponse_serveur_json)
#2 types de reponse:
#reponse={"response": "ok"}
#reponse={"response": "error","error": "error message"}

try:
    if reponse== {"response": "ok"}:
        r.close()
        serveur()      

    if reponse=={"response": "error","error": "error message"}:
        r.close()

except:
    r.close()