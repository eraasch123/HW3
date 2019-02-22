import pandas as pd
#importing the excel file
migration = pd.read_excel('Migration.xlsx',
                       skiprows=5, #skip 1st 5 rows of excel 
                       header=0, #header 
                       skipfooter=14, #skip last 14 rows 
                       na_values='(NA)', #
                       index_col=[0,1,2,3])

#cleaning and reshaping 
migration.dropna(how='all', inplace=True)
migration= migration.reset_index()
new = migration["Mobility period"].str.split(" ", n = 1, expand=True)
migration["Years"] = new[0]
migration["info"] = new[1]
migration.drop(columns=["Mobility period"], inplace=True)
 
#renaming the column name 
migration.rename(columns={migration.columns[3] : 'Total_diff_res',
                       migration.columns[4] : 'diff_res_samecounty',
                       migration.columns[5] : 'diff_res_diff_county',
                       migration.columns[6] : 'drdc_same_state',
                       migration.columns[7] : 'drdc_diff_state',
                       migration.columns[8] : 'movers_from_abroad' }
              , inplace=True)



migration = migration.iloc[1:]

cols = migration.columns.tolist()
cols = cols[-1:] + cols[:-1]
cols = cols[-1:] + cols[:-1]
migration = migration[cols]


#exporting and saving the file 
writer = pd.ExcelWriter('migration_clean.xlsx', engine='xlsxwriter') 
migration.to_excel(writer, sheet_name='migration', index=False)
writer.save()

