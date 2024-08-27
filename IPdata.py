from scapy.all import sr1,IP, ICMP, IPv6, ICMPv6EchoRequest
import requests

def ping(ip_address):
    try:
        paquete = IP(dst=ip_address) / ICMP()
        respuesta = sr1(paquete, timeout=6, verbose=False)
        if respuesta is None:
            print(f"ocurrio un error al validar la ip {ip_address}")
        else:
            print(f"se envio un paquete ICMP  {ip_address}:{respuesta.src}")
    except Exception as e:
        pass
    try:
        paquete = IPv6(dst=ip_address) / ICMPv6EchoRequest()
        respuesta = sr1(paquete, timeout=6, verbose=False)
        if respuesta is None:
            print(f"ocurrio un error al validar la ip {ip_address}")
        else:
            print(f"se envio un paquete ICMP  {ip_address}")
    except Exception as e:
        pass
    
def ipinfo(ip_address):
    try:
        respuesta = requests.get(f"http://ipinfo.io/{ip_address}/json")
        datos = respuesta.json()
        return datos
    except Exception as e:
        print(f"Error al obtener información de la IP {ip_address}")

def main():
    ipuser= input("ingrese IP ")
    ping(ipuser)
    ipinfo(ipuser)
    ip_info = ipinfo(ipuser)
    if ip_info:
        print(f"Información de la IP {ipuser}:")
        print(f"IP: {ip_info.get('ip', 'N/A')}")
        print(f"Nombre de host: {ip_info.get('hostname', 'N/A')}")
        print(f"Ciudad: {ip_info.get('city', 'N/A')}")
        print(f"Región: {ip_info.get('region', 'N/A')}")
        print(f"País: {ip_info.get('country', 'N/A')}")
        print(f"Loc: {ip_info.get('loc', 'N/A')}")
        print(f"Proveedor de servicios de Internet: {ip_info.get('org', 'N/A')}")
        print(f"Código postal: {ip_info.get('postal', 'N/A')}")
        print(f"Zona horaria: {ip_info.get('timezone', 'N/A')}")
    else:
        print("No se pudo obtener información de la IP.")

if __name__ == "__main__":
    main()
