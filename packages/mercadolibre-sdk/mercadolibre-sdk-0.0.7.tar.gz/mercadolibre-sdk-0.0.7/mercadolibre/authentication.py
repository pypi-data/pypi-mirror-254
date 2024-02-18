from mercadolibre._authentication import _Authentication


class Authentication(_Authentication):

    def __init__(self):
        super().__init__()

    def get_access_token(self):
        return self._get_access_token()
