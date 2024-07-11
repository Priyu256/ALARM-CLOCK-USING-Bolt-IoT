API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxx'##get your bolt credentials
DEVICE_ID = 'BOLTxxxxxx'   
from boltiot import Bolt
import datetime
import pytz
import time

# Initialize the Bolt device
mybolt = Bolt(API_KEY, DEVICE_ID)

# Digital pin to which the buzzer is connected (use '0' for digital pin 0)
buzzer_pin = '0'

try:
    # Set timezone to Indian Standard Time (IST)
    ist_timezone = pytz.timezone('Asia/Kolkata')

    # Get current time in IST
    now = datetime.datetime.now(ist_timezone)

    # Calculate alarm time for 8:00 PM IST today
    alarm_time = now.replace(hour=20, minute=0, second=0, microsecond=0)

    # If current time is already past 8:00 PM IST, set alarm for tomorrow
    if now.hour > 20 or (now.hour == 20 and now.minute >= 12):
        alarm_time += datetime.timedelta(days=1)

    # Calculate time difference in seconds until alarm time
    time_to_alarm = (alarm_time - now).total_seconds()

    # Wait until alarm time
    time.sleep(time_to_alarm)

    # Turn on the buzzer
    response = mybolt.digitalWrite(buzzer_pin, 'HIGH')
    print("Buzzer turned ON at 8.00 PM IST.")
    print("Eat medicine")

    # Optionally, keep the buzzer on for 60 seconds
    time.sleep(60)  # Adjust duration as needed

    # Turn off the buzzer
    response = mybolt.digitalWrite(buzzer_pin, 'LOW')
    print("Buzzer turned OFF.")

except Exception as e:
    print("Error:", e)

# Ensure the buzzer is turned off at the end
finally:
    try:
        response = mybolt.digitalWrite(buzzer_pin, 'LOW')
        print("Buzzer turned OFF in the finally block.")
    except Exception as e:
        print("Error in finally block:", e)
