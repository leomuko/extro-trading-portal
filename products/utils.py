from importlib import resources

with resources.files('tzdata.zoneinfo').joinpath('iso3166.tab').open('r') as f:
    country_names = list(
        line.rstrip('\n').split('\t', 1)
        for line in f
        if not line.startswith('#')
    )

for i, country in enumerate(country_names):
    country_names[i][0] = country_names[i][1]
    if country[0] == 'UG':
        _, country_names = country_names.pop(i), country_names
