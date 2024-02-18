from .api import MercadoLibreAPI


class Item:
    @classmethod
    def retrieve(cls, id: str) -> dict:
        api = MercadoLibreAPI()
        return api.retrieve_request(path=f'/items', id=id)
