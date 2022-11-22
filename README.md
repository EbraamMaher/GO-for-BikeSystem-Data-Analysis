# GO-for-BikeSystem-Data-Analysis

# (Ford Gobike System Data)
## by (Ebraam Maher)


## Dataset

> Ford GO bike system data set provides data of 3 categories:
1) time related data: whole trip durarion , start & end time

2)station related data: start & end stations name, start & end stations location (latitude longitude )

3)client's related data like date of birth, gender, user type (Subscriber or not).
dataset dimension (183412, 16) where it consists of 16 columns ( duration_sec start_time end_time start_station_id start_station_name start_station_latitude start_station_longitude end_station_id end_station_name end_station_latitude end_station_longitude bike_id user_type member_birth_year member_gender bike_share_for_all_trip)


## Summary of Findings

> most common age lies between 25 and 35 years old members and and there is a few above 60 Years old
> Males are the dominant gender
> the most common hours to start the trip is at [7:9] (sunrise) and [16:18] (sunset )
> there is a strong negative relationship between trip duration and age
> males tends to be subscribers compared to females
> at any start hour over the day ,the customers are always have higher trip duration than (subscribers)

## Key Insights for Presentation

> trip duration has a strong relationship with member type if we compare the types w.r.t the start hour ,Customers always tends to have greater trip duration than subscribers.
>trip duration has a strong relationship with member type if we compare the types w.r.t the start hour ,Customers always tends to have greater trip duration than subscribers.


### you can try exploring the data-set using ***bike.py***  to get your insights or check the **exploration_template.ipynb** file to see the visualization of the insight I concluded
