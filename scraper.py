import requests
from bs4 import BeautifulSoup
import csv
import sys

categories = [
    "books_1",
    "travel_2",
    "mystery_3",
    "historical-fiction_4",
    "sequential-art_5",
    "classics_6",
    "philosophy_7",
    "romance_8",
    "womens-fiction_9",
    "fiction_10",
    "childrens_11",
    "religion_12",
    "nonfiction_13",
    "music_14",
    "default_15",
    "science-fiction_16",
    "sports-and-games_17",
    "add-a-comment_18",
    "fantasy_19",
    "new-adult_20",
    "young-adult_21",
    "science_22",
    "poetry_23",
    "paranormal_24",
    "art_25",
    "psychology_26",
    "autobiography_27",
    "parenting_28",
    "adult-fiction_29",
    "humor_30",
    "horror_31",
    "history_32",
    "food-and-drink_33",
    "christian-fiction_34",
    "business_35",
    "biography_36",
    "thriller_37",
    "contemporary_38",
    "spirituality_39",
    "academic_40",
    "self-help_41",
    "historical_42",
    "christian_43",
    "suspense_44",
    "short-stories_45",
    "novels_46",
    "health_47",
    "politics_48",
    "cultural_49",
    "erotica_50",
    "crime_51"
]

print("Categories available in the store:")
for category in categories:
    print(f"- {category}")

user_choice = input("\nEnter your choice: ")

if user_choice not in categories:
    print("Invalid category selected.")
    sys.exit(1)

def main() -> None:
    page_number = 1

    while True:
        if user_choice == "books_1":
            url = f"https://books.toscrape.com/catalogue/category/{user_choice}/page-{page_number}.html"
        else:
            url = f"https://books.toscrape.com/catalogue/category/books/{user_choice}/page-{page_number}.html"

        print(f"Scraping page {page_number}...")
        site = requests.get(url)

        if site.status_code == 404:
            print("Reached the last page. Scraping finished!")
            break
        page_number += 1

main()
