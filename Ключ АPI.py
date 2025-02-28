import requests
response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos")
endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "DEMO_KEY"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get(endpoint, params=query_params)
photos = response.json()["photos"]
print(f"Найдено {len(photos)} фотографий.")
print(photos[0]["img_src"])