import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


df=pd.DataFrame({'Day':[1,2,3,4],'visitor':[200,100,230,300],'bounce_rate':[20,45,60,10]})

df.set_index('Day',inplace=True)
# print(df)

# change index value as per 'Day' value
#      visitor  bounce_rate
# Day
# 1        200           20
# 2        100           45
# 3        230           60
# 4        300           10

# df.plot()
# plt.show()


#Change Header
df=df.rename(columns={'visitor':'users'})
print(df)
#      users  bounce_rate
# Day
# 1      200           20
# 2      100           45
# 3      230           60
# 4      300           10