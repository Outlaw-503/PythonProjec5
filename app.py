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
  st.bar_chart(data=data,x="brand_name",y="price")
  st.bar_chart(data=data,x="brand_name",y="rating")
  st.bar_chart(data=data,x="processor_brand",y="rating")
  st.bar_chart(data=data,x="processor_brand",y="price")
