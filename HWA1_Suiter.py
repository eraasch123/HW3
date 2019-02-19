import pandas
import csv, sqlite3

marriagerates=pandas.read_excel('dirty_marriage_rates.xlsx',
                                skiprows=0, #skip no rows at the beggining because metadata was deleted
                                header=[0,1], # make the header the first and second
                                skipfooter=8, #skip the final 8 lines in the excel file
                                na_values='---', #this line accounts for empty values and how theyre represented in the excel file
                                usecols=22, # Use all 22 columns included in the excel file
                                index_cols=[0]) #start our index using column 0

marriagerates=marriagerates.stack([0,1]).reset_index() #This line stacks our excel in long format using columns 0 and 1 as our headers
# marriagerates.columns={'Year', 'ok',"Val","Value"} #this was just some test code
#marriagerates= marriagerates.set_index('ok') #test code
marriagerates.rename(columns={marriagerates.columns[0] : "State", #These next 5 lines of code rename our column headers for the new excel
                     marriagerates.columns[1] : "Marriage rates",#we are creating. The inplace true statement assures we don't create a copy but a new file
                     marriagerates.columns[2] : "Year",
                     marriagerates.columns[3] : "Marriage rate"},
                     inplace=True)

#marriagerates=marriagerates.dropna(how='all')
marriagerates.drop(columns=['Marriage rates'], inplace=True) #when we reshaped our data an extra comlumn called marriage rates was included in each
print(marriagerates.to_string()) #row but was not necessary. So we drop that column



marriagerates.to_excel(excel_writer='marriage_rates_cleaned.xls',           # name the excel file "marriage_rates_cleaned"
                sheet_name='Cleaned_marriage_rates',                            # name the sheet "cleaned_marriage_rates"
                na_rep='null',                                  # treat n/a as null
                index=False)

conn = sqlite3.connect('marriage_rates_cleaned.db')                    #create the database and save it in a variable
marriagerates.to_sql(con=conn,                                          #connect the database to sql, name it and specify what to do if it already exists
                name='MarriageRates',
                if_exists='replace')
cursor = conn.cursor()                                                     # create a cursor so we can run an sql command in the next line
cursor.execute("SELECT * FROM MarriageRates;")                             #select all of the info from our database marriagerates
database = cursor.fetchall()                                                #save the results as a variable
#print(database)                                                            #print the variable to see our database
