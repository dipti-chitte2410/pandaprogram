import pandas as pd

df1=pd.DataFrame({'HPI':[80,90,70,60],"int_rate":[2,1,2,3],"ind_GDP":[50,45,45,67]},
index=[2001,2002,2003,2004])
df2=pd.DataFrame({'HPI':[80,99,70,60],"int_rate":[2,1,2,3],"ind_GDP":[50,45,45,67]},
index=[2005,2006,2007,2008])

merge=pd.merge(df1,df2,on='HPI')
 
print(merge)

#     HPI  int_rate_x  ind_GDP_x  int_rate_y  ind_GDP_y
# 0   80           2         50           2         50
# 1   70           2         45           2         45
# 2   60           3         67           3         67