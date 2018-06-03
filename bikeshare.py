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
    
    print('Hello! Let\'s explore some US bikeshare data!\n \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city='NONE'
    
    while(city=='NONE'):
        entry=input('Print the city name to analyse : (Washington , Chicago , New York )\n')
        if (entry.lower() != 'washington')& (entry.lower()!='chicago') & (entry.lower()!='new york'):
            print('invalid city')
        else:
            city=entry
   
    s=input('want to filter data by month enter y/Y  \n ') 
    if(s.lower()=='y'):
        month='NONE'
        while(month=='NONE'):
            mon=input('enter month to be analysed january,february,march , april ,may ,june \n  ')
            month_list=['january','february','march','april','may','june']
            if mon.lower() in month_list:
                month=mon
            else:
                print(' invalid input....enter name of month as asked ...\n')
                
    else:
        month='all'
    p=input('want to filter data by week day  y /Y  \n ')    
    if(p.lower()=='y'):
        day='NONE'
        while(day=='NONE'):
            entry1=input('enter day of week to be analysed sunday , monday , tuesday , wednesday , thursday, friday , saturday... \n ')
            day_list=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
            if entry1.lower() in day_list:
                day=entry1
            else:
                print('Invalid week day entered...give input as asked \n')
                
    else:
        day='all'

            
        


    # TO DO: get user input for month (all, january, february, ... , june)


 # DO: get user input for day of week (all, monday, tuesday, ... sunday)


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
    if city.lower()=='washington':
        df=pd.read_csv('washington.csv')
    elif city.lower()=='chicago':
        df=pd.read_csv('chicago.csv')
    else :
        df=pd.read_csv('new_york_city.csv')
    count=0
    
            
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    
    if(month!='all'):
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]    
    if(day!='all'):
        df=df[df['day_of_week']==day.title()]
        
    
                
            
    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if(month=='all'):
        max_month=df['month'].mode()[0]
        
        count=len(df[df['month']==max_month])
        
        print ('--->The most common month is : {} and count is  : {}' .format(max_month,count ))
        
        
    
    # TO DO: display the most common day of week
    if(day=='all'):
        max_day=df['day_of_week'].mode()[0]
        count1=len(df[df['day_of_week']==max_day])
        print('--->The most common day of week is : {} and count is {}'.format(max_day,count1))
    
    df['Start_Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    count2=len(df[df['hour']==common_hour])
    print('---> The most common hour is: {} and count is : {}'.format(common_hour,count2))
     
    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    count=len(df[df['Start Station']==popular_start_station])
    print('---> The most commonly used start station is:{} and count is: {} '.format(popular_start_station,count))

    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    count1=len(df[df['End Station']==popular_end_station])
    print('---> The most commonly used end station is: {} and count is: {}  '.format(popular_end_station,count1) )

    # TO DO: display most frequent combination of start station and end station trip
    df['start_station_&_end_station']= df['Start Station']+"  to  " + df['End Station'].map(str)
    frequent_combination=df['start_station_&_end_station'].mode()[0]
    count2=len(df[df['start_station_&_end_station']==frequent_combination])
    print('---> The most frequent combination of start and end station trip is : {} \n count is :  {}'.format(frequent_combination,count2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=(df['Trip Duration']).sum()

    # TO DO: display mean travel time

    mean_travel_time= (df['Trip Duration']).mean()
    print('---> Total travel time is : {} seconds'.format(total_travel_time))
    print('---> Mean travel time is : {} seconds'.format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('--->User Types :')
    print(user_types)
    if 'Gender' in df.columns:
        gender_types=df['Gender'].value_counts()
        print('\n--->Gender types :')
        print(gender_types)
    
    # TO DO: Display counts of gender
    if 'Birth Year' in df.columns:
        earliest_year=df['Birth Year'].min()
        count1=len(df[df['Birth Year']==earliest_year])
        print('\n--->The earliest year of birth is : {} and count is  :  {}'.format(earliest_year,count1))
        recent_year=df['Birth Year'].max()
        count2=len(df[df['Birth Year']==recent_year])
        print('--->The most recent year of Birth is : {} and count is :{}'.format(recent_year,count2))
               
        common_year=df['Birth Year'].mode()[0]
        count=len(df[df['Birth Year']==common_year])
        print('--->The most common birth year is  :{} and count is : {}'.format(common_year,count))
    
    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
      
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        n=input('want to see raw data  enter y/Y\n')
        if (n.lower()=='y'): 
            n1='y'
            count=0
            while(n1.lower()=='y'):
                print(df.head(count+5))
                count=count+5
                n1=input(' If you want to see more data ? enter y/Y \n')
        else:
            print(' OKAY ! ')
        
        
        

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
          

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
        
