import time
import pandas as pd
import numpy as np


def get_month():
    """
    Asks month to specify a day to analyze.

    Returns:
        (str) month - name of the month to analyze
    """
    dict_months = {1: 'January', 2: 'February', 3: 'March',
                   4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'All'}

    while True:
        try:
            print('Choose month?\n')

            tuple_months = '1. January', '2. February', '3. March', '4. April', '5. May', '6. June', '7. July', '8. All'
            for tuple_month in tuple_months:
                print(tuple_month)

            user_month_id = int(input('Insert month number: '))
            print('\nMonth you have select: {0}\n'.format(dict_months[user_month_id]))

            return dict_months[user_month_id].lower()

        except:
            print('\nnot flexible\n')


def get_day():
    """
    Asks user to specify a day to analyze.

    Returns:
        (str) day - name of the day to analyze
    """
    dict_days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday',
                 5: 'Thursday', 6: 'Friday', 7: 'Saturday', 8: 'All'}

    while True:
        try:
            print('Choose day?\n')

            tuple_days = '1. Sunday', '2. Monday', '3. Tuesday', '4. Wednesday', '5. Thursday', '6. Friday', '7. Saturday', '8. All'
            for tuple_day in tuple_days:
                print(tuple_day)

            user_day_id = int(input('Insert day number: '))
            print('\nDay you have select: {0}\n'.format(dict_days[user_day_id]))

            return dict_days[user_day_id].lower()

        except:
            print('\nnot flexible\n')


def get_city():
    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze
    """
    dict_cities = {1: 'Chicago', 2: 'New York', 3: 'Washington'}

    while True:
        try:
            print('I think i can get you data for\n')

            tuple_cities = '1. Chicago', '2. New York', '3. Washington'
            for tuple_city in tuple_cities:
                print(tuple_city)

            user_city_id = int(input('Insert city number: '))
            print('\nCity you have select: {0}\n'.format(dict_cities[user_city_id]))

            return dict_cities[user_city_id].lower()

        except:
            print('\nnot flexible\n')


def search():
    """
    Asks user to specify a search approach to analyze.

    Returns:
        (str) filter - name of the search to use
    """
    dict_filters = {1: 'Month', 2: 'Day', 3: 'both', 4: 'None'}

    while True:
        try:
            print('You can make a choice by\n')

            tuple_filters = '1. Month', '2. Day', '3. Both', '4. None'
            for tuple_filter in tuple_filters:
                print(tuple_filter)

            user_filter_id = int(input('Insert filter number: '))
            print('\nFilter choice you have select: {0}\n'.format(
                dict_filters[user_filter_id]))

            return dict_filters[user_filter_id].lower()

        except:
            print('\nnot flexible\n')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = get_city()

    # dispaly filter option list for the user and asks user to input a vaild selection from the list
    filter = search()

    month = 'all'
    day = 'all'

    if filter == 'month':
        # get user input for month (all, january, february, ... , june)
        month = get_month()
    elif filter == 'day':
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = get_day()
    elif filter == 'both':
        month = get_month()
        day = get_day()

    print('-'*40)
    return city, month, day

# Loading the data


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

    city_data = {'chicago': 'chicago.csv',
                 'new york': 'new_york_city.csv',
                 'washington': 'washington.csv'}

    df = pd.read_csv(city_data[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['start_end_station'] = df['Start Station']+' --> '+df['End Station']

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

# time stats


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is {0}.'.format(common_month))

    # display the most common day of week
    common_week = df['day_of_week'].mode()[0]
    print('The most common day of week is {0}.'.format(common_week))

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is {0}.'.format(common_start_hour))
    print('\nThis will take %s seconds.' % (time.time() - start_time))
    print('-'*40)

# station stats


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common Start Station is {0}.'.format(common_start_station))

    # display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print('The most common End Station is {0}.'.format(common_end_station))

    # display most frequent combination of start station and end station trip
    most_frequent_combination = df['start_end_station'].mode()[0]
    print('The most frequent combination of start station and end station trip is {0}.'.format(
        most_frequent_combination))

    print('\nThis will take %s seconds.' % (time.time() - start_time))
    print('-'*40)

# trip stats


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_duration = df['Trip Duration'].sum()
    print('The total travel time is {0}.'.format(total_travel_duration))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {0}.'.format(mean_travel_time))

    print('\nThis will take %s seconds.' % (time.time() - start_time))
    print('-'*40)

# user stats


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('The counts of user types is {0}.'.format(count_user_types))

    # Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('The counts of gender is {0}.'.format(count_gender))
    else:
        print('There is no Gender data found')

    # Display earliest, most recent, and most common year of birth

    if "Birth Year" in df.columns:
        common_year_of_birth = df['Birth Year'].mode()[0]
        print('The common year of birth is {0}.'.format(common_year_of_birth))

        recent_year_of_birth = df['Birth Year'].max()
        print("The most recent year of birth is {0}.".format(recent_year_of_birth))

        earliest_year_of_birth = df['Birth Year'].min()
        print('The earliest year of birth is {0}.'.format(earliest_year_of_birth))
    else:
        print('There is no Birth Year data found')

    print('\nThis will take %s seconds.' % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nIf you would like to restart? Insert yes or no.\n')
        if restart.lower() != 'yes':
            break

        rows=0
        # The user can replay this option 100 times
        for x in range(100):
            print(df[rows:rows + 5])
            more_rows = input('\nMore individual trips? (yes/no).\n')
            rows += 5
            if more_rows.lower() != 'yes':
                break
        restart = input('\nRestart? (yes/no).\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
