import os

def start_vpn():
    # OpenVPN bağlantısını başlatır
    config_path = "/backend/vpn/us-free-1.protonvpn.udp.ovpn"
    os.system(f"sudo openvpn --config {config_path}")

def stop_vpn():
    os.system("sudo killall openvpn")

