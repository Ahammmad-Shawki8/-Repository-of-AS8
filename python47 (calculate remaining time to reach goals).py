# In this module, we will write a program which will estimate how long time we need to reach our different goals.
# We are going to write 3 script to solve 3 different problems:
    # first script will be calculate monthly progress toward a goal
    # second script will be calculate weekly progress toward a goal
    # third script will be calculate daily progress toward a goal


# we need to use the datetime and calendar module.
import datetime
import calendar

# for first problem, we will calculate the number of months it would take to pay of a credit card.
# here we have some constances related to credit card.
balance = 5000
interest_rate = 13 * 0.01
monthly_payment = 500

# now lest write script that uses this information to pay our credit card.
# when we pay off a credit card, we usually make payment at the first of the month or towards the end of the month.
# So, we need to specify some date.
today = datetime.date.today()
# now we need to fiure out the first day of the next month.
# we need to take the remaining days left in the current month and add those to the current day.
# to do this, we need to know that how many days in each month,
# and to get this we can use the calender module.

# monthrange() method takes year and month as an argument, and return the first day of that month and also the number of days in that month.
# and it also works for leap years too.
month_info = calendar.monthrange(today.year,today.month)
# this will return a tuple.
# lets print this out.
print(month_info)
# in python, days of the week starts with monday(0), then tuesday(1) .... 
# so first value is that the day of week in which the first day of that month falls on.
# the second value is the total days in that month, so we nned to grab that.
days_in_current_month = month_info[1]
print(days_in_current_month)

# now if we wanted to advanced to the first of the next month, then we can just add the difference of days that are left.
days_till_end_of_month = days_in_current_month - today.day
print(days_till_end_of_month)

# now we need to add this date to todays date so that we can carried over to the next month.
# for adding dates, we can use time deltas.

start_date = today  + datetime.timedelta(days = days_till_end_of_month + 1)
# we have to add one day because otherwise that will take us to the end of the month.
print(start_date)
# we can see that we do get the first day of the next month.

# now we will create another variable here called end_date which we initially set to start_date, 
# but we will incriment that end_date throughout this script. 
end_date = start_date

# now we will see how long it would take to pay off our balance.
# so lets create a while loop

while balance  > 0:
    # first we need to add the interest that will accumulate form the previous month.
    # since the interest rate is annual we need to divide by 12.
    interest_charge = (interest_rate/12) * balance
    balance += interest_charge
    # now we need to substract the monthly payment
    balance -= monthly_payment
    # lets round the balance to two decimal places.
    balance = round(balance,2)
    # if we pay off our balance then we dont want our balance to become negative.
    if balance < 0:
        balance = 0

    # we can compress the previous 3 line of code into 1 line by turnery operator.
    # balance = 0 if balance < 0 else round(balance,2) 

    # now we need to incriment to the next month if the balance hasn't reach ed zero yet.
    print(end_date, balance)
    # now to forward a month, we can just add the number of days of the month to the end_date.
    month_info = calendar.monthrange(end_date.year,end_date.month)
    days_in_current_month = month_info[1]
    end_date += datetime.timedelta(days = days_in_current_month)

    # we always have to become careful when we use a while loop, because there is always a chance that we can stuck in a infinite loop.
    # for example, if our monthly_poayment < interest_charge, then we will never be able to pay off our balance.
    # so, lets run our code.



# now lets move to the next script.
# here we will calculate the number of weeks we need to lose certain amount of kg's to get in a better shape.

# we only need to import datetime only.
import datetime
# just like previous script we need to have few constances.
current_weight = 71
goal_weight = 60
avg_kgs_week = 0.6

start_date = datetime.date.today()
end_date = start_date

# now lets create our loop:
while current_weight > goal_weight:
    end_date += datetime.timedelta(days = 7)
    current_weight -= avg_kgs_week

print(end_date)
print(f"Reached goal in {(end_date-start_date).days // 7} weeks")


# now lets move to next script
# we will calculate days to reach certain subscribers goal

# here we have to import datetime and math module
import datetime
import math

# just like previous two script we need to have few constances.
goal_subs = 100_000
current_subs = 85_000
subs_to_go = goal_subs - current_subs
avg_subs_day = 200 

days_to_go = math.ceil(subs_to_go/avg_subs_day)

today = datetime.date.today()
end_date = today + datetime.timedelta(days = days_to_go)
print(end_date)

# so, it is kind of fun to write this short little scripts and calculate the remaining time to reach our goals
# we can make more complicated scripts if we like.
# for example, we can add expexted monthly growth or something like that.
# we can create this type of short scripts to solve our real world problem,
# it is a good practice for become an expert programmer.