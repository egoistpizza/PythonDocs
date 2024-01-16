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
from pytube import Playlist
from tqdm import tqdm
import logging

# Set up the log file
logging.basicConfig(filename='yayvds_pd.log', level=logging.INFO)

def download_video(video, path_to_download, counter, resolution=None):
    try:
        print(f'Downloading: {video.title}')
        
        # Retrieve streams with different resolution
        streams = video.streams.filter(res=resolution, file_extension="mp4").first()
        out_file = streams.download(output_path=path_to_download)
        
        new_file_name = f'{path_to_download}\\{counter}-{os.path.splitext(os.path.basename(out_file))[0]}.mp4'
        os.rename(out_file, new_file_name)
        
        logging.info(f"Downloaded: {video.title}")
    except Exception as e:
        logging.error(f"Error downloading {video.title}: {e}")

def download_playlist(playlist_url, download_path, resolution=None):
    try:
        p = Playlist(playlist_url)
        counter = 1

        for video in tqdm(p.videos, desc="Downloading Playlist"):
            download_video(video, download_path, counter, resolution)
            counter += 1

        len_of_dir = len([name for name in os.listdir(download_path) if os.path.isfile(os.path.join(download_path, name))])

        if len(p) == len_of_dir:
            print(f"{len_of_dir}/{len(p)} video(s) has been successfully saved to directory {download_path}.")
        elif len(p) != len_of_dir and len_of_dir != 0:
            print(f"{len_of_dir}/{len(p)} video(s) has been successfully saved to directory {download_path}. Some videos are missing.")
        else:
            print(f"Something went wrong.")
    except KeyboardInterrupt:
        print("Download interrupted by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter the Playlist URL: ")
    download_path = input("Enter the download directory: ")
    resolution = input("Enter the desired resolution (optional): ")

    download_playlist(playlist_url, download_path, resolution)
