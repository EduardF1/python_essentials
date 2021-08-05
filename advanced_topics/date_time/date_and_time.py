# **********************************************************************************************************
import time

# **********************************************************************************************************
#   print(time.ctime(0))  # get epoch
# print(time.ctime(1000000))  # convert a time expressed in seconds since epoch to a readable string
#                           epoch = date and time from which a computer measures system time
# print(time.time())  # return current seconds since epoch
# print(time.ctime(time.time()))  # get current date & time

# time_object = time.localtime()
# time_object = time.gmtime()  # get time in UTC format
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_str = time.asctime(time_tuple)
# print(time_str)

# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_str = time.mktime(time_tuple)  # convert a time tuple to seconds since epoch
# print(time_str)