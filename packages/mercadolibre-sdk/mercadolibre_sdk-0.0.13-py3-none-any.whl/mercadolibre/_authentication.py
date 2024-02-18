import json
import os
from datetime import datetime, timedelta

import redis
import requests
from dotenv import load_dotenv

load_dotenv()


class _Authentication:
    def __init__(self):
        self.__client_id = os.getenv('MERCADOLIBRE_CLIENT_ID')
        self.__client_secret = os.getenv('MERCADOLIBRE_CLIENT_SECRET')
        self.__redirect_uri = os.getenv('MERCADOLIBRE_REDIRECT_URI')
        self.__redis_manager = _RedisManager()

        if not self.__client_id:
            raise Exception('Missing MERCADOLIBRE_CLIENT_ID. Set MERCADOLIBRE_CLIENT_ID in your env variables')

        if not self.__client_secret:
            raise Exception('Missing MERCADOLIBRE_CLIENT_SECRET. Set MERCADOLIBRE_CLIENT_SECRET in your env variables')

        if not self.__redirect_uri:
            raise Exception('Missing MERCADOLIBRE_REDIRECT_URI. Set MERCADOLIBRE_REDIRECT_URI in your env variables')

    def _get_auth_url(self):
        return f'https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={self.__client_id}&redirect_uri={self.__redirect_uri}'

    def _exchange_code_for_token(self, code):
        token_url = 'https://api.mercadolibre.com/oauth/token'
        payload = {
            'grant_type': 'authorization_code',
            'client_id': self.__client_id,
            'client_secret': self.__client_secret,
            'code': code,
            'redirect_uri': self.__redirect_uri
        }
        response = requests.post(token_url, data=payload)
        auth_data = self.__handle_mercadolibre_response(response)
        self.__save_auth_data(auth_data)

        return auth_data

    def __save_auth_data(self, auth_data):
        try:
            self.__redis_manager.save_auth_data(auth_data)
        except Exception as e:
            print('Redis not configured, saving on text file and env variables')

            auth_data = json.dumps(auth_data)

            with open('auth_data.txt', 'w') as file:
                file.write(auth_data)

            os.environ['MERCADOLIBRE_AUTH_DATA'] = auth_data

    def __refresh_token(self, refresh_token):
        token_url = 'https://api.mercadolibre.com/oauth/token'
        payload = {
            'grant_type': 'refresh_token',
            'client_id': self.__client_id,
            'client_secret': self.__client_secret,
            'refresh_token': refresh_token
        }
        response = requests.post(token_url, data=payload)
        auth_data = self.__handle_mercadolibre_response(response)
        self.__save_auth_data(auth_data)

        return auth_data

    def __handle_mercadolibre_response(self, response):
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data['access_token']
            refresh_token = token_data.get('refresh_token', None)
            expires_in = token_data['expires_in']
            expiration_time = datetime.now() + timedelta(seconds=expires_in)

            auth_data = {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'expiration_time': expiration_time.isoformat()
            }

            return auth_data
        else:
            raise Exception(f'Failed to get token: {response.status_code}, {response.text}')

    def get_access_token(self):
        auth_data = dict()
        try:
            auth_data = self.__redis_manager.get_auth_data()
        except Exception as e:
            try:
                with open('auth_data.txt', 'r') as file:
                    auth_data = file.read()
            except Exception as e:
                auth_data = os.getenv('MERCADOLIBRE_AUTH_DATA')
            finally:
                if auth_data:
                    auth_data = json.loads(auth_data)

        if not auth_data or 'access_token' not in auth_data or 'expiration_time' not in auth_data:
            raise Exception('Access token not found. Please authorize the application first.')

        expiration_time = datetime.fromisoformat(auth_data['expiration_time'])
        if expiration_time <= datetime.now():
            refresh_token = auth_data.get('refresh_token')
            if not refresh_token:
                raise Exception('Refresh token not found. Reauthorize the application.')

            access_token, refresh_token, expiration_time = self.__refresh_token(refresh_token)

            return access_token
        else:
            return auth_data['access_token']


class _RedisManager:
    def __init__(self):
        host = os.getenv('MERCADOLIBRE_REDIS_HOST', 'localhost')
        port = os.getenv('MERCADOLIBRE_REDIS_PORT', '6379')
        self.redis_client = redis.StrictRedis(host=host, port=port, decode_responses=True)

    def save_auth_data(self, auth_data):
        self.redis_client.hset('mercadolibre_auth_data', mapping=auth_data)

    def get_auth_data(self):
        auth_data = self.redis_client.hgetall('mercadolibre_auth_data')
        return auth_data
