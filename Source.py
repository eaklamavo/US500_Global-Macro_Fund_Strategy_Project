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
fred = Fred(api_key='39596bxxxxxxxxxxx5a8ed5') # fred api key

#calling ISM man_pmi
ism_pmi = quandl.get("ISM/MAN_PMI", authtoken="qHmb8Wxxxxxxxxx8fx")
                
#calling ISM non-man_pmi
ism_nmi = quandl.get("ISM/NONMAN_NMI", authtoken="qHmb8xxxxxxxxx8fx")
ism_nmi = ism_nmi.rename(columns={"Index": "NMI"})

#calling Real Gross Domestic Product  
gdp = fred.get_series('A191RL1Q225SBEA')
gdp = gdp.to_frame()
gdp.index.name = 'Date'
gdp.columns = ["GDP (%)"]

#calling Uni Of Mich. Consumer Sent. Indi.
umcsi = fred.get_series('UMCSENT')
umcsi = umcsi.to_frame()
umcsi.index.name = 'Date'
umcsi.columns = ["UMCSI"]

#calling Building Permit
bui_perm = fred.get_series('PERMIT')
bui_perm = bui_perm.to_frame()
bui_perm.index.name = 'Date'
bui_perm.columns = ["Num. of Permits"]

#calling Manufacturers' New Orders: Durable Goods
dur_goods = fred.get_series('DGORDER')
dur_goods = dur_goods.to_frame()
dur_goods.index.name = 'Date'
dur_goods.columns = ["Durable Goods qty"]

#calling Industrial Production: Total Index 
ind_pro = fred.get_series('INDPRO')
ind_pro = ind_pro.to_frame()
ind_pro.index.name = 'Date'
ind_pro.columns = ["Ind_Prodtn. qty"]

#calling Unemployment Rate 
unemploy = fred.get_series('UNRATE')
unemploy = unemploy.to_frame()
unemploy.index.name = 'Date'
unemploy.columns = ["Num. of Unemployed"]

#calling Initial Claims 
ini_claims = fred.get_series('ICSA')
ini_claims = ini_claims.to_frame()
ini_claims.index.name = 'Date'
ini_claims.columns = ["Num. of Init.Claims"]

#calling Continued Claims (Insured Unemployment) 
cont_claims = fred.get_series('CCSA')
cont_claims = cont_claims.to_frame()
cont_claims.index.name = 'Date'
cont_claims.columns = ["Num. of Contd.Claims"]

##############################################

#printing latest figs
last_ism_pmi = ism_pmi.iloc[[-1]]
last_ism_nmi = ism_nmi.iloc[[-1]]
last_umcsi = umcsi.iloc[[-1]]
last_bui_perm = bui_perm.iloc[[-1]]
last_dur_goods = dur_goods.iloc[[-1]]
last_ind_pro = ind_pro.iloc[[-1]]
last_unemploy = unemploy.iloc[[-1]]
last_ini_claims = ini_claims.iloc[[-1]]
last_cont_claims = cont_claims.iloc[[-1]]
last_gdp = gdp.iloc[[-1]]

print('ISM PMI :',last_ism_pmi) 
print('ISM NMI :',last_ism_nmi)
print('REAL GDP :',last_gdp)
print('UMCSI :',last_umcsi)
print('BUILDING PERMITS :',last_bui_perm)
print('DURABLE GOODS :',last_dur_goods)
print('INDUSTRIAL PRODUCTION :',last_ind_pro)
print('UNEMPLOYMENT RATE :',last_unemploy)
print('INITIAL CLAIMS :',last_ini_claims)
print('CONTINUED CLAIMS :',last_cont_claims)

###############################################

#Visualization

#ISM PMI chart
import warnings
warnings.filterwarnings('ignore')
fig, ax = plt.subplots(figsize=(16, 8))
plt.plot(ism_pmi, color='blue', label='PMI')
plt.grid()
plt.title("Purchasing Manager's Index (PMI) Composite Index")
plt.legend(loc='upper left')
plt.axhline(50, color ='black')

#ISM NMI chart
fig, ax = plt.subplots(figsize=(16, 8))
plt.plot(ism_nmi, color='blue', label='NMI')
plt.grid()
plt.title("Services Purchasing Manager's Index (NMI) Composite Index")
plt.legend(loc='upper left')
plt.axhline(50, color ='black')

#Real GDP Chart
fig, ax = plt.subplots(figsize=(16, 8))
plt.plot(gdp, color='blue', label='Real GDP')
plt.grid()
plt.title("Real Gross Domestic Product (%)")
plt.legend(loc='upper left')
plt.axhline(0, color ='black')

#University Of Michigan Consumer Sentiment Index (UMCSI) chart
fig, ax = plt.subplots(figsize=(16, 8))
plt.plot(umcsi, color='blue', label='UMCSI')
plt.grid()
plt.title("University Of Michigan Consumer Sentiment Index (UMCSI)")
plt.legend(loc='upper left')

#New Private Housing Units Authorized by Building Permits chart
fig, ax = plt.subplots(figsize=(16, 8))
plt.plot(bui_perm, color='blue', label='Building Permits')
plt.grid()
plt.title("New Private Housing Units Authorized by Building Permits")
plt.legend(loc='upper left')

#Manufacturers' New Orders: Durable Goods chart
fig, ax = plt.subplots(figsize=(16, 8))
plt.plot(dur_goods, color='blue', label='New Orders: Durable Goods')
plt.grid()
plt.title("Manufacturers' New Orders: Durable Goods")
plt.legend(loc='upper left')

#Industrial Production Index chart
fig, ax = plt.subplots(figsize=(16, 8))
plt.plot(ind_pro, color='blue', label='Industrial Production Index')
plt.grid()
plt.title("Industrial Production Index")
plt.legend(loc='upper left')

#Unemployment Rate chart
fig, ax = plt.subplots(figsize=(16, 8))
plt.plot(unemploy, color='blue', label='Unemployment Rate')
plt.grid()
plt.title("Unemployment Rate (%)")
plt.legend(loc='upper left')

#Initial Claims chart
fig, ax = plt.subplots(figsize=(16, 8))
plt.plot(ini_claims, color='blue', label='Initial Claims')
plt.grid()
plt.title("Initial Claims")
plt.legend(loc='upper left')

#Continued Claims (Insured Unemployment) chart
fig, ax = plt.subplots(figsize=(16, 8))
plt.plot(cont_claims, color='blue', label='Continued Claims')
plt.grid()
plt.title("Continued Claims (Insured Unemployment)")
plt.legend(loc='upper left')
