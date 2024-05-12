import pandas as pd
from sqlalchemy import create_engine

user      = 'postgres'
password  = 'postgres'
hostname  = '127.0.0.1'
database  = 'postgres'
port      = '5436'
conn_string = f'postgresql://{user}:{password}@{hostname}:{port}/{database}'
engine      = create_engine(conn_string)
conn        = engine.connect()

# ---------- Buat Ambil dan jadiin Table di database------
df = pd.read_csv('https://github.com/Calycha/Assignment_Day_35_Kelompok_13/blob/main/Sales_data.csv')
df = df[['Order_ID','Date','Customer_Id','City','Product ID','Cupcake_Flavor','Quantity','Unit_Price','rating']]
df.to_sql("Sales_data",engine, if_exists='replace')

# ---------- Ngambil di database buat jadi dataframe ----------
query   = "SELECT * FROM Sales_data"
df_read = pd.read_sql(query,engine)
df_read.head()