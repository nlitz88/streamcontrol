



# Essentially, I just want this to be a simple script that contacts some sort of time server to determine the sunset time every day, or use a library call
# that references some sort of stored calendar (as this should be something that is predictable, at least roughly. This needn't be exact).

# Also, basically want this to act like a daemon. At every interval of time, just check to see if the current time is the next designated time.

# As far as the stream scheduler goes, while I don't think this needs to be very complex, I think a cool way to design would be to include stream_intervals.
# That is, when you run the service, you call the script with multiple start, end times, 

# OR just keep it simple to start: make it poll for the current time.
# if it's a new day, then go get the sunset/sunrise time for that day.
# Then, if the time is the sunrise time, turn on the stream.
# If the time is the sunset time, turn off the stream.
# Otherwise, don't do anything.

# This can be generalized to:
# If the current time is nearest time (start point at the top of the start point stack) then start the stream.
# If the current time is the nearest stop time (stop time at the top of the stop time stack) then stop the stream.

# If they provide sunrise:sunset as a range, then it'll add the time of sunrise to the startpoint stack and the sunset time to the stoppoint stack.

# It would be expected that the user does not overlap time intervals; otherwise, this would result in the stream ending prematurely, or other undefined behavior.
# The user would define the start and stop times for every day in arguments for running the script, either in the form of arguments or a file, with intervals
# on each line like: 
# 2:00-3:00,
# sunrise-sunset,
# 23:00-23:30


# AND, don't even necessarily have to set this up to be an infinite loop; could just use the built in linux timer feature from systemd. However, that
# would kind of make it impossible to use on Windows right out of the box.