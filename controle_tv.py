from ppadb.client import Client as AdbClient
import os
import time

FIRE_TVS = [
    "192.168.15.152",   
]
FIRE_TV_PORT = 5555
URL_SISTEMA = "https://irb.klingo.app/#/painel/NZTMLK"

client = AdbClient(host="127.0.0.1", port=5037)

for ip in FIRE_TVS:
    print(f"\n Conectando ao Fire TV {ip}...")

    device = client.device(f"{ip}:{FIRE_TV_PORT}")

    if not device:
        print("Não conectado. Tentando parear...")
        os.system(f"adb connect {ip}:{FIRE_TV_PORT}")
        time.sleep(2)  
        device = client.device(f"{ip}:{FIRE_TV_PORT}")

    if device:
        print(f"Conectado ao Fire TV {ip}")
        print("Abrindo o sistema de chamados...")
        device.shell(f'am start -a android.intent.action.VIEW -d "{URL_SISTEMA}"')
        print(f"Site aberto com sucesso na Fire TV {ip}!")
    else:
        print(f"Falha ao conectar à Fire TV {ip}. Verifique a depuração ADB e o IP.")
