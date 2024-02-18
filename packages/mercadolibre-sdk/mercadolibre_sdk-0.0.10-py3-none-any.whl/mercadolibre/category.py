
def action_request(self, path: str, action: str, id: str, limit: int = 50, offset: int = 0,
                   params: dict = None) -> list | dict:
    path = f'{path}/{id}/{action}'
    params = self._set_pagination(limit, offset, params)
    return self.make_request(method='GET', path=path, params=params)