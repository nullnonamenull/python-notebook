import argparse

from brewery_api import fetch_breweries


def main():
    parser = argparse.ArgumentParser(
        description="Fetch breweries by city and country.")
    parser.add_argument("--city",
                        type=str,
                        help="City to fetch breweries from",
                        default=None)
    parser.add_argument("--country",
                        type=str,
                        help="Country to filter breweries by",
                        default=None)

    args = parser.parse_args()

    breweries = fetch_breweries(city=args.city,
                                country=args.country)
    for brewery in breweries:
        print(brewery)


if __name__ == "__main__":
    main()
