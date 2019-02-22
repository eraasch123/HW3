import pandas as pd
#reading the data in python
divorce = pd.read_excel('divorce.xlsx',
                        skiprows=5,                     
                       header=[0], #skipping the header
                       skipfooter=4, #cleaning the footer
                       #na_values='---', #null values
                       usecols=22, # all the columns that we need from the dirty excel file                       
                       index_col=[0])

#dropping empty rows
#divorce.drop(divorce.index[0])
divorce = divorce.replace('---', 'Null')
divorce.dropna(how='all', inplace=True)              #modifying the object
# pivoting table 
divorce = divorce.stack([0]).reset_index()
#print (divorce)
### Renaming the column's name
divorce.rename(columns={divorce.columns[0] : 'State',
                       divorce.columns[1] : 'Year',
                      divorce.columns[2] : 'divorce_rate',
                    }
          , inplace=True)    
# export the dataframe to excel file and save it in a separate file

divorce.to_excel(excel_writer='clean_divorce.xlsx',           #naming the new excel file
                sheet_name='divorce_rate',                            # name of the sheet
                na_rep='null',                                  
                index=False)

  

