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
<<<<<<< HEAD
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
=======
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington)
>>>>>>> documentation
    while True:
        city = input("Enter a city to explore: Chicago, New York City, or Washington? ").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Please enter a valid city!")
    # get user input for month (all, january, february, ... , june)
<<<<<<< HEAD
    while True:    
=======
    while True:
>>>>>>> documentation
        month = input("Enter any of the first six months of the year, or enter 'all' for all six months: ").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Please enter a valid month!")
    # get user input for day of week (all, monday, tuesday, ... sunday)
<<<<<<< HEAD
    while True:    
=======
    while True:
>>>>>>> documentation
        day = input("Enter a day for which you would like to explore the data, or enter 'all' for all days: ").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Please enter a valid day!")
<<<<<<< HEAD
    
=======

>>>>>>> documentation
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is", most_common_month, "\n")

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is", most_common_day, "\n")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common start hour is", most_common_hour, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is", most_used_start_station, "\n")

    # display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is", most_used_end_station, "\n")

    # display most frequent combination of start station and end station trip
    df['station_combination'] = df['Start Station'] + " " + df['End Station']
    most_common_trip = df['station_combination'].mode()[0]
    print("The most frequent combination of start station and end station trip is", most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is", total_travel_time, "\n")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean time is", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    user_types_count = df.groupby(['User Type'])['User Type'].count()
    print(user_types_count, "\n")

    # display counts of gender
    try:
        gender_count = df.groupby(['Gender'])['Gender'].count()
        print(gender_count)
    except KeyError:
        print("Gender data is not available")
<<<<<<< HEAD
        
    # display earliest, most recent, and most common year of birth
    try:       
=======

    # display earliest, most recent, and most common year of birth
    try:
>>>>>>> documentation
        # most recent year of birth
        most_recent_birth_year = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        print("The most recent year of birth is", most_recent_birth_year, "\n")
        # earliest year of birth
        earliest_birth_year = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        print("The earliest year of birth is", earliest_birth_year, "\n")
        # most common year of birth
<<<<<<< HEAD
        most_common_birth_year = df['Birth Year'].mode()[0]          
=======
        most_common_birth_year = df['Birth Year'].mode()[0]
>>>>>>> documentation
        print("The most common year of birth is", most_common_birth_year, "\n")
    except:
        print("Birth Year data is not available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # display 5 rows to the user when they ask for raw data
        rows = 0
        count = 0
        while True:
            rawdata = input('\nWould you like to display 5 rows of the dataset? Enter yes or no.\n').lower()
            if rawdata == 'yes':
                print(df.iloc[count:rows+5])
                rows +=5
                count +=5
<<<<<<< HEAD
            elif rawdata == 'no':
                break
            else:
                print('\nInvalid entry. Please enter yes or no.')
        
=======
            else:
                break

>>>>>>> documentation
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> documentation
