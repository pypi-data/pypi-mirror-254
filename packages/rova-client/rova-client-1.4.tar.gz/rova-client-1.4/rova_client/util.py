from datetime import datetime

class UniqueIDGenerator:
    def __init__(self):
        self.current = 0
        self.max_val = 2**32 - 1  # Maximum value for 32-bit unsigned integer

    def get_unique_id(self):
        if self.current >= self.max_val:
            raise Exception("Maximum limit of unique IDs reached.")
        self.current += 1
        return self.current

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
