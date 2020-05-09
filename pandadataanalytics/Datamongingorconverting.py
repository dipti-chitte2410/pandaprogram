import pandas as pd
country=pd.read_csv('C:\\Users\\Asus\\Downloads\\FL_insurance_sample.csv',index_col=0)
country.to_html('insurance.html')