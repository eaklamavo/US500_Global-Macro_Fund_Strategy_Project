###ISM Manufacturing Index (PMI)####

###1####
##install quandl
#!pip install Quandl
########

##import required libraries##
import pandas as pd
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
%matplotlib inline
import quandl

###2####
##call ISM_PMI from quandl
########
ism_pmi = quandl.get("ISM/MAN_PMI", authtoken="qHmbxxxxxxxxD8fx")
ism_pmi #quick view

###3####
###simple line chart
########
ism_pmi.plot()

###End####

###ISM Non-Manufacturing Index (NMI)####

###4####
##call ISM_NMI from quandl
########
ism_nmi = quandl.get("ISM/NONMAN_NMI", authtoken="qHmbxxxxxxxxD8fx")
ism_nmi #quick view

###5####
###simple line chart
########
ism_nmi.plot()

###End####

###6####
###show latest ISM releases
########
last_ism_pmi = ism_pmi.iloc[[-1]]
last_ism_nmi = ism_nmi.iloc[[-1]]
print(last_ism_pmi) 
print(last_ism_nmi)

###End####
