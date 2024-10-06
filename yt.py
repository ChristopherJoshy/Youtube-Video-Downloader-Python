import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    
    try:
        yt = YouTube(url)
        # Get the highest resolution video stream with audio
        stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        
        # Ask user for download directory
        download_folder = filedialog.askdirectory()
        
        if download_folder:
            # Download the video
            stream.download(output_path=download_folder)
            messagebox.showinfo("Success", f"Video downloaded successfully at {download_folder}")
        else:
            messagebox.showwarning("Cancelled", "Download folder not selected")
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video.\n{e}")
window = tk.Tk()
window.title("YouTube Video Downloader")
window.geometry("400x200")
url_label = tk.Label(window, text="YouTube URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=5)
download_button = tk.Button(window, text="Download Video", command=download_video)
download_button.pack(pady=20)
window.mainloop()
