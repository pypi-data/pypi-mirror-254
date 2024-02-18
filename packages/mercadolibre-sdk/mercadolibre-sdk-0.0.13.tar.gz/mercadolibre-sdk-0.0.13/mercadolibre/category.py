from .api import MercadoLibreAPI


class Category:

    @classmethod
    def highlights(cls, site_id, category_id):
        path = f'/highlights/{site_id}/category/{category_id}'
        api = MercadoLibreAPI()
        return api.make_request(method='GET', path=path)
