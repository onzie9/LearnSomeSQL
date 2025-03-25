import geonamescache as gnc


def dict_size(d: dict) -> int:
    output = 0
    for k in d.keys():
        output += len(d[k])
    return output


gc = gnc.GeonamesCache()
us_cities = {}
european_countries = {}
african_countries = {}
asian_countries = {}
south_american_countries = {}
oceania_countries = {}

european_cities = {}
african_cities = {}
asian_cities = {}
south_american_cities = {}
oceania_cities = {}

all_cities = gc.get_cities()
all_countries = gc.get_countries()

for c in all_countries.keys():
    if all_countries[c]['continentcode'] == 'EU':
        european_countries[c] = all_countries[c]
    elif all_countries[c]['continentcode'] == 'AF':
        african_countries[c] = all_countries[c]
    elif all_countries[c]['continentcode'] == 'AS':
        asian_countries[c] = all_countries[c]
    elif all_countries[c]['continentcode'] == 'OC':
        oceania_countries[c] = all_countries[c]
    elif all_countries[c]['continentcode'] == 'SA':
        south_american_countries[c] = all_countries[c]

#all_non_us_countries = {all_countries[c]}

for c in all_cities.keys():
    if all_cities[c]['countrycode'] == 'US':
        us_cities[c] = all_cities[c]
    elif all_cities[c]['countrycode'] in european_countries.keys():
        european_cities[c] = all_cities[c]
    elif all_cities[c]['countrycode'] in asian_countries.keys():
        asian_cities[c] = all_cities[c]
    elif all_cities[c]['countrycode'] in african_countries.keys():
        african_cities[c] = all_cities[c]
    elif all_cities[c]['countrycode'] in south_american_countries.keys():
        south_american_cities[c] = all_cities[c]
    elif all_cities[c]['countrycode'] in oceania_countries.keys():
        oceania_cities[c] = all_cities[c]

us_cities_for_db = {}
seen_states = []
all_states = list(set([us_cities[k]['admin1code'] for k in us_cities.keys()]))

for state in all_states:
    all_cities = []
    for k in us_cities.keys():
        if us_cities[k]['admin1code'] == state and us_cities[k]['population']>50000:
            all_cities.append(us_cities[k]['name'])
    us_cities_for_db[state] = all_cities

european_cities_for_db = {}
for ec in european_countries:
    all_cities = []
    for k in european_cities.keys():
        if european_cities[k]['countrycode'] == ec and european_cities[k]['population'] > 50000:
            all_cities.append(european_cities[k]['name'])
    european_cities_for_db[ec] = all_cities

asian_cities_for_db = {}
for ec in asian_countries:
    all_cities = []
    for k in asian_cities.keys():
        if asian_cities[k]['countrycode'] == ec and asian_cities[k]['population'] > 50000:
            all_cities.append(asian_cities[k]['name'])
    asian_cities_for_db[ec] = all_cities

african_cities_for_db = {}
for ec in african_countries:
    all_cities = []
    for k in african_cities.keys():
        if african_cities[k]['countrycode'] == ec and african_cities[k]['population'] > 50000:
            all_cities.append(african_cities[k]['name'])
    african_cities_for_db[ec] = all_cities

south_american_cities_for_db = {}
for ec in south_american_countries:
    all_cities = []
    for k in south_american_cities.keys():
        if south_american_cities[k]['countrycode'] == ec and south_american_cities[k]['population'] > 50000:
            all_cities.append(south_american_cities[k]['name'])
    south_american_cities_for_db[ec] = all_cities

oceania_cities_for_db = {}
for ec in oceania_countries:
    all_cities = []
    for k in oceania_cities.keys():
        if oceania_cities[k]['countrycode'] == ec and oceania_cities[k]['population'] > 50000:
            all_cities.append(oceania_cities[k]['name'])
    oceania_cities_for_db[ec] = all_cities

