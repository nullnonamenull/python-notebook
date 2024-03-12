import requests

from models import Brewery


def fetch_breweries(city: str = None, country: str = None) -> list:
    url = "https://api.openbrewerydb.org/breweries"
    params = {"page": 1, "per_page": 20}

    if city:
        params["by_city"] = city
    if country:
        params["by_country"] = country

    response = requests.get(url, params=params)
    breweries_data = response.json()

    breweries = []
    for brewery_data in breweries_data:
        filtered_data = {
            key: brewery_data[key] for key in brewery_data if key in {
                'id', 'name', 'brewery_type', 'street', 'city', 'state',
                'postal_code', 'country', 'longitude', 'latitude',
                'website_url', 'phone'
            }
        }

        if ('longitude' in filtered_data and
                filtered_data['longitude'] is not None):
            filtered_data['longitude'] = float(filtered_data['longitude'])
        if ('latitude' in filtered_data and
                filtered_data['latitude'] is not None):
            filtered_data['latitude'] = float(filtered_data['latitude'])

        brewery = Brewery(**filtered_data)
        breweries.append(brewery)

    return breweries
