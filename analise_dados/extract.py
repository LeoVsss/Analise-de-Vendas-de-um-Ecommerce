import pandas as pd
import numpy
from pathlib import Path
import math

path_arq = Path(__file__).resolve().parent.parent / "csv" / "online_shopping.csv"

def extract_data(path):
  df = pd.read_csv(path)
  print("-- Extração dos dados ocorrida com sucesso")
  return df