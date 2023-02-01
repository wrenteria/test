# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:51:06 2023

@author: wrenteria
"""
import numpy as np
import streamlit as st
f = open('texto.txt')
t = f.readline()
f.close()
st.write("Hello ,let's learn how to build a streamlit app together")
st.title ("Test application")
st.header(t)
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
