from flask import Flask, render_template, request, send_file, redirect, url_for
from pytube import YouTube
import os
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    try:
        url = request.form['video_url']
        logging.debug(f"Attempting to download video from URL: {url}")

        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        download_path = stream.download()

        logging.debug(f"Video downloaded to: {download_path}")
        return send_file(download_path, as_attachment=True, download_name=f"{yt.title}.mp4")
    
    except Exception as e:
        logging.error(f"Error occurred while downloading video: {str(e)}")
        return redirect(url_for('index', error=str(e)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
