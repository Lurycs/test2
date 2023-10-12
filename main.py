from typing import Optional, List, Dict
from pydantic import BaseModel
#
# class User(BaseModel):
#     name: str
#     followers: int
#     posts: int
#
# a = User(name ='Jordan', followers = 50, posts = 2)
#
# print(a)
#
#
# class User1(BaseModel):
#     name: str
#     surName: str
#     age: int
#
# b = User1(name='Max', surName='Pak', age=15)
# print(b)
#
# class Player(BaseModel):
#     player_name: Optional[str]
#     player_deposit: Optional[str]
#     player_items: List[Dict[str, int]]
#     player_friends: List[str] = '0'
#
# try:
#     new_player = Player(player_name='Jordan', player_deposit= 0,  player_items=[{'lifes'}])
#     print(new_player)
#
# except:
#     print('Error data')


class User(BaseModel):
    username: str
    mail: Optional[str] = None
    language: str

class Artist(BaseModel):
    artist_name: str
    artist_followers: int

class Song(BaseModel):
    artist: Artist
    song_name: str
    date_of_publishing: str

class Playlist(BaseModel):
    user: User
    songs: Song
    likes: int=0

#
# try:
a = User(username = 'Basta', language='ru')
b = Artist(artist_name='Basta',artist_followers=5000000)
c = Song(artist= b, song_name= "asd", date_of_publishing='12.10.23')
d = Playlist(user=a, songs=c)
print(c)
#
# except:
#     print('Error data')









# class Comment(BaseModel):
#     user: str
#     comment: str
#     like: int = 0
#
# first_comment = Comment()





# player_coins:List[int] = []
# player_nam:Optional[str] = 'Hello'
#
# class Player(BaseModel):
#     name: str
#     deposit: int
#     items: List[Dict[str, int]]
#     friends:List[str] = 'Electronic'
#
# s1mple = Player(name = 'Tolik', items = ['burger'], deposit = 3400)
# print(player_coins)
# print(player_nam)
