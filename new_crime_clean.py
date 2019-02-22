import pandas as pd


#opening the  excel file
crime = pd.read_excel("CrimeStatebyState.xlsx",  index_col=0)


#converting from wide to long format
crime = crime.stack(0).reset_index()
#renaming the column names 
crime.rename(columns={crime.columns[0]:'Year',
                          crime.columns[1]: 'Crime_type',
                          crime.columns[2]: 'Total_number'},
                 inplace=True)
#saving the cleaned file as new_crime.csv 
crime.to_csv(path_or_buf="new_crime.xlsx", index=False)
