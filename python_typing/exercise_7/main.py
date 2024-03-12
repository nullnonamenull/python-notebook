from brewery_api import fetch_breweries


def main():
    breweries = fetch_breweries()
    for brewery in breweries:
        print(brewery)


if __name__ == "__main__":
    main()
