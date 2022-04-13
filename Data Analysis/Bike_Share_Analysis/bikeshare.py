import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    city=''
    month=''
    day=''
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Would you like to see data for chicago,new york city or washington')
    is_valid_city =False
    while not is_valid_city:
        city=input().lower()
        if city not in CITY_DATA:
            print('Please select a right city chicago,new york city or washington')
            continue
        else:
            is_valid_city=True
            
    # get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    print("Would you like to filter data with month: 'january', 'february', 'march', 'april', 'may' ,'june' or 'all' for non filter ")
    is_valid_month =False
    while not is_valid_month:
        month=input().lower()
        if not month in months:
            print("Please select a right month: 'january', 'february', 'march', 'april', 'may' ,'june' or 'all' for non filter ")
            continue
        else:
            is_valid_month=True
            
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('Would you like to filter data with day: "monday", "tuesday", "wednesday", "thursday","friday", "saturday", "sunday" or "all" for non filter')
    dayes=["all","monday", "tuesday", "wednesday", "thursday","friday", "saturday", "sunday"]
    is_valid_day =False
    while not is_valid_day:
        day=input().lower()
        if not day in dayes:
            print('Please select a right day: "monday", "tuesday", "wednesday", "thursday","friday", "saturday", "sunday" or "all" for non filter')
            continue
        else:
            is_valid_day=True
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df =pd.read_csv(r'{}'.format(CITY_DATA[city]))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] =df['Start Time'].dt.hour
    if month != 'all':
       
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        
        df = df[df['month']==month]

    
    if day != 'all':
        
        day=day.title()
        df = df[df['day_of_week']==day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    _month_index=df['month'].mode()[0]-1
    
    print(months[_month_index].title())


    # display the most common day of week
    print(df['day_of_week'].mode()[0])

    # display the most common start hour
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)  


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("most commonly used start station is:{} , and count:{}".format(df['Start Station'].mode()[0],df['Start Station'].value_counts().max()))


    # display most commonly used end station
    print("most commonly used end station is:{} , and count:{}".format(df['End Station'].mode()[0],df['End Station'].value_counts().max()))

    # display most frequent combination of start station and end station trip
    
    print("most frequent combination of start station and end station trip is {}".format(df[['Start Station', 'End Station']].mode().loc[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['travel_time']=pd.to_datetime(df['End Time'])-df['Start Time']

    # display total travel time
    print("total travel time : {}".format(df['travel_time'].sum()))


    # display mean travel time
    print("average travel time :{}".format(df['travel_time'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("counts of user types")
    print(df['User Type'].value_counts())


    # Display counts of gender
    
    if 'Gender' in df.columns:
        print("counts of gender")
        print(df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("earliest year of birth :{}".format(df['Birth Year'].min()))
        print("most recent year of birth :{}".format(df['Birth Year'].max()))
        print("most common year of birth :{}".format(df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    print('Do you want to see decribtive statistics ? type "Yes" or any else to cancel')
    _answer=input().title()
    if _answer=="Yes":
        print('Do you want to include categorical data ? type "Yes" or any else to cancel')
        _answer=input().title()
        if _answer=="Yes":
            print(df.describe(include='all'))
        else:
            print(df.describe())
    print('Do you want to see 5 rows of data? type "Yes" or any else to cancel')
    _answer=input().title()
    _rows=5
    while _answer=="Yes":
        print(df.head(_rows))
        print('Do you want to increase 5 rows of data? type "Yes" or any else to cancel')
        _answer=input().title()
        if _answer=="Yes":
            _rows += 5
        else:
            break
            
            
            
           
     
        
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
