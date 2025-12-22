import pandas as pd

def clean_claims(df):
    df = df.copy()
    df = df.drop_duplicates()
    return df

claims = load_claims().drop_duplicates()

contracts = load_contracts().drop_duplicates()

vehicles = load_vehicles().drop_duplicates()