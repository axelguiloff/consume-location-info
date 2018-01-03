class PoiClient:
    def __init__(self, api_key):
        self._api_key = api_key

    def retrieve_poi(self, location_data):
        import requests
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
        url += 'key=' + self._api_key
        url += '&location='+str(location_data['latitude'])+','
        url += str(location_data['longitude'])
        url += '&rankby=distance'
        url += '&type=natural_feature'
        response = requests.get(url)
        return response.json()

    def list_nearby(self, points_of_interest):
        print("------------------")
        print("Points of Interest")
        print("------------------")
        if len(points_of_interest) == 0:
            print("No suggestions")
            return
        for poi in points_of_interest[0:5]:
            print(poi["name"])