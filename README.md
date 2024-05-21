# DosHCP
Un programme python de DHCP flooding

# Prévention
Ce script est conçu à des fins éducatives et pour tester la sécurité des réseaux avec l'autorisation explicite des propriétaires du réseau. L'exécution de ce script sur des réseaux non autorisés est illégale et peut causer des perturbations significatives dans les opérations réseau. Utilisez ce script de manière responsable et éthique.

# Prérequis
Installer Scapy :
    
    pip3 install scapy

# Installation

    git clone https://github.com/franckhtr/DosHCP.git

# Modification à faire
Ouvrez le script et modifiez la ligne 54 : sendp(packet, iface="Wi-Fi") en remplaçant "Wi-Fi" par le nom de l'interface réseau que vous souhaitez modifier. 

# Execution

    python3 doshcp.py
