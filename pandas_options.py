import pandas as pd 
from faker import Faker

# colheader_justify - right - justification of column headers 
# date_dayfirst - False - prints and parses dates with the day first, eg 20/01/2005
# max_columns - 0 - 0 is autodetect, change to None to avoid truncation
# max_colwidth - 50 - maximum width in characters of a column
# max_rows - 60 - maximum number of rows pandas should output
# min_rows - 10 - numbers of rows to show in a truncated repr 
# precision - 6 - floating point output precision in terms of number of places after the decimal
# show_dimensions - truncate - only show table size if truncated. True/False
# width - 80 - width of the display in characters
# chained_assignment - warn - Controls SettingWithCopyWarning: ‘raise’, ‘warn’, or None.

options ={
    'display': {
        'colheader_justify': 'right',
        'date_dayfirst': True,
        'max_columns': None,
        'max_colwidth': -1,
        'max_rows': 60,
        'min_rows': 20,
        'precision': 6,
        'show_dimensions': True,
        'width': 80   
    },
    'mode': {
        'chained_assignment': None,
    }
}

# set all pandas options 
for category, option in options.items():
    for op, value in option.items():
        pd.set_option(f'{category}.{op}', value)


## TEST DATA TO VIEW CHANGES -> remove # if required 
#fake = Faker()
#
#df = pd.DataFrame(columns = ['addr', 
#                             'name', 
#                             'msisdn', 
#                             'code'])
#
#for i in range(100):
#    addr, name, msisdn, pcode = fake.address(), fake.name(), fake.msisdn(), fake.postalcode()
#    df.loc[len(df)] = [addr, name, msisdn, pcode]
#    
#print(df)