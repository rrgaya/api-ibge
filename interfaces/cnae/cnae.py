import json
import httpx


url = "https://servicodados.ibge.gov.br/api/v2/cnae/classes"


class Cnae:
    def __init__(self, json_ibge=None):
        response = httpx.get(url)
        self.json_ibge = json.loads(response.content.decode("utf-8"))

    def json(self):
        return self.json_ibge

    def count(self):
        return len(self.json_ibge)

    def get_id(self):
        return [self.json_ibge[i]["id"] for i in range(self.count())]

    def get_name(self):
        return [self.json_ibge[i]["nome"] for i in range(self.count())]
