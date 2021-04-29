"""
Given a map Map<String, List<String>> userSongs with user names as keys and a list
of all the songs that the user has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a
list of all the songs within that genre as values.
The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a
list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one
favorite genre if he/she has listened to the same number of songs per each of the genres.
"""

def get_favorites(dic):
    # import ipdb; ipdb.set_trace()
    likes = max(dic.items())
    favorites = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    res = {}
    for key in favorites:
        if favorites[key] < likes[1]:
            return res
        res[key] = favorites[key]
    return res

def music_favorite_genres(users, genres):
    users_favorites = {}
    for user in users:
        favorites = {}
        songs = users[user]
        for song in songs:
            for genre in genres:
                if song in genres[genre]:
                    if genre in favorites:
                        favorites[genre] += 1
                    else:
                        favorites[genre] = 0
        users_favorites[user] = get_favorites(favorites)
    return users_favorites
# Input:
userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output = {
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

print(music_favorite_genres(userSongs, songGenres))
