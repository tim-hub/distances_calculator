def get_coordinate(the_address):
    import time
    import requests
    import random
    the_url = 'https://nominatim.openstreetmap.org/search?q='
    the_format = '&format=json'
    durations = [0, 0.1, 0.3, 0.5, 1, 1.2]

    if (the_address!="" and the_address!=None):
        time.sleep(random.choice(durations))
        return requests.get(the_url+the_address+the_format).text
    else:
        return None

