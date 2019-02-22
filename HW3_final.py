import pandas
import re


class cleaning_files:
    def housing_rates(self):
        housingrates1 = pandas.read_excel('h081.xls',
                                          skiprows=4,
                                          header=[0, 1],
                                          skipfooter=56,
                                          index_col=[0])

        housingrates1 = housingrates1.stack().stack().reset_index()

        housingrates1.rename(columns={housingrates1.columns[0]: "State",
                                      # These next 5 lines of code rename our column headers for the new excel
                                      housingrates1.columns[1]: "Type",
                                      # we are creating. The inplace true statement assures we don't create a copy but a new file
                                      housingrates1.columns[2]: "Year",
                                      housingrates1.columns[3]: "Values"},
                             inplace=True)
        housingrates1["Type"].replace(regex=True, inplace=True, to_replace=r'\n', value=r" ")

        housingrates1["Year"].replace(regex=True, inplace=True, to_replace=r'\([0-9]*\)|\([^)]*\)', value=r'')
        # print(housingrates1)

        housingrates1["Year"] = housingrates1.Year.astype(int)

        # housingrates1.to_excel(excel_writer='housing_rates_cleaned.xls',           # name the excel file "marriage_rates_cleaned"
        # sheet_name='Cleaned_housing_rates',                            # name the sheet "cleaned_marriage_rates"
        # na_rep='null',                                  # treat n/a as null
        # index=False)

        housingrates2 = pandas.read_excel('h081.xls',
                                          skiprows=59,
                                          header=[0, 1],
                                          skipfooter=1,
                                          index_col=[0])

        housingrates2 = housingrates2.stack().stack().reset_index()

        housingrates2.rename(columns={housingrates2.columns[0]: "State",
                                      # These next 5 lines of code rename our column headers for the new excel
                                      housingrates2.columns[1]: "Type",
                                      # we are creating. The inplace true statement assures we don't create a copy but a new file
                                      housingrates2.columns[2]: "Year",
                                      housingrates2.columns[3]: "Values"},
                             inplace=True)
        housingrates2["Type"].replace(regex=True, inplace=True, to_replace=r'\n', value=r" ")

        housingrates2["Year"].replace(regex=True, inplace=True, to_replace=r'\([0-9]*\)|\([^)]*\)', value=r'')

        housingrates2["Year"] = housingrates2.Year.astype(int)
        # print(housingrates2)

        finaltable = housingrates1.append(housingrates2, ignore_index=True)
        #print(finaltable)
        finaltable.to_excel(excel_writer='housing_rates_cleaned.xls',  # name the excel file "marriage_rates_cleaned"
                            sheet_name='Cleaned_housing_rates',  # name the sheet "cleaned_marriage_rates"
                            na_rep='null',  # treat n/a as null
                            index=False)
    def marriage_rates(self):

        marriagerates = pandas.read_excel('dirty_marriage_rates.xlsx',
                                          skiprows=0,  # skip no rows at the beggining because metadata was deleted
                                          header=[0, 1],  # make the header the first and second
                                          skipfooter=8,  # skip the final 8 lines in the excel file
                                          na_values='---',
                                          # this line accounts for empty values and how theyre represented in the excel file
                                          usecols=22,  # Use all 22 columns included in the excel file
                                          index_cols=[0])  # start our index using column 0

        marriagerates = marriagerates.stack(
            [0, 1]).reset_index()  # This line stacks our excel in long format using columns 0 and 1 as our headers
        # marriagerates.columns={'Year', 'ok',"Val","Value"} #this was just some test code
        # marriagerates= marriagerates.set_index('ok') #test code
        marriagerates.rename(columns={marriagerates.columns[0]: "State",
                                      # These next 5 lines of code rename our column headers for the new excel
                                      marriagerates.columns[1]: "Marriage rates",
                                      # we are creating. The inplace true statement assures we don't create a copy but a new file
                                      marriagerates.columns[2]: "Year",
                                      marriagerates.columns[3]: "Marriage rate"},
                             inplace=True)

        # marriagerates=marriagerates.dropna(how='all')
        marriagerates.drop(columns=['Marriage rates'],
                           inplace=True)  # when we reshaped our data an extra comlumn called marriage rates was included in each
        #print(marriagerates.to_string())  # row but was not necessary. So we drop that column

        marriagerates.to_excel(excel_writer='marriage_rates_cleaned.xls',
                               # name the excel file "marriage_rates_cleaned"
                               sheet_name='Cleaned_marriage_rates',  # name the sheet "cleaned_marriage_rates"
                               na_rep='null',  # treat n/a as null
                               index=False)
    def divorce_rates(self):
        import pandas as pd
        # reading the data in python
        divorce = pd.read_excel('divorce.xlsx',
                                skiprows=5,
                                header=[0],  # skipping the header
                                skipfooter=4,  # cleaning the footer
                                # na_values='---', #null values
                                usecols=22,
                                # all the columns that we need from the dirty excel file
                                index_col=[0])

        # dropping empty rows
        # divorce.drop(divorce.index[0])
        divorce = divorce.replace('---', 'Null')
        divorce.dropna(how='all', inplace=True)  # modifying the object
        # pivoting table
        divorce = divorce.stack([0]).reset_index()
        # print (divorce)
        ### Renaming the column's name
        divorce.rename(columns={divorce.columns[0]: 'State',
                                divorce.columns[1]: 'Year',
                                divorce.columns[2]: 'divorce_rate',
                                }
                       , inplace=True)
        # export the dataframe to excel file and save it in a separate file

        divorce.to_excel(excel_writer='clean_divorce.xlsx',  # naming the new excel file
                         sheet_name='divorce_rate',  # name of the sheet
                         na_rep='null',
                         index=False)

final= cleaning_files()
final.housing_rates()
final.marriage_rates()
final.divorce_rates()