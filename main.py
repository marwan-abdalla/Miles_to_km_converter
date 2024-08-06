from tkinter import *


# Function to convert miles to kilometers
def miles_to_km():
    number = int(miles_input.get())
    converted_number = (number * 1.6)
    kilometer_label.config(text=converted_number)


# Set up the main window
window = Tk()

window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Input for miles
miles_input = Entry(width=10)
miles_input.grid(column=2, row=2)

# Label for Miles
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=2)

# Label for "is equal to"
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=3)

# Label for kilometers result
kilometer_result_label = Label(text="Km")
kilometer_result_label.grid(column=3, row=3)

# Label to display the converted number
kilometer_label = Label(text="0")
kilometer_label.grid(column=2, row=3)

# Button to trigger the conversion
calculate_button = Button(text="calculate", command=miles_to_km, width=10)
calculate_button.grid(column=2, row=4)

# Start the main event loop
window.mainloop()

