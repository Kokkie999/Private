import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import datetime as dt
from plotly.subplots import make_subplots
from statistics import mean, median, mode, stdev


# Diverse instellingen
project = "Energiemanagement"
vandaag = dt.datetime.now().date().strftime("%d-%m-%Y")
opslag = "C:\\Users\\Iwan\\OneDrive\\Energiemanagement\\Output\\"


# Ophalen data vanaf Raspberry PI
df = pd.read_csv("//raspberrypi/pi/domoticz/data/logging.csv")
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%d-%m-%Y %H:%M:%S")


# Afgenomen elektrische vermogen in kW over de laatste 30 dagen
df_act_elektra_start = (dt.datetime.now()+dt.timedelta(days=-30)).date()
df_act_elektra_eind = dt.datetime.now().date()
df_act_elektra = df.copy()
df_act_elektra = df_act_elektra[['Timestamp', 'Actueel_Elektra']]
df_act_elektra = df_act_elektra.loc[
    (df_act_elektra['Timestamp'].dt.date >= df_act_elektra_start) &
    (df_act_elektra['Timestamp'].dt.date < df_act_elektra_eind)]
df_act_elektra['Meetwaarde'] = df_act_elektra['Actueel_Elektra']/1000
# df_act_elektra['Gemiddelde'] = mean(df_act_elektra['Meetwaarde'])
# df_act_elektra['Mediaan'] = median(df_act_elektra['Meetwaarde'])
df_act_elektra['80% contractwaarde'] = 5.856
df_act_elektra['90% contractwaarde'] = 6.624
df_act_elektra['Contractwaarde'] = 7.360

titel = ("Afgenomen elektrische vermogen tussen " +
         df_act_elektra_start.strftime("%d-%m-%Y") +
         " en " +
         vandaag)

fig = go.Figure()
fig.update_layout(
    template='plotly',
    title=go.layout.Title(text="<b>" + titel + "</b>",
                          font=dict(family='Arial', size=20, color='#141251')),
    autosize=True,
    margin=dict(l=50, r=50, t=100, b=50),
    paper_bgcolor='LightSteelBlue',
    showlegend=True,
    xaxis=go.layout.XAxis(
        rangeselector=dict(
            buttons=list([dict(count=1, label="gisteren",
                               step='day', stepmode='todate'),
                          dict(count=7, label="week",
                               step='day', stepmode='todate'),
                          dict(count=14, label="14 dagen",
                               step='day', stepmode='backward'),
                          dict(count=1, label= "Maand",
                               step='month', stepmode='backward')])
        ),
        rangeslider=dict(visible=True),
        type='date'
    )
)
fig.add_trace(
    go.Scatter(
        name="Meetwaarde",
        x=df_act_elektra['Timestamp'],
        y=df_act_elektra['Meetwaarde'],
        line=dict(color='blue', width=0.5)
    )
)
# fig.add_trace(
#    go.Scatter(
#        name="Gemiddelde",
#        x=df_act_elektra['Timestamp'],
#        y=df_act_elektra['Gemiddelde'],
#        line=dict(color='green', width=2)
#    )
# )
# fig.add_trace(
#    go.Scatter(
#        name='Mediaan',
#        x=df_act_elektra['Timestamp'],
#        y=df_act_elektra['Mediaan'],
#        line=dict(color='firebrick', width=2)
#    )
# )
fig.add_trace(
    go.Scatter(
        name='80% contractwaarde',
        x=df_act_elektra['Timestamp'],
        y=df_act_elektra['80% contractwaarde'],
        line=dict(color='orange', width=1, dash='dash')
    )
)
fig.add_trace(
    go.Scatter(
        name='90% contractwaarde',
        x=df_act_elektra['Timestamp'],
        y=df_act_elektra['90% contractwaarde'],
        line=dict(color='red', width=1, dash='dash')
    )
)
fig.add_trace(
    go.Scatter(
        name='Contractwaarde',
        x=df_act_elektra['Timestamp'],
        y=df_act_elektra['Contractwaarde'],
        line=dict(color='red', width=1)
    )
)
fig.update_xaxes(
    go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="<b>Timestamp</b>",
            font=dict(family='Arial', size=12, color='#141251')
        )
    ),
    tickangle=-45,
    tickfont=dict(family='Arial', size=12, color='#141251')
)
fig.update_yaxes(
    go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="<b>Afgenomen elektrische vermogen in kW</b>",
            font=dict(family='Arial', size=12, color='#141251')
        )
    ),
    tickfont=dict(family='Arial', size=12, color='#141251')
)
fig.write_html(opslag + titel + ".html")  # Visual wegschrijven
fig.show()