import pandas as pd

def data_import(name):

    data = pd.read_csv(name)

    df = pd.DataFrame(data)
    return df

