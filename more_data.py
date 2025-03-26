from faker import Faker
import geonamescache as gnc
import datetime
from dateutil.relativedelta import relativedelta
import random

# Create a year of dates.
num_years = 10
base = datetime.datetime(year=2021, day=1, month=1)
date_list_years = [(base + relativedelta(years=x)).strftime('%m/%d/%Y') for x in range(num_years)]
date_list_weeks = [(base + relativedelta(weeks=x)).strftime('%m/%d/%Y') for x in range(num_years*52)]

# Each country only has one key, so only the last date is showing up.
# I need to create a dictionary with two keys or whatever.  Or just a nested dict.
country_name = {}
gc = gnc.GeonamesCache()
all_countries = gc.get_countries()
for k in all_countries.keys():
    country_data = {'Leader': '', 'Address': '', 'Motto': ''}
    for lang in all_countries[k]['languages'].split(','):
        try:
            leader = Faker(lang).name()
            country_data['Address'] = Faker(lang).address()
            country_data['Motto'] = Faker(lang).text(max_nb_chars=30)
            for d in date_list_years:

                if random.random() < .25:
                    leader = Faker(lang).name() # Simulates elections or changes in power.
                country_data['Leader'] = leader
                country_name[(k,d)] = country_data

            break
        except (AttributeError, IndexError) as e:
            pass
