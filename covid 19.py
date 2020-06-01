# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 07:22:54 2020

@author: Lenovo
"""



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import warnings
corona=pd.read_csv('covid_19_data.csv')
corona.describe().T
corona= corona.rename(columns={'Province/State': 'Province','Country/Region':'Country','ObservationDate':'Date','Confirmed':'Cases'})

corona.Country.replace({'Mainland China': 'China'}, inplace=True)
corona['Date'] = corona['Date'].apply(pd.to_datetime)
corona.drop(['SNo'],axis=1,inplace=True)
corona.drop(list(corona[corona.Cases==0.0].index), axis = 0, inplace=True)

corona.isnull().sum()
coronamissing=corona[corona['Province'].isnull()]['Country'].value_counts().to_frame(name='Missing_Province_count')
coronacountry=corona['Country'].value_counts().to_frame(name='Country_count')
mergedDf = coronacountry.merge(coronamissing, left_index=True, right_index=True)
corona[corona.Country=='Others']
corona.Country.replace({'Others': 'Japan'}, inplace=True)
countries=corona.sort_values(by='Cases', ascending=False)['Country'].unique()
print("\nNumber of countries affected by covid 19 : ",len(countries))

corona.groupby("Country").aggregate(['mean', np.std,max,'count']).sort_values([('Cases','max')], ascending=False).head(40)
coronatotal=corona.groupby(['Date','Country'])['Cases','Deaths','Recovered'].sum()
coronatotal.reset_index(inplace=True)  
coronatotal['Death_rate']=coronatotal['Deaths']/coronatotal['Cases']
coronatotal['Recovery_rate']=coronatotal['Recovered']/coronatotal['Cases']
coronatotal[coronatotal.Country=='India']


coronatotal['log(Cases)']=np.log(coronatotal.Cases)

plt.rcParams["axes.labelsize"] = 20
plt.rcParams["xtick.labelsize"] = 16
plt.rcParams["ytick.labelsize"] = 16
sns.set_style("whitegrid")
sns.lineplot(x="Date", y="log(Cases)", hue='Country',linewidth=6,  data=coronatotal[coronatotal.Country.isin(countries[0:10])]);
plt.xticks(rotation=45,ha='right');
sns.set(rc={'figure.figsize':(14,14)})
leg = plt.legend(fontsize='x-large',loc=2, facecolor='white', )
# set the linewidth of each legend object
for i in leg.legendHandles:
    i.set_linewidth(10.0)


plt.rcParams["axes.labelsize"] = 20
plt.rcParams["xtick.labelsize"] = 16
plt.rcParams["ytick.labelsize"] = 16
sns.set_style("whitegrid")
sns.lineplot(x="Date", y="Death_rate", hue='Country', linewidth=6, data=coronatotal[(coronatotal.Country.isin(countries[0:10]))&(coronatotal.Date>'2020-03-15')]);
plt.xticks(rotation=45,ha='right');
sns.set(rc={'figure.figsize':(14,14)})
leg = plt.legend(fontsize='x-large',loc=2, facecolor='white', )
# set the linewidth of each legend object
for i in leg.legendHandles:
    i.set_linewidth(10.0)
plt.rcParams["axes.labelsize"] = 20
plt.rcParams["xtick.labelsize"] = 16
plt.rcParams["ytick.labelsize"] = 16
sns.set_style("whitegrid")
sns.lineplot(x="Date", y="Recovery_rate", hue='Country',linewidth=6, data=coronatotal[(coronatotal.Country.isin(countries[0:10]))&(coronatotal.Date>'2020-03-15')]);
plt.xticks(rotation=45,ha='right');
sns.set(rc={'figure.figsize':(14,14)})
leg = plt.legend(fontsize='x-large',loc=2, facecolor='white', )
# set the linewidth of each legend object
for i in leg.legendHandles:
    i.set_linewidth(10.0)    
 
    
    
