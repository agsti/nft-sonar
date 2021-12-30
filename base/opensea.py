import requests


class Opensea:
    def get_assets(self, collection, page):
        page_size = 50
        url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=%d&limit=%d&collection=%s" % (page*page_size, page_size, collection)
        response = requests.request("GET", url)
        json_response = response.json()
        if "assets" in json_response:
            return json_response['assets']
        else:
            return json_response

    def get_collections(self, page):
        page_size = 250
        url = "https://api.opensea.io/api/v1/collections?offset=%d&limit=%d" % (page*page_size, page_size)
        response = requests.request("GET", url)
        json_response = response.json()
        if "collections" in json_response:
            return json_response['collections']
        else:
            return json_response
