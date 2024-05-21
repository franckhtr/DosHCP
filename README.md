# DosHCP 
Un programme python de DHCP flooding

# Prévention 👨🏻‍🏫
Ce script est conçu à des fins éducatives et pour tester la sécurité des réseaux avec l'autorisation explicite des propriétaires du réseau. L'exécution de ce script sur des réseaux non autorisés est illégale et peut causer des perturbations significatives dans les opérations réseau. Utilisez ce script de manière responsable et éthique.

# Comment ça fonctionne 💡
1) Le script génère une addresse MAC aléatoire
2) Grâce aux fonctionnalités de Scapy, le script crée une requête DHCP
3) Une boucle envoi les trames à haute fréquence sur le réseau

# Conséquences ⚠
Le grand nombre de trames DHCP peut provoquer un dénis de service DHCP sur le serveur DHCP du réseau ciblé.
Si les trames passent par des switch, cela peut également provoquer une saturation de la table CAM du commutateur (MACof).
Il est donc INDISPENSABLE de manier cet outil avec précaution et de l'utiliser uniquement dans des environnements clos (réseau de VMs) à des buts de test.


# Prérequis ⏮
Installer Scapy :
    
    pip3 install scapy

# Installation ⚙

    git clone https://github.com/franckhtr/DosHCP.git

# Modification à faire ✏
Ouvrez le script et modifiez la ligne 54 : sendp(packet, iface="Wi-Fi") en remplaçant "Wi-Fi" par le nom de l'interface réseau que vous souhaitez utiliser. 

# Execution 💥

    python3 doshcp.py
