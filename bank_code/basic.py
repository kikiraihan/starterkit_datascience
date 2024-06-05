# change root folder in notebook
import sys
sys.path.append('../')
from helper.visualisasiHelper import plotly_graph

# import module reload
import importlib
importlib.reload(sys.modules['folder_modul.nama_modul'])


#reverse dataframe
df_reversed = df.iloc[::-1]
