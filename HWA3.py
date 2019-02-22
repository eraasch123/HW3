import pandas
import re

housingrates1=pandas.read_excel('h081.xls',
                               skiprows=4,
                               header=[0, 1],
                               skipfooter=56,
                               index_col=[0])




housingrates1=housingrates1.stack().stack().reset_index()


housingrates1.rename(columns={housingrates1.columns[0] : "State", #These next 5 lines of code rename our column headers for the new excel
                     housingrates1.columns[1] : "Type",#we are creating. The inplace true statement assures we don't create a copy but a new file
                     housingrates1.columns[2] : "Year",
                     housingrates1.columns[3] : "Values"},
                     inplace=True)
housingrates1["Type"].replace(regex=True, inplace=True, to_replace=r'\n',value= r" ")

housingrates1["Year"].replace(regex=True, inplace=True, to_replace=r'\([0-9]*\)|\([^)]*\)',value= r'')
#print(housingrates1)

housingrates1["Year"]=housingrates1.Year.astype(int)


#housingrates1.to_excel(excel_writer='housing_rates_cleaned.xls',           # name the excel file "marriage_rates_cleaned"
                #sheet_name='Cleaned_housing_rates',                            # name the sheet "cleaned_marriage_rates"
                #na_rep='null',                                  # treat n/a as null
                #index=False)


housingrates2=pandas.read_excel('h081.xls',
                               skiprows=59,
                               header=[0,1],
                               skipfooter=1,
                               index_col=[0])




housingrates2=housingrates2.stack().stack().reset_index()


housingrates2.rename(columns={housingrates2.columns[0] : "State", #These next 5 lines of code rename our column headers for the new excel
                     housingrates2.columns[1] : "Type",#we are creating. The inplace true statement assures we don't create a copy but a new file
                     housingrates2.columns[2] : "Year",
                     housingrates2.columns[3] : "Values"},
                     inplace=True)
housingrates2["Type"].replace(regex=True, inplace=True, to_replace=r'\n',value= r" ")

housingrates2["Year"].replace(regex=True, inplace=True, to_replace=r'\([0-9]*\)|\([^)]*\)',value= r'')


housingrates2["Year"]=housingrates2.Year.astype(int)
#print(housingrates2)



finaltable= housingrates1.append(housingrates2, ignore_index=True)
print(finaltable)
finaltable.to_excel(excel_writer='housing_rates_cleaned.xls',           # name the excel file "marriage_rates_cleaned"
                sheet_name='Cleaned_housing_rates',                            # name the sheet "cleaned_marriage_rates"
                na_rep='null',                                  # treat n/a as null
                index=False)
