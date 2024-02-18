from .api import MercadoLibreAPI


class Review:
    @classmethod
    def item(cls, id: str) -> dict:
        api = MercadoLibreAPI()
        return api.retrieve_request(path=f'/reviews/item', id=id)
