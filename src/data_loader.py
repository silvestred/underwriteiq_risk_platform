import pandas as pd

def load_claims():
    return pd.read_csv("../data/insurance_simple/claims.csv")

def load_contracts():
    return pd.read_csv("../data/insurance_simple/contracts.csv")

def load_vehicles():
    return pd.read_csv("../data/insurance_simple/vehicles.csv")


