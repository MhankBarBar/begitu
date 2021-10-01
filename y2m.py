from bs4 import BeautifulSoup as bs
from requests import post
from re import match, search
from typing import Union

class Y2mate:

    def __init__(self, url: Union[str], type: Union[str], quality: Union[str], server: Union[str]="en68") -> Union[None]:
        """
        :url: String
        :type: String -> mp4|mp3
        :quality: String -> mp4 (144p, 240p, 360p, 480p, 720p, 1080p) | mp3 (128)
        :server: String -> (id4, en60, en61, en68)
        e.g:
        from y2mate import Y2mate
        yt = Y2mate("https://youtu.be/pOWuBM2RNmI", "mp3", "128")
        yt.fetch
        """
        self.__url = url
        self.__type = type
        self.__quality = quality
        self.__server = server

    def __getid(self, url: Union[str]) -> Union[str, bool]:
        """
        Private function
        :url: String
        :return: String|Boolean
        """
        pattern = r"(?:http(?:s|):\/\/|)(?:(?:www\.|)youtube(?:\-nocookie|)\.com\/(?:shorts\/)?(?:watch\?.*(?:|\&)v=|embed\/|v\/)|youtu\.be\/)([-_0-9A-Za-z]{11})"
        return match(pattern, url).group(1) if match(pattern, url) else False

    @property
    def fetch(self) -> Union[dict]:
        if not self.__getid(self.__url):raise Exception("Invalid YouTube url")
        try:
            return {'result': bs(post(f'https://www.y2mate.com/mates/{self.__server}/convert', data={'type': 'youtube', '_id': search('var k__id = "(.+?)"', bs(post('https://www.y2mate.com/mates/{self.__server}/analyze/ajax', data={'url': f'https://youtu.be/{self.__getid(self.__url)}', 'q_auto': 0, 'ajax': 1}).json()['result'], 'html.parser').findAll('script')[1].string)[1], 'v_id': self.__getid(self.__url), 'ajax': '1', 'token': '', 'ftype': self.__type, 'fquality': self.__quality}).json()['result'], 'html.parser').a['href']}
        except IndexError:
            return {'error': 'Terjadi kesalahan'}
