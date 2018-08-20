from osm_coordinate import get_coordinate

def extract_coordinate(the_address):
    import json
    addr= json.loads(get_coordinate(the_address))[0]
    return (addr["lat"], addr["lon"])



def get_distance(addr1, addr2):

    # https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
    # credits to Micheal
    from math import sin, cos, sqrt, atan2, radians

    coord1= extract_coordinate(addr1)
    print(coord1)
    coord2 = extract_coordinate(addr2)
    print(coord2)

    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(float(coord1[0]))
    lon1 = radians(float(coord1[1]))
    lat2 = radians(float(coord2[0]))
    lon2 = radians(float(coord2[1]))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    print("Result:", distance)
    # print("Should be:", 278.546, "km")
    return distance

def main_cmd():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("address1", help="address 1")
    parser.add_argument("address2", help="address 2")
    args = parser.parse_args()

    print(get_distance(args.address1, args.address2))


