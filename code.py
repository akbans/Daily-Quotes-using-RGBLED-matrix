import adafruit_display_text.label
import board
import displayio
import framebufferio
import rgbmatrix
import terminalio
import time
import random
import datetime
from adafruit_bitmap_font import bitmap_font

# Release any previous displays
displayio.release_displays()

# Create the RGB Matrix object
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=1,
    rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
    addr_pins=[board.A5, board.A4, board.A3, board.A2],
    clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1)

# Associate the RGB matrix with a Display
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

# Load the 4x6 font for the header and date
small_font = bitmap_font.load_font("4x6.bdf")

# Function to load quotes from a local text file
def load_quotes(filename):
    try:
        with open(filename, "r") as file:
            quotes = [line.strip() for line in file if line.strip()]
        return quotes
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return ["No quotes available. Please add quotes to the file."]

# Load quotes from the text file
quotes = load_quotes("quotes.txt")

# Function to generate a random color
def get_random_color():
    return random.randint(0, 0xFFFFFF)

# Get the current date and use it to select the quote of the day
def get_quote_of_the_day():
    current_date = datetime.date.today()
    quote_index = current_date.toordinal() % len(quotes)  # Use the date to pick a quote
    return quotes[quote_index]

# Create the "Quote of the Day" header and date
header_text = "Quote of the Day"
current_date = datetime.date.today().strftime("%d %b %Y")  # Format the date
header = adafruit_display_text.label.Label(
    small_font,
    color=0xFFFF00,  # Yellow color
    text=header_text)
header.x = (display.width - header.bounding_box[2]) // 2  # Center align
header.y = 2  # Near the top

date_label = adafruit_display_text.label.Label(
    small_font,
    color=0x00FF00,  # Green color
    text=current_date)
date_label.x = (display.width - date_label.bounding_box[2]) // 2  # Center align
date_label.y = 10  # Below the header

# Create a scrolling label with the quote of the day
current_quote = get_quote_of_the_day()
current_color = get_random_color()
quote_label = adafruit_display_text.label.Label(
    terminalio.FONT,
    color=current_color,
    text=current_quote)
quote_label.x = display.width
quote_label.y = 24  # Centered below the header and date

# Create a display group and add all elements
g = displayio.Group()
g.append(header)
g.append(date_label)
g.append(quote_label)
display.root_group = g

# Scroll function
def scroll(line):
    line.x -= 1  # Move one pixel at a time
    line_width = line.bounding_box[2]
    if line.x < -line_width:
        line.x = display.width  # Reset the position
        return False
    return True

while True:
    scroll(quote_label)
    display.refresh(minimum_frames_per_second=60)
    time.sleep(0.02)  # Short delay for smooth scrolling
