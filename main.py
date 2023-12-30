import os
import csv
import tkinter as tk
from tkinter import filedialog

def generate_csv():
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_file = 'folder_names.csv'
        folder_names = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]
        with open(output_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Folder Names'])
            for folder_name in folder_names:
                csv_writer.writerow([folder_name])
        status_label.config(text=f"CSV file '{output_file}' generated successfully.")

# Creating the GUI window
root = tk.Tk()
root.title("Folder Names to CSV Generator")

# Setting the size of the window
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Button to trigger the CSV generation process
generate_button = tk.Button(root, text="Select Folder and Generate CSV", command=generate_csv)
generate_button.pack(pady=20)

# Label to display status/messages
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
