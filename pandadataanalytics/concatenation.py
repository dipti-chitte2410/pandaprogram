import pandas as pd

df1=pd.DataFrame({'HPI':[80,90,70,60],"int_rate":[2,1,2,3],"ind_GDP":[50,45,45,67]},
index=[2001,2002,2003,2004])
df2=pd.DataFrame({'HPI':[80,99,70,60],"int_rate":[2,1,2,3],"ind_GDP":[50,45,45,67]},
index=[2004,2006,2007,2008])

concat=pd.concat([df1,df2])
print(concat)


#       HPI  int_rate  ind_GDP
# 2001   80         2       50
# 2002   90         1       45
# 2003   70         2       45
# 2004   60         3       67
# 2004   80         2       50
# 2006   99         1       45
# 2007   70         2       45
# 2008   60         3       67