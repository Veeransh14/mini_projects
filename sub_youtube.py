import tkinter as tk
from youtube2zim import YouTubeTranscriptApi

def fetch_and_display_subtitles(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        subtitles = ''
        for segment in transcript:
            subtitles += segment['text'] + '\n'
        # Display subtitles in a text area
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, subtitles)
    except Exception as e:
        print(f"Error fetching subtitles: {e}")

# Create GUI window
window = tk.Tk()
window.title("YouTube Video Subtitles")

# Create a text area to display subtitles
text_area = tk.Text(window, height=20, width=80)
text_area.pack()

# Entry widget to input video ID
video_id_entry = tk.Entry(window, width=40)
video_id_entry.pack()

def on_submit():
    video_id = video_id_entry.get()
    fetch_and_display_subtitles(video_id)

# Button to fetch subtitles
submit_button = tk.Button(window, text="Fetch Subtitles", command=on_submit)
submit_button.pack()

window.mainloop()
