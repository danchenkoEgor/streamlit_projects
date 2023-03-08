import streamlit as st 
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 

st.write("""
# Tips dataset analytics

Source: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
""")

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

st.write("""
### Who orders the most - men or women?
""")
         
fig, axes = plt.subplots(2, 1, figsize = (7, 7))

sns.histplot(data = tips, x = 'total_bill', hue = 'sex', ax = axes[0])\
    .set(title = 'Histplot', xlabel = 'Total Bill', ylabel = 'Count')
sns.violinplot(data = tips, x = 'sex', y = 'total_bill', ax = axes[1])\
    .set(title = 'Violin Plot', xlabel = 'Sex', ylabel = 'Total Bill')
plt.tight_layout()

st.pyplot(fig)

st.write("""
According to the charts above the average bill is somewhat larger for men
""")

st.write("""
### What is the distribution of total bill size across the week for both sexes?
""")
         
figs, ax = plt.subplots()
sns.barplot(data = tips, x = 'day', y = 'total_bill', hue = 'sex')\
    .set(title = 'Barplot', xlabel = 'Day', ylabel = 'Total Bill')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

st.pyplot(figs)

st.write("""
It turns out that men spend the most on sundays as well as women. 
The smallest checks for men are on thursdays, for women - on fridays.
It is noticable that on fridays men have an unusually large spread of bill totals which can indicate
an increases impulsivity of purchase behaviour. 


## Summary

An in-depth investigation of male impulsive purchase behaviour triggers is adviced in order
to max-out the profits. 
""")