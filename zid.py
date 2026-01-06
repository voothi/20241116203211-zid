import datetime
import pyperclip

# Get the current time in the required format
current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

# Copy the string to the clipboard
pyperclip.copy(current_time)

# Print the string to the screen
print(current_time)
