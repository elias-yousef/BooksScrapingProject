import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import sys

def get_categories() -> dict:
    category_dict = {}
    category_dict["Books"] = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    try:
        site = requests.get("https://books.toscrape.com/catalogue/category/books_1/index.html")
    except Exception as error:
        print(error)

    src = site.content
    soup = BeautifulSoup(src, "lxml")
    main_ul = soup.find('ul', class_='nav nav-list')

    if main_ul:
        inner_ul = main_ul.find('ul')
        if inner_ul:
            category_links = inner_ul.find_all('a')
            for link in category_links:
                name = link.text.strip()
                full_url = urljoin(site.url, link.get('href'))
                category_dict[name] = full_url
    return category_dict


def main() -> None:
    url = ""
    print("Categories available in the store:")
    category = get_categories()

    for name in list(category.keys()):
        print(name)

    user_choice = input("which one to scrap data? :")
    if user_choice in category:
        url = category[user_choice]
    else:
        print("Categories is not available")
        sys.exit(1)
    page_number = 1
    indx = url.find('index')
    books_info = []
    while True:
        if "books_1" in url:
            url = f"https://books.toscrape.com/catalogue/category/books_1/page-{page_number}.html"
        else:
            if page_number == 1:
                pass
            else:
                url = url[:indx] + f"page-{page_number}.html"
        site = requests.get(url)
        if site.status_code == 404:
            print(f"Reached the last page. Scraping finished! page {page_number - 1} was the last page")
            break
        print(f"Scraping page {page_number}...")
#==============================================================#
################## Start scaning each page #####################
        src = site.content
        soup = BeautifulSoup(src, "lxml")
        books = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
        for book in books:
            heading_name = book.find('h3')
            link = heading_name.find('a')
            book_name = link["title"]
            price = book.find('p', {"class": "price_color"}).text.strip()
            price = price[1:]
            avilability = book.find('p', {"class": "instock availability"}).text.strip()
            title_stars = book.find('p', {"class": "star-rating"})
            classes = title_stars['class']
            num_of_stars = classes[1]
            books_info.append({"Book name": book_name, "Price": price, "Avilable": avilability, "Stars": num_of_stars})
        page_number += 1
    keys = books_info[0].keys()
    with open('BookLibraryScrapData.csv', 'w') as output_file:
        dck_write = csv.DictWriter(output_file, keys)
        dck_write.writeheader()
        dck_write.writerows(books_info)
main()
