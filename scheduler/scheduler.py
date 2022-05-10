from time import sleep
from datetime import datetime
import pytz
from suntime import Sun
from geopy.geocoders import Nominatim

sleep_interval = 1        # Sleep interval in seconds

# start_queue = {}
# stop_queue = {}

# Get latitude and longitude of current location.
geolocator = Nominatim(user_agent="chirp")
# Setup location (make this configurable via command line arguments).
address = "pittsburgh pa"
location = geolocator.geocode(address)

# Extract latitude and longitude.
latitude = location.latitude
longitude = location.longitude
sun = Sun(latitude, longitude)

# Then, get the current date that will be used to compute the sunrise/sunset times.
current_date = datetime.now().date()
sun_rise = sun.get_local_sunrise_time(current_date)
sun_set = sun.get_local_sunset_time(current_date)
# NOTE: these times are returned in UTC time (No daylight savings time considered, right! We're just concerned with where the Sun is!).

# # Convert these times to configurable time zone. For now, just hardcoded to EST. Just for readability; NOT for utili
# sun_rise_est = sun_rise.astimezone(pytz.timezone('US/Eastern'))
# sun_set_est = sun_set.astimezone(pytz.timezone('US/Eastern'))
# print("Sunrise: ", sun_rise_est.strftime('%H:%M'))
# print("Sunset: ", sun_set_est.strftime('%H:%M'))

# Store the last date.
last_date = datetime.now().date()

while(True):

    # Get current_time as time object.
    current_date = datetime.now().date()
    # Check if it's a new day. If so, update last_date, and get sunset/sunrise times.
    if(current_date != last_date):
        # Set the new last_date.
        last_date = current_date
        # Update the sun_rise and sun_set times for this new day.
        sun_rise = sun.get_local_sunrise_time(current_date)
        sun_set = sun.get_local_sunset_time(current_date)

    # Now, get the current time and determine if an action needs to be taken.
    current_time = datetime.now().time()


    ## NOTE: NEED TO ADD THE CONDITION THAT THE STREAM ISN'T ALREADY STARTED!!! (EITHER POLL OBS OR SET A VARIABLE?)
    if(current_time >= sun_rise.time() and current_time < sun_set.time()):

        # Start the stream!
        print("Time: xxxx Starting the stream!")
    
    elif(current_time >= sun_set.time()):
        # STOP THE STREAM
        print("Stopping the stream!")

    # Otherwise, do nothing!
    else:
        print("Nothing to do. Stream Status: ??")

    sleep(sleep_interval)