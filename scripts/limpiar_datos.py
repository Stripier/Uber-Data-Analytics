import zipfile
import pandas as pd

#Descomprimir el archivo zip
with zipfile.ZipFile(r'C:/Users/karal/OneDrive/Escritorio/Github DK/Proyectos/Uber-Data-Analytics/datasets/uber-ride-analytics-dashboard.zip', 'r') as zip_ref:
    zip_ref.extractall('C:/Users/karal/OneDrive/Escritorio/Github DK/Proyectos/Uber-Data-Analytics/datasets')
    
print("Archivo descomprimido exitosamente.")

df=pd.read_csv(r'C:/Users/karal/OneDrive/Escritorio/Github DK/Proyectos/Uber-Data-Analytics/datasets/ncr_ride_bookings.csv')