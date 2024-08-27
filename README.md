# IPdata

IPdata es una herramienta creada para extraer información sobre una dirección IP. Este código funciona con IPv4 e IPv6. El código se basa en la librería Scapy y la API de ipinfo.io.

## Características

- **Ping a IPv4 e IPv6**: Envía paquetes ICMP a direcciones IPv4 e IPv6 para validar su accesibilidad.
- **Información de IP**: Utiliza la API de ipinfo.io para obtener detalles sobre la dirección IP, como el nombre de host, ciudad, región, país, proveedor de servicios de Internet, código postal y zona horaria.

## Requisitos

- Python 3.x
- Librería Scapy
- Librería Requests

## Instalación

1. Clona el repositorio:
   git clone https://github.com/grimoriodelhacker/IPdata.git
   cd IPdata
   python IPdata.py
