import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

#Graph type in metaplotlib library
style.use('fivethirtyeight')
country=pd.read_csv('C:\\Users\\Asus\\Documents\\book1.csv',index_col=0)
#pd reads csv file using read_csv
df=country.head(5)
#display top five data of country csv file
df=df.set_index(['countrycode'])
#set index as per countrycode
sd=df.reindex(columns=['2010','2011'])
#Pandas dataframe.reindex() function conform DataFrame to new index with optional filling logic
df=sd.diff(axis=1)
#To display difference between two columns
df.plot(kind='bar')
#Toplot bar
plt.show()
#display