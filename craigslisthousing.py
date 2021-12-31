from craigslist import CraigslistEvents
cl_e = CraigslistEvents(site='newyork', filters={'free': True, 'food': True})

for result in cl_e.get_results(sort_by='newest', limit=5):
    print(result)