from mercadolibre._authentication import _Authentication


class Authentication:

    @classmethod
    def get_access_token(cls):
        return _Authentication().get_access_token()
