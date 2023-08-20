import subprocess
import tkinter as tk

def start_files():
    # Launch the first Python file in the background
    process1 = subprocess.Popen(['python', 'blink_detector_face_orientation.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)

    # Launch the second Python file
    process2 = subprocess.Popen(['python', 'AC-test_lastrun.py'])

def exit_program():
    root.destroy()

# Create the GUI
root = tk.Tk()
root.attributes('-fullscreen', True)  # Set the GUI to full screen

# Set the font size for the labels and buttons
font_size = 30

# Create a frame to center the elements
center_frame = tk.Frame(root)
center_frame.pack(expand=True)

# Create the instruction label with larger font size
instruction_label = tk.Label(center_frame, text='Click the start button.', font=('Arial', font_size))
instruction_label.pack()

# Create the start button with larger font size
start_button = tk.Button(center_frame, text='Start', command=start_files, font=('Arial', font_size))
start_button.pack(pady=20)

# Create the exit button with larger font size
exit_button = tk.Button(center_frame, text='Exit', command=exit_program, font=('Arial', font_size))
exit_button.pack()

# Center the frame in the GUI
center_frame.place(relx=0.5, rely=0.5, anchor='center')

# Start the GUI event loop
root.mainloop()


