import pandas as pd
df1=pd.DataFrame({"int_rate":[2,1,2,3],"ind_GDP":[50,45,45,67]},
index=[2001,2002,2003,2005])
df2=pd.DataFrame({"lower_hpI_rate":[50,60,70,80],"unemployment":[1,3,5,6]},
index=[2002,2003,2004,2001])

joining=df1.join(df2)
print(joining)
#           int_rate  ind_GDP  lower_hpI_rate  unemployment
# 2001         2       50            80.0           6.0
# 2002         1       45            50.0           1.0
# 2003         2       45            60.0           3.0
# 2005         3       67             NaN           NaN
joining=df2.join(df1)
print(joining)
#           lower_hpI_rate  unemployment  int_rate  ind_GDP
# 2002              50             1       1.0     45.0
# 2003              60             3       2.0     45.0
# 2004              70             5       NaN      NaN
# 2001              80             6       2.0     50.0