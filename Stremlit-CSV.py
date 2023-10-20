import streamlit as st
import pandas as pd
from datetime import datetime
import Filter
import seaborn as sns
import matplotlib.pyplot as plt
import Plot



df = pd.read_csv("resources/wetterdaten2.csv")
df = df.loc[:, ~df.columns.isin(['Datum', 'Zeit'])]
lst_row = df.iloc[-1]
stop_d_value=lst_row['Timestamp']
parsed_datetime = datetime.strptime(stop_d_value, "%Y-%m-%d %H:%M:%S")


st.title("Downloads")

st.markdown('''
### Choose your filters 
''')
filtered = Filter.filter_dataframe(df)
st.write(filtered)



st.markdown('''
#### Download here!
''')
csv_data = filtered.to_csv(index= False)
st.download_button(
    label='Download as csv',
    data=csv_data,
    file_name='customTimeFrame.csv',
    key='download_button'

)
st.markdown('''
## Graph
''')

filtered_notnull = filtered.dropna()
option = st.selectbox(
     'Select What do you want so see',
    ('Value1','Temp1','Temp2','Temp3','Globalstrahlung','Gehaeusetemp','Windgeschw','Windrichtung','Lufttemperatur','rel Feuchte','Taupunkttemp','Luftdruck abs','Luftdruck red','Helligkeit Nord','Helligkeit Ost','Helligkeit Sued','Helligkeit West','Helligkeit','Niederschlag','NiedIntensitaet','NiedSumme','Niederschlagsart','Sonne Elevation','Sonne Azimut','Globalstrahlung'))





st.pyplot(Plot.get_plot(filtered_notnull))
#st.line_chart(filtered_notnull, x="Timestamp", y=option,height=500, width=1500)












