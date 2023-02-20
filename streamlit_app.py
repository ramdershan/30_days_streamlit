import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime
#Day 2

# st.write("Hello World!") 

#Day 3

# st.header('st.button')

# if st.button("Say Hello"):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')

##Day 5

# st.header('st.write')

# # Example 1

# st.write('Hello, *World!* :sunglasses:')

# # Example 2

# st.write(1234)

# # Example 3

# df = pd.DataFrame({
#      'first column': [1, 2, 3, 4],
#      'second column': [10, 20, 30, 40]
#      })
# st.write(df)

# # Example 4

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# # Example 5

# df2 = pd.DataFrame(
#      np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#      x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c)

## Day 8

# st.header('st.slider')

# # Example 1

# st.subheader('Slider')

# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years old')

# # Example 2

# st.subheader("Range slider")

# values = st.slider(
#      "Select a range of values",
#      0.0, 100.0, (25.0, 75.0)
# )
# st.write('Values:', values)

# # Example 3

# st.subheader('Range time slider')

# appointment = st.slider(
#      "Schedule your appointment:",
#      value = (time(11, 30), time(12, 45)),
#      format = "hh:mm"
# )

# st.write("You're scheduled for:", appointment)

# #Example 4

# st.subheader("Datetime slider")

# start_time = st.slider(
#      "When do you start?",
#      value = datetime(2020, 1, 1, 9, 30),
#      format = 'MM/DD/YY - hh:mm'
# )

# st.write('Start time:', start_time)

## Day 9

# st.header('Line Chart')

# chart_data = pd.DataFrame(
#                np.random.randn(20,3),
#                columns = ['a', 'b', 'c']
# )

# st.line_chart(chart_data)

## Day 10

# st.header('st.selectbox')

# option = st.selectbox(
#      'What is your favourite colour?',
#      ('Blue', 'Red', 'Green')
# )

# st.write('Your favourite colour is ', option)

## Day 11

st.header('st.multiselect')

options = st.multiselect(
     "What are your favourite colours",
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red']
)

st.write('You selected:', options)