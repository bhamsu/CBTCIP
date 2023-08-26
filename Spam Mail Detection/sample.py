import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("GUI Example")

# Create the text box
text_box = tk.Entry(window)
text_box.pack()

# Create the button
button = tk.Button(window, text="Click Me!")
button.pack()

# Create the label
label = tk.Label(window)
label.pack()

# Bind the button click event to a function
def click_handler():
  text = text_box.get()
  if text == "Hello":
    label.config(text="The text is Hello")
  else:
    label.config(text="The text is not Hello")

button.config(command=click_handler)

# Start the main loop
window.mainloop()
