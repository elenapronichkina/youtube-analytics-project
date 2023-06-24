import json
import os
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY_YT')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"] #название канала
        self.description = self.channel['items'][0]['snippet']['description'] #описание канала
        self.url = f"https://www.youtube.com/channel/{channel_id}" #ссылка на  канал
        self.subscriber_count = int(self.channel["items"][0]["statistics"]["subscriberCount"]) #количество подписчиков
        self.video_count = int(self.channel["items"][0]["statistics"]["videoCount"]) #количество видео
        self.view_count = int(self.channel["items"][0]["statistics"]["viewCount"])   #общее количество просмотров


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(info)

    @classmethod
    def get_service(cls):
        """возвращает объект для работы с YouTube API"""
        return cls.youtube
    #    print(cls.youtube)

    def to_json(self, filename):
        """сохраняет в файл значения атрибутов экземпляра Channel"""
        data = {
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscribers_count": self.subscribers_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }
        with open(filename, "w", encoding="windows-1251") as file:
            json.dumps(data, file, indent=2, ensure_ascii=False)