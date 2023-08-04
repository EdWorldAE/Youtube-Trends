import requests
import tkinter as tk
from tkinter import ttk
def get_trending_videos():
    # Get user input from text fields
    country_value = country_entry.get()
    type_value = type_entry.get()

    url = "https://youtube-trending.p.rapidapi.com/trending"
    querystring = {"country": country_value, "type": type_value}
    headers = {
        "X-RapidAPI-Key": "Your API Key here",
        "X-RapidAPI-Host": "youtube-trending.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Define the keys we want to display
    keys_to_display = [
        "title",
        "description",
        "publishedDate",
        "publishedText",
        "videoId",
        "videoUrl",
        "channelName",
        "channelId",
        "channelUrl"
    ]

    # Clear the previous results
    output_text.delete(1.0, tk.END)

    # Loop through each video and display the selected fields in the Text widget
    for video in data:
        for key in keys_to_display:
            output_text.insert(tk.END, f'"{key}": "{video.get(key, "N/A")}",\n')
        output_text.insert(tk.END, "-----------------------------\n")


# Create the main application window
app = tk.Tk()
app.title("YouTube Trending Videos")

# Add widgets for Country and Type
ttk.Label(app, text="Country:").grid(column=0, row=0, padx=10, pady=5)
country_entry = ttk.Entry(app)
country_entry.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(app, text="Type:").grid(column=0, row=1, padx=10, pady=5)
type_entry = ttk.Entry(app)
type_entry.grid(column=1, row=1, padx=10, pady=5)

# Button to fetch trending videos
ttk.Button(app, text="Get Trending Videos", command=get_trending_videos).grid(column=0, row=2, columnspan=2, pady=10)

# Text widget to display the results
output_text = tk.Text(app, wrap=tk.WORD, width=80, height=20)
output_text.grid(column=0, row=3, columnspan=2, padx=10, pady=5)

app.mainloop()
