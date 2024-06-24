import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
s=st.container()
with s:
  data=pd.read_csv("smartphones_cleaned_v6.csv")
  data.dropna(subset=["rating","processor_brand","num_cores","processor_speed","battery_capacity","num_front_cameras","os","primary_camera_front"],axis=0,inplace=True)
  data.drop(columns=["fast_charging","extended_upto"],inplace=True)
  st.write("A Chart showing total sales according to phone brands \n")
  st.bar_chart(data=data,x="brand_name",y="price")
  st.write("A Chart showing total sales according to processor brands \n")
  st.bar_chart(data=data,x="processor_brand",y="price")
  st.write("A Chart showing refresh rates of smartphones in terms of their operating system \n")
  st.bar_chart(data=data,x="os",y=data["refresh_rate"].unique())
