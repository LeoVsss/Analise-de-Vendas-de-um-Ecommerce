import pandas as pd


def rename_table(df):
  translate_column = {'customer_id':'cliente_id',
               'gender':'genero',
               'age':'idade',
               'country':'pais',
               'device_type':'tipo_dispositivo',
               'product_category':'categoria_produto',
               'time_spent_minutes':'tempo_gasto_minutos',
               'items_viewed':'itens_vistos',
               'items_purchased':'itens_comprados',
               'total_spent_usd':'total_gasto_em_dolar' }

  translate_device = {
    'Mobile':'Celular',
    'Desktop':'Computador',
  }

  translate_category = {
    'Electronics':'Eletrônicos',
    'Clothing':'Roupas',
    'Sports':'Esporte',
    'Home':'Domicílio',
    'Beauty':'Beleza',
    'Books':'Livros'
  }

  translate_gender = {
    'Male':'Masculino',
    'Female':'Feminino'
  }

  translate_country = {
    'UK':'Reino Unido',
    'USA':'EUA',
    'Pakistan':'Paquistão',
    'India':'Índia',
    'Canada':'Canadá',
    'Australia':'Austrália'

  }




  df = df.rename(columns = translate_column)
  df['tipo_dispositivo'] = df['tipo_dispositivo'].replace(translate_device)
  df['categoria_produto'] =df['categoria_produto'].replace(translate_category)
  df['genero'] = df['genero'].replace(translate_gender)
  df['pais'] = df['pais'].replace(translate_country)
  df['cliente_id'] = df['cliente_id'].str.replace('CUST', 'CLIEN')

  print("-- Traduções dos campos ocorrida com sucesso")
  return df

