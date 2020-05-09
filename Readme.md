DATA ALAYTICS
PYTHON application
1.Web scrapping
2.Testing
3.Web development
4.Data analytics

Data is stored in differnet format eg Excel,chart
To perform analysis over this data it is stored in common data format called as Data warehousing
Then analysis is perform over this data warehousing for data visulaization where data can be display or predict in different format such as graph,pie chart etc

Data analysis Example =>Percentage increase in unemployment in India from 2010 to 2012

Panda =>is software library in python programming language for data manipulation and analysis
suited for:
1.Tabular data with heterogeneously types columns
2.ordered and unordered time series data
3.arbitary matrix data with row and column labels
4.Any other form of observational/statistical data sets.

1.DataFrame

Operation performed on pandas Dataframe:
1.Slicing DataFrame
print('starting first two\n',df.head(2))
print('Ending last two\n',df.tail(2))
2.Changing index
\*\*df.set_index('Day',inplace=True)

3.Data COnversion or data munging
**country=pd.read_csv('C:\\Users\\Asus\\Downloads\\FL_insurance_sample.csv',index_col=0)
country.to_html('insurance.html')**
4.Joining and merging
Joining is done based on index and
\*\*joining=df1.join(df2)
\*\*joing=df2.join(df2)
merge
\*\* pd.merge(df1,df2,on='HPI')
5.Concatenation
6.Changing the column header
\*\*df=df.rename(columns={'visitor':'users'})
