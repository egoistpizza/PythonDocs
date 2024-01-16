#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2024 Yusuf ÖZÇETİN

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Yet Another YouTube Video Downloader Script - Playlist Downloader ---> YAYVDS-PD
"""

import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QComboBox, QProgressBar
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from pytube import Playlist
from tqdm import tqdm
import logging

class DownloadThread(QThread):
    update_progress = pyqtSignal(int)

    def __init__(self, playlist_url, download_path, resolutions=None):
        super(DownloadThread, self).__init__()
        self.playlist_url = playlist_url
        self.download_path = download_path
        self.resolutions = resolutions
        self.cancelled = False

    def run(self):
        try:
            p = Playlist(self.playlist_url)
            counter = 1

            for video in tqdm(p.videos, desc="Downloading Playlist"):
                if self.cancelled:
                    break

                self.download_video(video, counter)
                counter += 1

            len_of_dir = len([name for name in os.listdir(self.download_path) if os.path.isfile(os.path.join(self.download_path, name))])

            if not self.cancelled:
                if len(p) == len_of_dir:
                    print(f"{len_of_dir}/{len(p)} video(s) has been successfully saved to directory {self.download_path}.")
                elif len(p) != len_of_dir and len_of_dir != 0:
                    print(f"{len_of_dir}/{len(p)} video(s) has been successfully saved to directory {self.download_path}. Some videos are missing.")
                else:
                    print(f"Something went wrong.")
            else:
                print("Download cancelled.")
        except KeyboardInterrupt:
            print("Download interrupted by the user.")
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"An error occurred: {e}")

    def download_video(self, video, counter):
        try:
            self.update_progress.emit(counter)

            # Check if the video supports any of the specified resolutions
            streams = video.streams.filter(res=self.resolutions, file_extension="mp4")
            if streams:
                # Choose the stream with the highest resolution
                selected_stream = max(streams, key=lambda x: int(x.resolution.split('p')[0]))
            else:
                # If not, choose the stream with the highest resolution
                selected_stream = video.streams.filter(file_extension="mp4").get_highest_resolution()

            out_file = selected_stream.download(output_path=self.download_path)

            new_file_name = f'{self.download_path}/{counter}-{os.path.splitext(os.path.basename(out_file))[0]}.mp4'
            os.rename(out_file, new_file_name)

            logging.info(f"Downloaded: {video.title}")
        except Exception as e:
            logging.error(f"Error downloading {video.title}: {e}")

    def cancel_download(self):
        self.cancelled = True

class DownloaderApp(QWidget):
    def __init__(self):
        super(DownloaderApp, self).__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.link_label = QLabel("Playlist URL:")
        self.link_input = QLineEdit(self)

        self.dir_label = QLabel("Download Directory:")
        self.dir_input = QLineEdit(self)
        self.browse_button = QPushButton("Browse", self)
        self.browse_button.clicked.connect(self.browse_directory)

        self.resolution_label = QLabel("Resolution:")
        self.resolution_combobox = QComboBox(self)
        self.resolution_combobox.addItems(["1080p", "720p", "480p", "360p", "240p", "1440p (2K)", "2160p (4K)", "4320p (8K)"])

        self.progress_label = QLabel("Progress:")
        self.progress_bar = QProgressBar(self)

        self.download_button = QPushButton("Download", self)
        self.download_button.clicked.connect(self.start_download)

        self.cancel_button = QPushButton("Cancel Download", self)
        self.cancel_button.clicked.connect(self.cancel_download)

        layout.addWidget(self.link_label)
        layout.addWidget(self.link_input)
        layout.addWidget(self.dir_label)
        layout.addWidget(self.dir_input)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.resolution_label)
        layout.addWidget(self.resolution_combobox)
        layout.addWidget(self.progress_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.download_button)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)
        self.setWindowTitle('YouTube Playlist Downloader')
        self.setGeometry(100, 100, 500, 300)  # Pencere boyutu ve konumu


    def browse_directory(self):
        download_dir = QFileDialog.getExistingDirectory(self, "Select Download Directory")
        if download_dir:
            self.dir_input.setText(download_dir)

    def start_download(self):
        playlist_url = self.link_input.text()
        download_path = self.dir_input.text()
        resolution = self.resolution_combobox.currentText()

        self.thread = DownloadThread(playlist_url, download_path, resolution)
        self.thread.update_progress.connect(self.update_progress_bar)
        self.thread.start()

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    def cancel_download(self):
        if hasattr(self, 'thread') and isinstance(self.thread, DownloadThread):
            self.thread.cancel_download()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DownloaderApp()
    window.show()
    sys.exit(app.exec_())