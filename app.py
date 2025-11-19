from flask import Flask, render_template, jsonify, send_from_directory
from ppadb.client import Client as AdbClient
import os
import time

app = Flask(__name__)

FIRE_TVS = [
    "192.168.15.152",
]
FIRE_TV_PORT = 5555
URL_SISTEMA = "https://irb.klingo.app/#/painel/NZTMLK"

# Pasta onde as imagens temporárias são salvas
SCREEN_DIR = "screenshots"
os.makedirs(SCREEN_DIR, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/abrir")
def abrir_site():
    resultados = []
    client = AdbClient(host="127.0.0.1", port=5037)

    for ip in FIRE_TVS:
        try:
            print(f"\n Conectando ao Fire TV {ip}...")
            device = client.device(f"{ip}:{FIRE_TV_PORT}")

            if not device:
                os.system(f"adb connect {ip}:{FIRE_TV_PORT}")
                time.sleep(2)
                device = client.device(f"{ip}:{FIRE_TV_PORT}")

            if device:
                device.shell(f'am start -a android.intent.action.VIEW -d "{URL_SISTEMA}"')
                resultados.append({"ip": ip, "status": "Site aberto com sucesso!"})
            else:
                resultados.append({"ip": ip, "status": "Falha ao conectar"})
        except Exception as e:
            resultados.append({"ip": ip, "status": f"Erro: {str(e)}"})

    return jsonify(resultados)



@app.route("/tv1")
def tv1_screen():
    return send_from_directory(os.path.join("screenshots", "tv1"), "screenshot.png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
