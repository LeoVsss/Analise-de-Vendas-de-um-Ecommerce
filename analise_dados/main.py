from pathlib import Path
from extract import extract_data
from transform import rename_table
from load import create_table



path_arq = Path(__file__).resolve().parent.parent / "csv" / "online_shopping.csv"

df = extract_data(path_arq)
df_renamed = rename_table(df)
create_table(df_renamed, 'compras')
