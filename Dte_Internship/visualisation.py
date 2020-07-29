from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import pandas as pd
import re

#visualisation of data
data=pd.read_csv('final.csv' ,encoding='LATIN-1')
x=data['Autonomy_status'].iloc[0:50].values
y=data['College_region'].iloc[0:50].values
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_title(" colllege region VS Autonomy status")
plt.xlabel('Autonomy_status')
plt.ylabel('College Region')
ax.plot(x,y)