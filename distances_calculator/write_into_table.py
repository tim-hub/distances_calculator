
def write_into(origina_address, table_abs_path):
    import pandas as pd
    from . import get_distance

    df = pd.read_csv(table_abs_path)

    df['distance_to_'+origina_address] = df.address

    df['distance_to_'+origina_address]  = df['distance_to_'+origina_address].map(lambda a: get_distance(origina_address, a))

    print(df)

    df.to_csv(table_abs_path)

