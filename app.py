from flask import Flask, render_template, jsonify, send_from_directory
from ppadb.client import Client as AdbClient
import os
import time

app = Flask(__name__)

TVS = {
    "tv1": "192.168.15.145",
    "tv2": "192.168.15.128",
    "tv3": "192.168.15.138",
    "tv4": "192.168.15.131",
    "tv5": "192.168.15.132",
    "tv6": "192.168.15.130",
    "tv7": "192.168.15.129"
}

FIRE_TV_PORT = 5555
URL_SISTEMA = "https://irb.klingo.app/#/painel/NZTMLK"


@app.route("/")
def index():
    return render_template("index.html", tvs=list(TVS.keys()))


@app.route("/abrir")
def abrir_site():
    resultados = []
    client = AdbClient(host="127.0.0.1", port=5037)

    for nome, ip in TVS.items():
        try:
            device = client.device(f"{ip}:{FIRE_TV_PORT}")

            if not device:
                os.system(f"adb connect {ip}:{FIRE_TV_PORT}")
                time.sleep(2)
                device = client.device(f"{ip}:{FIRE_TV_PORT}")

            if device:
                device.shell(f'am start -a android.intent.action.VIEW -d "{URL_SISTEMA}"')
                resultados.append({"tv": nome, "status": "OK"})
            else:
                resultados.append({"tv": nome, "status": "Falha"})

        except Exception as e:
            resultados.append({"tv": nome, "status": f"Erro: {str(e)}"})

    return jsonify(resultados)


@app.route("/<tv>")
def screen(tv):
    pasta = os.path.join("screenshots", tv)
    arquivo = "screenshot.png"

    return send_from_directory(pasta, arquivo)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
