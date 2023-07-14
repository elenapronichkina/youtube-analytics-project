from src.video import PLVideo
class PlayList(PLVideo):
    """класс PlayList, инициализируется id плейлиста и имеет следующие
    публичные атрибуты: название плейлиста, ссылку на плейлист"""
    def __init__(self, playlist_id):
        super().__init__(video_id, playlist_id)
        self.pl_title = pl_title
        self.pl_url = f"https://www.youtube.com/channel/playlist?list={playlist_id}"# ссылка на плейлист

#методы класса PlayList
    #total_duration возвращает объект класса datetime.timedelta с суммарной длительность плейлиста
# (обращение как к свойству, использовать @property)
    @property
    def total_duration(self):
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(self.video_ids)
                                               ).execute()
        return video_response

    @total_duration.setter
    def total_duration(self):
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            return duration
    def show_best_video():
        """возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        like_count_list = []
        for video in playlist_videos['items']:

            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
            like_count: int = video_response['items'][0]['statistics']['likeCount']
            like_count_list.append(like_count)
        like_count_list.sort(reverse=True)
        max_like_count = like_count_list[0]
        return max_like_count


