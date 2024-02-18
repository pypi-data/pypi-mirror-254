from datetime import datetime

def timestamp():
  # Get the current date and time
  current_datetime = datetime.now()

  # Extract individual components from the current date and time
  year = current_datetime.year
  month = current_datetime.month
  day = current_datetime.day
  hour = current_datetime.hour
  minute = current_datetime.minute
  second = current_datetime.second

  # Create a new datetime object with the extracted components
  my_date = datetime(year, month, day, hour, minute, second)

  return my_date
print(timestamp())