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


