
def write_into(origina_address, table_abs_path):
    import pandas as pd
    from . import get_distance

    df = pd.read_csv(table_abs_path)

    df['distance_to_'+origina_address] = df.address

    df['distance_to_'+origina_address]  = df['distance_to_'+origina_address].map(lambda a: get_distance(origina_address, a))

    print(df)

    df.to_csv(table_abs_path)


def main_cmd():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("address", help="original address, like '125 Queen St, Auckland, 0620' ")
    parser.add_argument("csv_path", help="like '/user/test.csb' ")
    args = parser.parse_args()

    # print("{0:.3f} km".format(get_distance(args.address1, args.address2)))
    write_into(args.address, args.csv_path)

