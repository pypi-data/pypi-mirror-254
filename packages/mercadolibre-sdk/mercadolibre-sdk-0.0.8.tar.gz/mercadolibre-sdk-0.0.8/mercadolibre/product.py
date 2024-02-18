from .api import MercadoLibreAPI


class Product:
    @classmethod
    def retrieve(cls, id: str) -> dict:
        api = MercadoLibreAPI()
        return api.retrieve_request(path=f'/products', id=id)

    @classmethod
    def items(cls, id: str, limit: int = 50, offset: int = 0) -> list:
        api = MercadoLibreAPI()
        return api.action_request(path=f'/products', action='items', id=id, limit=limit, offset=offset)
