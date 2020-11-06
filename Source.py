###########################################

#importing req libs and api keys
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
from fredapi import Fred
fred = Fred(api_key='39596b7773612d3467c2e9xxxxxxxxxx') # fred api key

#calling ISM man_pmi
ism_pmi = quandl.get("ISM/MAN_PMI", authtoken="qHmb8WS585xxxxxxxxxx")

#calling ISM non-man_pmi
ism_nmi = quandl.get("ISM/NONMAN_NMI", authtoken="qHmb8WS585xxxxxxxxxx")

#calling Uni Of Mich. Consumer Sent. Indi.
umcsi = fred.get_series('UMCSENT')

#calling Building Permit
bui_perm = fred.get_series('PERMIT')

#calling Manufacturers' New Orders: Durable Goods
dur_goods = fred.get_series('DGORDER')

#calling Industrial Production: Total Index 
ind_pro = fred.get_series('INDPRO')

#calling Unemployment Rate 
unemploy = fred.get_series('UNRATE')

##############################################

#printing latest figs
last_ism_pmi = ism_pmi.iloc[[-1]]
last_ism_nmi = ism_nmi.iloc[[-1]]
last_umcsi = umcsi.iloc[[-1]]
last_bui_perm = bui_perm.iloc[[-1]]
last_dur_goods = dur_goods.iloc[[-1]]
last_ind_pro = ind_pro.iloc[[-1]]
last_unemploy = unemploy.iloc[[-1]]
print('ISM PMI :',last_ism_pmi) 
print('ISM NMI :',last_ism_nmi)
print('UMCSI :',last_umcsi)
print('BUILDING PERMITS :',last_bui_perm)
print('DURABLE GOODS :',last_dur_goods)
print('INDUSTRIAL PRODUCTION :',last_ind_pro)
print('UNEMPLOYMENT RATE :',last_unemploy)

##############################################



