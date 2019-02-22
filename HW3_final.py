import pandas
import re


class cleaning_files:
    def housing_rates(self):
        #read the file into python
        housingrates1 = pandas.read_excel('h081.xls',
                                          skiprows=4,  #skip the metadata
                                          header=[0, 1], #make the header columns 0 and 1
                                          skipfooter=56, #skip the second header for 2017 dollars
                                          index_col=[0]) #index at 0

        housingrates1 = housingrates1.stack().stack().reset_index() #stack our data twice and start the index over


        #rename our columns to meaningful headers
        housingrates1.rename(columns={housingrates1.columns[0]: "State",
                                      # These next 5 lines of code rename our column headers for the new excel
                                      housingrates1.columns[1]: "Type",
                                      # we are creating. The inplace true statement assures we don't create a copy but a new file
                                      housingrates1.columns[2]: "Year",
                                      housingrates1.columns[3]: "Values"},
                             inplace=True)

        #remove the numbers in parantheses that coinced with the year values
        housingrates1["Year"].replace(regex=True, inplace=True, to_replace=r'\([0-9]*\)|\([^)]*\)', value=r'')
        # print(housingrates1)


        # remove the new line character from the type column
        housingrates1["Type"].replace(regex=True, inplace=True, to_replace=r'\n', value=r" ")

        #change the year column from an object value to an integer
        housingrates1["Year"] = housingrates1.Year.astype(int)

        # housingrates1.to_excel(excel_writer='housing_rates_cleaned.xls',           # name the excel file "marriage_rates_cleaned"
        # sheet_name='Cleaned_housing_rates',                            # name the sheet "cleaned_marriage_rates"
        # na_rep='null',                                  # treat n/a as null
        # index=False)

        #do the same process as before but begin at the 2017 header in line 59
        housingrates2 = pandas.read_excel('h081.xls',
                                          skiprows=59,
                                          header=[0, 1],
                                          skipfooter=1,
                                          index_col=[0])
        #same as before, just stack twice and reset the index

        housingrates2 = housingrates2.stack().stack().reset_index()

        #rename our column headers
        housingrates2.rename(columns={housingrates2.columns[0]: "State",
                                      # These next 5 lines of code rename our column headers for the new excel
                                      housingrates2.columns[1]: "Type",
                                      # we are creating. The inplace true statement assures we don't create a copy but a new file
                                      housingrates2.columns[2]: "Year",
                                      housingrates2.columns[3]: "Values"},
                             inplace=True)
        #regular expressions to remove weird characters like before
        housingrates2["Type"].replace(regex=True, inplace=True, to_replace=r'\n', value=r" ")
        # regular expressions to remove weird characters like before
        housingrates2["Year"].replace(regex=True, inplace=True, to_replace=r'\([0-9]*\)|\([^)]*\)', value=r'')

        #change year to integer rather than object
        housingrates2["Year"] = housingrates2.Year.astype(int)
        # print(housingrates2)

        #merge our two datafiles into one so we can print as one excel sheet
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
    def migration_clean(self):
        import pandas as pd
        migration = pd.read_excel('Migration.xls',
                                  skiprows=5,
                                  header=0,
                                  skipfooter=14,
                                  na_values='(NA)',
                                  index_col=[0, 1, 2, 3])

        migration.dropna(how='all', inplace=True)
        migration = migration.reset_index()
        new = migration["Mobility period"].str.split(" ", n=1, expand=True)
        migration["Years"] = new[0]
        migration["info"] = new[1]
        migration.drop(columns=["Mobility period"], inplace=True)

        migration.rename(columns={migration.columns[3]: 'Total_diff_res',
                                  migration.columns[4]: 'diff_res_samecounty',
                                  migration.columns[5]: 'diff_res_diff_county',
                                  migration.columns[6]: 'drdc_same_state',
                                  migration.columns[7]: 'drdc_diff_state',
                                  migration.columns[8]: 'movers_from_abroad'}
                         , inplace=True)

        migration = migration.iloc[1:]

        cols = migration.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        cols = cols[-1:] + cols[:-1]
        migration = migration[cols]

        writer = pd.ExcelWriter('migration_clean.xlsx', engine='xlsxwriter')
        migration.to_excel(writer, sheet_name='migration', index=False)
        writer.save()

    def clean_crime_rates(self):
        import pandas as pd

        # opening the  excel file
        crime = pd.read_csv("CrimeStatebyState.csv", index_col=0, encoding='latin-1', error_bad_lines=False)

        # converting from wide to long format
        crime = crime.stack(0).reset_index()
        # renaming the column names
        crime.rename(columns={crime.columns[0]: 'Year',
                              crime.columns[1]: 'Crime_type',
                              crime.columns[2]: 'Total_number'},
                     inplace=True)
        # saving the cleaned file as new_crime.csv
        crime.to_csv(path_or_buf="new_crime.csv", index=False)



final= cleaning_files()
final.housing_rates()
final.marriage_rates()
#final.divorce_rates()
final.migration_clean()
final.clean_crime_rates()
