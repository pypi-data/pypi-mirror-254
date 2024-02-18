from .api import MercadoLibreAPI


class Search:
    @classmethod
    def list(cls,
             site_id: str,
             q: str = None,
             category_id: str = None,
             seller_id: str = None,
             official_store_id: str = None,
             product: str = None,
             sort: str = None,
             limit: int = 50,
             offset: int = 0) -> dict:
        api = MercadoLibreAPI()

        params = dict()

        if q:
            params['q'] = q

        if category_id:
            params['category'] = category_id

        if seller_id:
            params['seller_id'] = seller_id

        if official_store_id:
            params['official_store_id'] = official_store_id
        
        if product:
            params['product'] = product
            
        if sort:
            if sort not in ['relevance', 'price_asc', 'price_desc']:
                raise Exception('sort must be "relevance", "price_asc" or "price_desc"')

            params['sort'] = sort

        return api.list_request(path=f'/sites/{site_id}/search', limit=limit, offset=offset, params=params)
