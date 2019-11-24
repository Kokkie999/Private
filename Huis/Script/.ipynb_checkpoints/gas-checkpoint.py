import pandas as pd
import numpy as np
import datetime as dt
import plotnine as p9
import matplotlib.pyplot as plt


# Ophalen data vanaf Raspberry PI
df = pd.read_csv('//raspberrypi/pi/domoticz/data/logging.csv')
df.columns = df.columns.str.lower()
df['timestamp'] = pd.to_datetime(df['timestamp'], format="%d-%m-%Y %H:%M:%S")
df['datum'] = pd.to_datetime(df['timestamp'].dt.date)

df = df[['timestamp',
         'datum',
         'dagverbruik_gas',
         'kamertemperatuur',
         'thermostaat',
         'buitentemperatuur']]
df = df.rename(columns={'datum': 'date',
                        'dagverbruik_gas': 'usage',
                        'kamertemperatuur': 'temp_room',
                        'thermostaat': 'temp_setting',
                        'buitentemperatuur': 'temp_out'})

# EERSTE INZICHTEN
# Gasverbruik per dag
usage_day = (
    df[['date', 'usage']]
    .dropna(subset=['usage'])
    #.set_index('date')
)
(p9.ggplot() + 
 p9.geom_line(data=usage_day, mapping=p9.aes("date", "usage")))
