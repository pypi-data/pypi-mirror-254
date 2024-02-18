from .api import MercadoLibreAPI


class User:
    @classmethod
    def retrieve(cls, id: str) -> dict:
        api = MercadoLibreAPI()
        return api.retrieve_request(path=f'/users', id=id)
