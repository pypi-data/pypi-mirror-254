from questrade_api import Questrade
import pandas as pd
import numpy as np
from datetime import date,timedelta

def connect_questrade(token=None):
    # First try and see if a token already exists
    try:
        q = Questrade()
    except:
        q = Questrade(refresh_token=token)
    print("Questrade time is:", q.time)
    print("Successfully Connected to Questrade")
    return q

def get_account_numbers_list(q,account_type='TFSA'):
    df_Accounts=pd.DataFrame(q.accounts['accounts'])
    return df_Accounts[df_Accounts.type == account_type].number.tolist()


def create_date_list(start,end):
    date_range=pd.date_range(start, end, freq='M',)
    print(date_range)
    return date_range

def contr_start_year(birthyear=1990):
    contr_start_year=2009
    year_18=birthyear+18
    if year_18>2009:
        contr_start_year=year_18
    return contr_start_year

def create_df(start='2009-01-01', end=str(date.today() + timedelta(days=30)), account_type='TFSA',token=None):
    q = connect_questrade(token)
    # Return the account list and Questrade Object which will be reused to grab the activity
    account_list= get_account_numbers_list(q, account_type)
    print(account_type, 'account list:', account_list)
    date_range = create_date_list(start, end)
    # create empty dataframe
    df = pd.DataFrame()
    for account_num in account_list:
        print(
            f"grabbing activity from {date_range[0]} to {date_range[-1]} for {account_type}: {account_num}. Completed {int(account_list.index(account_num) * 100 / len(account_list))} % ")
        for dt in date_range:
            # print(f"grabbing activity from month {date}")
            # if the month is January-- print the year and the completion %
            if dt.month == 1:
                print(f'Processing {dt.year} for account {account_num}')
            array = q.account_activities(account_num, startTime=f"{dt.replace(day=1).date()}T00:00:00-0",
                                         endTime=f"{dt.date()}T00:00:00-0")
            # convert Array to dataframe
            df1 = pd.DataFrame(array['activities'])
            if len(df1) > 0:
                # Filter for Withdrawal and Contributions
                df2 = df1.loc[(df1['action'] == 'CON') | (df1['action'] == 'WDR')]
                # Add A new Column with Account Number
                df2.insert(0, 'Account_Number', account_num)
                # Add Year
                df2.insert(1, 'Year', dt.date().year)
                # Append this dataframe to the master dataframe
                df = pd.concat([df, df2])

    print('Grabbing Activity Completed-100%')
    # Fix the Withdrawals that are Zero
    # This happens when the Withdrawal was In Kind- not cash withdrawal
    try:
        df.loc[:, 'netAmount'] = np.where(df.netAmount == 0, np.where(df.currency == 'CAD',
                                                                      df.description.str.split(pat='MARKET VALUE',
                                                                                               expand=True)[1],
                                                                      df.description.str.split(pat='CNV@', expand=True)[
                                                                          1].str.split(expand=True)[1]), df.netAmount)
    finally:
        # Fix the netAmount to remove the $ and the commas
        df.loc[:, 'netAmount'] = df[['netAmount']].replace('[\$,]', '', regex=True).astype(float)

        # Force the withdrawals to be negative values
        df.loc[:, 'netAmount'] = np.where(df.action == 'WDR', -1 * df.netAmount.abs(), df.netAmount)
        return df

TFSA_dollar_limit_dict={2009:5000
,2010:5000
,2011:5000
,2012:5000
,2013:5500
,2014:5500
,2015:10000
,2016:5500
,2017:5500
,2018:5500
,2019:6000
,2020:6000
,2021:6000
,2022:6000
,2023:6500
,2024:7000
,2025:7000
,2026:7000
,2027:7000
,2028:7000
}

df_TFSA_limit=pd.DataFrame(TFSA_dollar_limit_dict.items(),columns=['year','limit'])

#Create this function so that the user can return a dataframe with the TFSA limit from every year
def df_tfsa_limit():
    df_tfsa_limit=pd.DataFrame(TFSA_dollar_limit_dict.items(),columns=['year','limit'])
    return df_tfsa_limit

##Need a function that gets your contribution room based on your birthyear
def max_contr_room_Limit(birthyear=1900,end_yr=date.today().year):
    start_year=contr_start_year(birthyear)
    limit=df_TFSA_limit[(df_TFSA_limit.year>=start_year) & (df_TFSA_limit.year<=end_yr)]['limit'].sum()
    return limit

def print_summary(df):
    today = date.today()
    current_contr_room = df.loc[df['Year'] == today.year].Current_Contr_Room.values[0]
    next_year_contr_room = df.loc[df['Year'] == today.year + 1].Current_Contr_Room.values[0]
    print("Today's date:", today)
    print(f"Your current contribution room is: ${current_contr_room}")
    print(f"Next Year's Contribution room on Jan 1 {today.year + 1} is:  ${next_year_contr_room}")
    return  current_contr_room,next_year_contr_room


# Add optional arguments here
## given is the contribution room and year from the CRA
def contribution_room(given_year=None, given_contr_room=None, open_year=2009, birth_year=1990, token=None):
    contr_start_year1 = contr_start_year(birth_year)

    if given_year is None or given_contr_room is None:
        given_year = None
        given_contr_room = None

    if given_year != None:
        start_year = given_year
        start_contr_room = given_contr_room
    # If they inputted a valid open_year use the open year
    elif open_year >= 2009:
        start_year = open_year
        start_contr_room = max_contr_room_Limit(birth_year, start_year)
    # If the user did not input anything assume they are were born before 1990
    ## and start year is 2009
    else:
        start_year = contr_start_year1
        start_contr_room = max_contr_room_Limit(birth_year, start_year)

    print(f'start_year is {start_year}')
    #Raise error if start year is before 2009 or After the current year
    if (start_year < 2009) or (start_year > date.today().year):
        raise Exception('given year or open year is not Valid!')

    ### Get the data with create_df
    if start_year == 2009:
        print('WARNING: A valid year was not input as open_year or given_year. THIS WILL TAKE A VERY LONG TIME.')
    df = create_df(start=(str(start_year) + '-01-01'), token=token)
    df1 = df.groupby(['Year', 'type'])['netAmount'].sum().reset_index()

    df2 = df1.pivot_table(index='Year', columns='type', values='netAmount').reset_index()
    # If Deposits or withdrawals don't exist add it now
    df2.loc[:, 'Deposits'] = df2.get('Deposits', 0)
    df2.loc[:, 'Withdrawals'] = df2.get('Withdrawals', 0)

    # first thing is limit the df to the year that was given
    df3 = df2.reset_index(drop=True)

    # Insert enough rows so that there is one row for every year until next year
    # this will fix if they had no activity in a year.
    b = pd.DataFrame({'Year': [x for x in range(start_year, date.today().year + 2)]})
    df4 = pd.merge(left=df3, right=b, on='Year', how='outer').fillna(0).sort_values(by='Year').reset_index(drop=True)

    # Add the Given Contribution Room on January 1st
    # first make a new column with zeros
    df4.insert(0, 'Contr_Room_Jan1', 0)
    # Update the value in one cell
    # TO DO need to fix this in case the given contribution room does not match the date range that you have for the dataframe
    # Update Contr room on Jan 1 to be the given value
    df4.loc[:, 'Contr_Room_Jan1'] = np.where(df4.Year == start_year, start_contr_room, df4.Contr_Room_Jan1)

    # Add a new Column 'New Year Dollar limit"
    df4.insert(0, 'New_Year_Dollar_Limit', df4['Year'].map(TFSA_dollar_limit_dict))

    # Calculate Contr Room on Jan 1
    for i in range(1, len(df4)):
        df4.loc[i, 'Contr_Room_Jan1'] = df4.loc[i - 1, 'Contr_Room_Jan1'] - df4.loc[i - 1, 'Deposits'] - df4.loc[
            i - 1, 'Withdrawals'] + df4.loc[i, 'New_Year_Dollar_Limit']

    ## Calculate the Current Contribution Room
    df4.insert(5, 'Current_Contr_Room', df4.Contr_Room_Jan1 - df4.Deposits)

    ### print summary
    current_contr_room, next_year_contr_room = print_summary(df4)

    return current_contr_room, next_year_contr_room, df4


# Create a function so that if new information is found we can just update the dataframe instead of grabbing the activity again
def update_df(df, given_year=None, given_contr_room=None, birth_year=1990):
    # contr_start_year1=contr_start_year(birth_year)
    # df1=df.copy()
    if given_year is None or given_contr_room is None:
        given_year = df.Year.min()
        given_contr_room = max_contr_room_Limit(birth_year, df.Year.min())

    # print(given_year,given_contr_room)
    df.loc[:, 'Contr_Room_Jan1'] = np.where(df.Year == given_year, given_contr_room, df.Contr_Room_Jan1)

    # Calculate Contr Room on Jan 1
    ### Only update the rows after given_year, so start the range with the index after given_year
    ### If we update all rows, it will overwrite the change we just made above
    for i in range(dfa[dfa.Year == given_year].index[0] + 1, len(df)):
        df.loc[i, 'Contr_Room_Jan1'] = df.loc[i - 1, 'Contr_Room_Jan1'] - df.loc[i - 1, 'Deposits'] - df.loc[
            i - 1, 'Withdrawals'] + df.loc[i, 'New_Year_Dollar_Limit']

    ## Calculate the Current Contribution Room
    df.loc[:, 'Current_Contr_Room'] = df.Contr_Room_Jan1 - df.Deposits

    return df