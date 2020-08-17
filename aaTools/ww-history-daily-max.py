'''
Python v3.8 or later
Windows 
DESCRIPTION: Get from Historian the daily maximum values (filtered between two time ranges during days) between two dates.
OWNER: Roan Fourie
REVISION: 0
REVISION DATE: 2020-08-17 (Week 34)
REVISION AUTHOR: Roan Fourie
REVISION DESCRIPTION: 
        Edit the list of tags and edit the dates and times where data must be parsed from.
        Return files with the day's maximum value.
USAGE:   
NOTES:
'''

import pyodbc 
import pandas as pd
import numpy as np

################################################################################
###########################  EDIT START HERE   #################################
################################################################################
tags = ['KDCE_GP2_00INS01_00IQWT320.FA_PV0',
    'KDCE_GP2_00INS02_00IQWT320.FA_PV0',
    'KDCE_GP2_00INS03_00IQWT320.FA_PV0'
]
server_name = 'HISTORIANSERVERNAME'
start_dt = '20200501 05:00:00.000'  # Note the format: '20200501 05:00:00.000'
end_dt = '20200814 05:00:00.000'  # Note the format: '20200814 05:00:00.000'
time_gt = '01:00'  # The begin time ('01:00')
time_lt = '05:30'  # The end time ('05:00')
# The time periods could be removed if you want to check the complete day.
# Remember to take it out of the SQL Query as well.  
################################################################################
###########################  EDIT END HERE   #################################
################################################################################

# Make a SQL connection
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      f"Server={server_name};"
                      "Database=Runtime;"
                      "Trusted_Connection=yes;")


with cnxn:  # using the with statement will automatically close the connections
    cursor = cnxn.cursor()  

    for tag in tags:
        # Query results from SQL into a Pandas Data Frame
        df = pd.read_sql_query(f"SET QUOTED_IDENTIFIER OFF \
        SELECT * FROM OPENQUERY(INSQL, \"SELECT DateTime = convert(nvarchar, DateTime, 21),Time = convert(char(5), DateTime, 108), [{tag}] \
        FROM WideHistory \
        WHERE wwRetrievalMode = 'Cyclic' \
        AND wwResolution = 600000 \
        AND wwQualityRule = 'Extended' \
        AND wwVersion = 'Latest' \
        AND DateTime >= '{start_dt}' \
        AND DateTime <= '{end_dt}'\") \
        where Time >= '{time_gt}' \
        AND Time <= '{time_lt}'", cnxn)

        # Convert DateTime string to date time object type
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        # Get only the date without the time
        df['DT'] = df['DateTime'].dt.date   
        # Group the dates together A-Z then select the one with the largest value in the group
        # This will give the maximum for the day in a new data frame
        df1 = df.groupby(['DT'], sort=False)[tag].max()

        print(df1)

        df1.to_csv(f'{tag}-results.csv', sep=",", encoding='utf-8')

