from abc import ABC, abstractmethod

import requests


class CSRFSession(requests.Session, ABC):
    def __init__(self):
        self.token = None
        super().__init__()

    @abstractmethod
    def _extract_csrf(self, response) -> str:
        pass

    def request(self, method, url, **kwargs):
        modified_url = self.url_base._replace(path=url)
        return super().request(method, modified_url.geturl(), **kwargs)

    def post(
        self, url, data={}, json=None, send_csrf=True, extract_csrf=True, **kwargs
    ):
        if send_csrf:
            data.update(csrfmiddlewaretoken=self.token)

        resp = super().post(url, data, json, **kwargs)

        if extract_csrf:
            self.token = self._extract_csrf(resp)

        return resp

    def get(self, url, params=None, send_csrf=True, extract_csrf=True, **kwargs):
        resp = super().get(
            url,
            params=params,
            headers={"csrfmiddlewaretoken": self.token} if send_csrf else {},
            **kwargs,
        )

        if extract_csrf:
            self.token = self._extract_csrf(resp)

        return resp
