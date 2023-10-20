import streamlit as st
import pandas as pd
from datetime import datetime
import Filter


df = pd.read_csv("resources/wetterdaten.csv")
df = df.loc[:, ~df.columns.isin(['Datum', 'Zeit'])]
lst_row = df.iloc[-1]
stop_d_value=lst_row['Timestamp']
parsed_datetime = datetime.strptime(stop_d_value, "%Y-%m-%d %H:%M:%S")


st.title("Downloads")

st.markdown('''
### Choose your filters 
''')
filtered = Filter.filter_dataframe(df)
st.write()
st.write(filtered)

st.line_chart(filtered)

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

#st.line_chart(filtered, x="Timestamp", y="Temp1")







