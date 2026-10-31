import csv

import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"  


def scrape_books(url):
    try:
        response = requests.get(
            url,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0 (compatible; LearningScraper/1.0)"}
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        books = []

        for item in soup.select("article.product_pod"):
            title = item.select_one("h3 a")
            price = item.select_one(".price_color")

            if title and price:
                books.append({
                    "title": title.get("title", title.get_text(strip=True)),
                    "price": price.get_text(strip=True),
                })

        if not books:
            print("No books found. Check the website URL and page selectors.")
            return

        with open("books.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["title", "price"])
            writer.writeheader()
            writer.writerows(books)

        print(f"Saved {len(books)} books to books.csv")

    except requests.exceptions.Timeout:
        print("The website took too long to respond.")
    except requests.exceptions.HTTPError as error:
        print(f"The website returned an HTTP error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Could not connect to the website: {error}")
    except OSError as error:
        print(f"Could not save the CSV file: {error}")


if __name__ == "__main__":
    scrape_books(URL)