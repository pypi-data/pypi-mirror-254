import os
import sys
from pathlib import Path

src_folder = f'{Path(__file__).parent}'
sys.path.append(src_folder)
os.chdir(src_folder)

import subprocess
import webbrowser
from multiprocessing import Process

from time import sleep

from dotenv import load_dotenv
from flask import Flask, request
import logging

from _authentication import _Authentication

app = Flask(__name__)
app.env = 'production'
app.logger.disabled = True
logging.getLogger('werkzeug').disabled = True

load_dotenv()


class Authorization(_Authentication):

    def __init__(self):
        super().__init__()

    def start(self):
        print('Starting server...')
        server = Process(target=self.run)
        server.start()

        sleep(5)
        print('Server started!')

        webbrowser.open(self._get_auth_url())
        print('Authorizing...')

        sleep(5)

        return server

    def run(self):
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        app.run(port=5000, debug=False)


def start_tunnel():
    redirect_uri = os.getenv('MERCADOLIBRE_REDIRECT_URI')

    if not redirect_uri:
        raise Exception('Missing MERCADOLIBRE_REDIRECT_URI. Set MERCADOLIBRE_REDIRECT_URI in your env variables')

    domain = redirect_uri.replace('http://', '').replace('https://', '')
    command = ['ngrok', 'http', f'--domain={domain}', '5000']

    print('Starting tunnel...')
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        sleep(5)
        print('Tunnel started!')
        return process
    except Exception as e:
        print(f'Error starting tunnel: {e}')
        process.terminate()


@app.route('/')
def callback():
    code = request.args.get('code')
    try:
        Authorization().__exchange_code_for_token(code)

        return """
            <body style="font-family: Arial">
                <img src="https://http2.mlstatic.com/frontend-assets/ml-web-navigation/ui-navigation/6.5.11/mercadolibre/logo__large_plus.png" />
                <h1>Mercado Libre client authorized with success!</h1>
                <h2>You can now close this window.</h2>
                <small>Developed by Mercado Radar - <a href="https://www.mercadoradar.com.br">https://www.mercadoradar.com.br</a><br>
                <br>
                Mercado Libre and its trademarks are the property of MercadoLibre, Inc.<br>
                Mercado Radar is not affiliated, endorsed, or sponsored by MercadoLibre, Inc.<br>
                This client is an independent, unofficial software developed by Mercado Radar.<br>
                All copyrights and trademarks mentioned here are the property of their respective owners.<br>
                </small>
            </body>
        """

    except Exception as e:
        return f'{e}'


def authorize():
    tunnel = start_tunnel()

    authorization = Authorization()
    server = authorization.start()

    tunnel.terminate()
    server.terminate()

    sys.exit()


if __name__ == '__main__':
    authorize()
