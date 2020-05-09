import pandas as pd
xyz_web={
    'day':[1,2,3,4,5,6],
    'visitor':[1000,700,6000,1000,400,350],
    'Bounce_rate':[20,20,23,15,10,34]
}


df=pd.DataFrame(xyz_web)
print(df)

#Slicing
print('starting first two\n',df.head(2))
print('Ending last two\n',df.tail(2))