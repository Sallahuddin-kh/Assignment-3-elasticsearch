import random
from elasticsearch import Elasticsearch

def populate_index():
    """
    Method populates an index named cities in local elasticsearch
    Adds random values in column City_name, Country_name, City_area and City_population
    in index named "cities". The index should be made manually before hand.
    """
    es = Elasticsearch()
    for i in range(1,1001):
        city_name = "city_"+str(i)
        country_name = "country_"+str(random.randint(1,20))
        city_area = random.randint(1,200)
        city_population = random.randint(5,20)
        doc = {
            "City_name":city_name,
            "Country_name":country_name,
            "City_area":city_area,
            "City_population":city_population
        }
        res = es.index(index="cities", id=i, body=doc)
        