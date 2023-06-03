import datetime
import ephem
import subprocess
import time

def play_mp3(mp3_file_path):
    # Play the MP3 file using mpg123
    command = "mpg123 " + mp3_file_path
    subprocess.call(command, shell=True)

def set_observer_location(lat, lon):
    # Set the observer's location
    observer = ephem.Observer()
    observer.lat = lat  
    observer.lon = lon  
    return observer

def get_next_full_moon(observer):
    # Calculate the next full moon
    next_full_moon = ephem.localtime(ephem.next_full_moon(ephem.now()))
    return next_full_moon

def get_time_until_full_moon(next_full_moon):
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    # Calculate the time difference until the next full moon
    difference = next_full_moon - current_datetime
    return difference

# Set observer's location to Miami, Florida
observer = set_observer_location('25.7617', '-80.1918')

# Get the next full moon
next_full_moon = get_next_full_moon(observer)

# Print the next full moon time in a user-friendly format
print(f"The upcoming full moon is scheduled for {next_full_moon.strftime('%B %d, %Y')}, at {next_full_moon.strftime('%I:%M:%S %p')}.")

while True:
    # Get the time difference until the next full moon
    time_difference = get_time_until_full_moon(next_full_moon)

    # Check if the time difference is less than or equal to zero, meaning it's the time of the full moon
    if time_difference.total_seconds() <= 0:
        print(f"Playing the MP3 file as it's the full moon on {next_full_moon.strftime('%B %d, %Y')} at {next_full_moon.strftime('%I:%M:%S %p')}.")

        # Replace with the actual path to your MP3 file
        mp3_file_path = '/home/pi/Music/DeclarationOfFaith_JoelOsteen.mp3'
        play_mp3(mp3_file_path)
 
        break

    # Calculate the remaining hours and minutes
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    # Print a statement every minute to show that the script is still running and checking the time
    print(f"The time now is {datetime.datetime.now().strftime('%I:%M:%S %p')}. The upcoming full moon is scheduled for {next_full_moon.strftime('%B %d, %Y')}, at precisely {next_full_moon.strftime('%I:%M:%S %p')}. We have {hours} hours and {minutes} minutes left.")
    
    # Wait for 1 minute before checking the time again
    time.sleep(60)

