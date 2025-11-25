import os
import time
from ppadb.client import Client as AdbClient

# IP da TV1
TV1_IP = "192.168.15.145"
PORT = 5555

# Caminho onde o screenshot será salvo
PASTA = "screenshots/tv1"
ARQUIVO = os.path.join(PASTA, "screenshot.png")

# Criar pasta (caso não exista)
os.makedirs(PASTA, exist_ok=True)

# Conexão com o servidor ADB
client = AdbClient(host="127.0.0.1", port=5037)

while True:
    try:
        device = client.device(f"{TV1_IP}:{PORT}")

        if device is None:
            print("[INFO] Tentando conectar à TV1...")
            os.system(f"adb connect {TV1_IP}:{PORT}")
            time.sleep(1)
            device = client.device(f"{TV1_IP}:{PORT}")

        # Se conectou, captura a tela
        if device:
            raw = device.screencap()
            with open(ARQUIVO, "wb") as f:
                f.write(raw)
            print(f"[OK] Screenshot da TV1 salvo em {ARQUIVO}")

        else:
            print("[ERRO] Não foi possível conectar à TV1")

    except Exception as e:
        print(f"[ERRO] TV1: {str(e)}")

    time.sleep(1)
