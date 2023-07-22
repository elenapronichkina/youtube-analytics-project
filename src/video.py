import json
import os
from googleapiclient.discovery import build
from src.channel import Channel
class Video(Channel):
    def __init__(self, channel_id, video_id):
        # Вызываем метод базового класса
        try:
            super().__init__(channel_id)
        # Дополнительный код

            video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=self.video_id).execute()
        except FileNotFoundError:
            raise FileNotFoundError("Неверный id")
            self.broken_video_id = broken_video_id  # id видео
            self.video = None
            self.video_title = None  # название видео
            self.url_video = None  # ссылка на видео
            self.view_count = None  # количество просмотров
            self.like_count = None  # количество лайков

        else:
            playlist_videos = self.youtube.playlists().list(channelId=self.channel_id,
                                     part='contentDetails,snippet',
                                     maxResults=50,).execute()
            self.video_id = video_id # id видео
            self.video = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
            self.video_title = video_response['items'][0]['snippet']['title']  # название видео
            self.url_video = f"https://www.youtube.com/channel/{channel_id}/{video_id}"# ссылка на видео
            self.view_count = int(self.video_response['items'][0]['statistics']['viewCount']) # количество просмотров
            self.like_count = int(self.video_response['items'][0]['statistics']['likeCount'])  # количество лайков



       # self.channel = self.youtube.channels().list(id=self.channel_id,
    #                                            part='snippet,statistics').execute()

class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(channel_id, video_id)
        self.playlist_id = playlist_id
        self.playlist = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()


