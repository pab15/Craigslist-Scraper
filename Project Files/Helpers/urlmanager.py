def urlManager(region, owner):
    if owner == 'owner':
        owner = 'cto'
    elif owner == 'all':
        owner = 'cta'
    elif owner == 'dealer':
        owner = 'ctd'
    else:
        owner = 'cta'
    return 'https://{}.craigslist.org/search/{}?'.format(region, owner)

def refineSearch(url):
    search_distance = ''
    postal_code = ''
    min_price = ''
    max_price = ''
    make_model = ''
    search_refinement = ''
    return ""

if __name__ == '__main__':
    print(urlManager('sfbay', 'owner'))
    print(urlManager('humboldt', 'dealer'))
    print(urlManager('medford', 'all'))
    print(urlManager('sfbay', 'idc'))