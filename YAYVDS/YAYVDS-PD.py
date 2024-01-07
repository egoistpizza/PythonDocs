#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2024 Yusuf ÖZÇETİN

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Yet Another YouTube Video Downloader Script - Playlist Downloader ---> YAYVDS-PD
"""

from pytube import YouTube,Playlist

p = Playlist("YouTube Playlist Link Here")

print(f'Downloading: {p.title}')

for video in p.videos:
    video.streams.first().download()
    