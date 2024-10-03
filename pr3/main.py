from bs4 import BeautifulSoup as bs
import requests

url = "https://www.muztorg.ru/category/akusticheskie-udarnye"

print(f"Страница {url}")

response = requests.get(url)
soup = bs(response.content, "html.parser")

products = soup.find_all("article", class_="catalog-card")
product_count = len(products)
print(f"\nКоличество товаров на странице: {product_count}")

most_expensive_product = None
cheapest_product = None
highest_rated_product = None
lowest_rated_product = None


for product in products:
    name_tag = product.find("a", class_="catalog-card__name")
    price_tag = product.find("meta", itemprop="price")
    rating_tag = product.find("div", class_="catalog-card__rating")

    if name_tag and price_tag:
        name = name_tag.text.strip()
        price_str = price_tag['content'].replace('&nbsp;', '').replace('\xa0', '').replace(',', '.')
        price = float(price_str)

        if most_expensive_product is None or price > most_expensive_product[1]:
            most_expensive_product = (name, price)

        if cheapest_product is None or price < cheapest_product[1]:
            cheapest_product = (name, price)

        if rating_tag:
            rating_str = rating_tag.find('span').text.split()[0]
            rating = float(rating_str.replace(',', '.'))

            if highest_rated_product is None or rating > highest_rated_product[1]:
                highest_rated_product = (name, rating)
            
            if lowest_rated_product is None or rating < lowest_rated_product[1]:
                lowest_rated_product = (name, rating)



print(f"\nСамый дорогой товар: {most_expensive_product[0]} - {most_expensive_product[1]} руб.")
print(f"\nСамый дешевый товар: {cheapest_product[0]} - {cheapest_product[1]} руб.")
print(f"\nТовар с самой высокой оценкой: {highest_rated_product}\nТовар с самой низкой оценкой: {lowest_rated_product}")
 
