import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# get user input for city (chicago, new york city, washington)
    city = input("choose a city: (chicago, new york city, washington)\t").lower()
    while city not in CITY_DATA:
        print("That's invalid input")
        city = input("choose a city: (chicago, new york city, washington)\t").lower()
# get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("choose a month: (january, february, march, april, may, june, all)\t").lower()
    while month not in months:
        print("That's invalid input")
        month = input("choose a month: (january, february, march, april, may, june, all)\t").lower()
 # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = input("choose a day: (saturday, sunday, monday, tuesday, wednesday, thursday, friday, all)\t").lower()
    while day not in days:
        print("That's invalid input")
        day = input("choose a day: (saturday, sunday, monday, tuesday, wednesday, thursday, friday, all)\t").lower()


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day and hour from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter data by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # filter data by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()
    print("The most common month: {} ".format(common_month[0]))

    # display the most common day of week
    common_day = df['day_of_week'].mode()
    print("The most common day: {} ".format(common_day[0]))


    # display the most common start hour
    common_hour = df['hour'].mode()
    print("The most common hour: {} ".format(common_hour[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    count_of_occurence = df['Start Station'].value_counts()
    print("The most popular start station: {}, Count of occurence: {} ".format(popular_start_station[0], count_of_occurence[0]))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()
    count_of_occurence = df['End Station'].value_counts()
    print("The most popular end station: {}, Count of occurence: {} ".format(popular_end_station[0], count_of_occurence[0]))

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ', ' + df['End Station']
    most_popular_trip = df['trip'].mode()
    count_of_occurence = df['trip'].value_counts()
    print("The most popular trip: {}, Count of occurence: {} ".format(most_popular_trip[0], count_of_occurence[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: {} ".format(total_travel_time))


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: {} ".format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print(user_types)

    # display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts().to_frame()
        print(gender)

    # display earliest, most recent, and most common year of birth
        earlist_year = df['Birth Year'].min()
        print("The earlist year is {} ".format(earlist_year))
        most_recent_year = df['Birth Year'].max()
        print("The most recent year is {} ".format(most_recent_year))
        common_year = df['Birth Year'].mode()
        print("The most common year is {} ".format(common_year[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    """ Ask the users if they want to see the raw data.
    Returns
    df - pandas dataframe containing 5 raw data or more as the users want

    """
    pd.set_option('display.max_columns',200)
    print("\nRaw data is avaliable to check...\n")
    display_raw = input("would you like to see the raw data in chunks of 5 raws, Enter yes or no\n").lower()
    while display_raw not in ('yes', 'no'):
        print("That's invalid input")
        display_raw = input("would you like to see the raw data in chunks of 5 raws, Enter yes or no\n").lower()
    while display_raw == 'yes':
         for chunk in pd.read_csv(CITY_DATA[city], index_col = 0, chunksize = 5):
            print(chunk)
            display_raw = input("would you like to see more raw data in chunks of 5 raws, Enter yes or no\n").lower()
            if display_raw != 'yes':
                print("OK, thank you")
                break
         break

    else:
        print("Ok, thank you")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
