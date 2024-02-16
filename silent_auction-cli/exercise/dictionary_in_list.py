country = input("Enter the country you visited: ")
visits = int(input("Enter the number of times you visited: "))
cities = input("Enter the cities you visited: ").split()

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris","Lille","Djion"]
    },
    {
        "country": "Germany",
        "visits": 11,
        "cities": ["Berlin","Moskow","Warsaw"]
    }
]

def add_new_country(country,visits,cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

add_new_country(country,visits,cities)

print(f"I've been to {travel_log[2]["country"]} {travel_log[2]["visits"]} times")

print(f" My favorite city is {travel_log[2]["cities"][0]}")