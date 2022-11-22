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
        (str) city  - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day   - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print("please,Enter the name of the city to analyze:\n")
        city=input("chicago   OR    new york city   OR   whashington\t").lower()
       
        
        if city in CITY_DATA.keys() :
            break
        else: print("Error,your input is not a  right name of the city")
    
    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']    

    while True:
        month=input("please,Enter month name, or 'all' to apply no month filter:\n choose from january, february, march, april, may, june \t").lower()
        if month in months or month=='all':
            break
        else: print("Error,your input is not right ")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
    while True:
        day=input("please,Enter month name, or 'all' to apply no day filter:\n choose from saturday, sunday, monday, tuesday, wednesday, thursday, friday\t")
        if day in days or day=='all':
           
            break
        else: 
            print("Error,your input is not right ")


    print('-'*40)
    return city, month, day
    
    
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city  - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day   - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df                = pd.read_csv(CITY_DATA[city])
    df['Start Time']  = pd.to_datetime(df['Start Time'])
    #print("1\n",df)
    
    df['month']       = df['Start Time'].dt.month
    #print("2\n",df)
    
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #print("3\n",df)
    
    df['start_hour' ] = df['Start Time'].dt.hour
    #print("4\n",df)
    
    #filteration by month
    if  month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month  = months.index(month) + 1
        df     = df[df['month'] == month]

    #filteration by day    
    if day != 'all':
         
         df  = df[df['day_of_week'] == day.title()]



    return df

def display_data(df):
    '''Display 5 rows of the data each time upon the user's request'''
    display=input("Do you need to see 5 lines from the data ?(yes / no)".lower())
    c=0     #counter to change the lines of the data to be printed upon  user's request
    print("OK")
    while display !='no' :    
        if  display == 'yes':
            print(df.iloc[c:c+5])
            c+=5
        else: print("we cannot undersatand your input")  #when the user gives wrong input(ex. typo) 
        display=input("need to see more 5 lines ?(yes / no)".lower())

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
   
 
    print('most common month: ',df['month'].mode()[0])
 
    # display the most common day of week
    print('most common day  : ',df['day_of_week'].mode()[0])

    # display the most common start hour
    print('most common hour : ',df['start_hour'].mode()[0])
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    ##for chicago: 6 Tuesday 17

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('most commonly used Start satation : ',df['Start Station'].mode()[0])
    # display most commonly used end station
    print('most commonly used End satation   : ',df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Start to End']=df['Start Station']+' TO '+df['End Station']
    print('most frequent combination of start station and end station trip :',df['Start to End'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time:',df['Trip Duration'].sum())

    # display mean travel time
    print('mean  travel time:',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # Display counts of user types
    print('counts of user types:\n',df['User Type'].value_counts())

    if 'Gender' in df.columns:
        # Display counts of gender
        print('\ncounts of gender types:\n',df['Gender'].value_counts())
    else:
        print('\nGender is not included in this city data')
    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        most_common_birth_year = df['Birth Year'].mode()[0]
        most_recent_birth_year = df['Birth Year'].max()
        earliest_birth_year    = df['Birth Year'].min()
        print('\nmost common birth year:{}\nmost recent_birth year:{}\nearliest birth year\t:{}'.format(most_common_birth_year,most_recent_birth_year,earliest_birth_year))
    else:
        print('\nBirth Year is not included in this city data')    
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
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
