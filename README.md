# YouTube Video Downloader

This project is a simple **YouTube Video Downloader** that allows users to download videos from YouTube directly to their computer. The app uses the Python `tkinter` library to create a graphical user interface (GUI) and `pytube` to handle the downloading of the video content.

## Features

- **User-Friendly Interface**: The app uses a simple GUI built with `tkinter` to make it easy for anyone to use.
- **Download in Highest Quality**: Automatically downloads the highest resolution video available with audio.
- **Custom Download Location**: You can select the folder where you'd like the video to be saved.

## How to Use

1. Enter a valid **YouTube URL** in the input field.
2. Click the **Download Video** button.
3. Choose the folder where you want to save the downloaded video.
4. The app will fetch the highest quality available for the video and download it to the specified location.

## Prerequisites

To run this app, you need:

- **Python 3.x** installed on your system.
- Install the required dependencies using:

  ```bash
  pip install pytube tkinter
  ```

  - `pytube` is used for downloading videos from YouTube.
  - `tkinter` is part of Python's standard library and doesn't need separate installation for most users.

## Running the Application

1. Clone or download the repository to your local machine.
2. Run the Python script using:

   ```bash
   python youtube_downloader.py
   ```

3. The application window will open, where you can input the YouTube video URL and start downloading.

## Code Overview

- **YouTube URL Input**: The user can input a valid YouTube URL into the text entry box.
- **Download Button**: When pressed, it fetches the highest quality video available and downloads it to the selected directory.
- **Error Handling**: The app provides error messages for invalid URLs or other issues (e.g., no internet connection).
- **Success Message**: Displays a confirmation once the video has been successfully downloaded.

## Example

- Example of the GUI:

  ![Example](./example_gui_screenshot.png) *(This would be a screenshot of your app’s window)*

## Dependencies

- `pytube`: A lightweight, Pythonic library for downloading YouTube videos.
- `tkinter`: A standard Python interface to the Tk GUI toolkit.

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

## Future Enhancements

- **Download Progress Bar**: Add a progress bar to show download progress.
- **Quality Selection**: Let users choose the video quality before downloading.
- **Video Metadata Display**: Display more information like video title, duration, etc., before downloading.

#This readme file was created using Chatgpt nothing else use Chatgpt
