# comments


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

ID =     'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'

client_credentials_manager = SpotifyClientCredentials(client_id = ID, client_secret = SECRET)
spotify = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

drake_id = "3TVXtAsR1Inumwj472S9r4"
billie_id = "6qqNVTkY8uBg9cP3Jd7DAH"
zeppelin_id = "36QJpDe2go2KgaRleHCDTp"
combs_id = "718COspgdWOnwOFpJHRZHS"
slipknot_id = "05fG473iIaoy82BF1aGhL8"
marshmello_id = "64KEffDW9EtZ1y2vBYgq8T"
khalid_id = "6LuN9FCkKOj5PcnpouEgny"

us_top_tracks = []
us_top_albums = []

us_drake_tracks = spotify.artist_top_tracks(drake_id, country="US")
us_top_tracks.append(us_drake_tracks)
us_drake_albums = spotify.artist_albums(drake_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_drake_albums)

us_billie_tracks = spotify.artist_top_tracks(billie_id, country="US")
us_top_tracks.append(us_billie_tracks)
us_billie_albums = spotify.artist_albums(billie_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_billie_albums)


us_zeppelin_tracks = spotify.artist_top_tracks(zeppelin_id, country="US")
us_top_tracks.append(us_zeppelin_tracks)
us_zeppelin_albums = spotify.artist_albums(zeppelin_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_zeppelin_albums)


us_combs_tracks = spotify.artist_top_tracks(combs_id, country="US")
us_top_tracks.append(us_combs_tracks)
us_combs_albums = spotify.artist_albums(combs_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_combs_albums)


us_slipknot_tracks = spotify.artist_top_tracks(slipknot_id, country="US")
us_top_tracks.append(us_slipknot_tracks)
us_slipknot_albums = spotify.artist_albums(slipknot_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_slipknot_albums)


us_marshmello_tracks = spotify.artist_top_tracks(marshmello_id, country="US")
us_top_tracks.append(us_marshmello_tracks)
us_marshmello_albums = spotify.artist_albums(marshmello_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_marshmello_albums)


us_khalid_tracks = spotify.artist_top_tracks(khalid_id, country="US")
us_top_tracks.append(us_khalid_tracks)
us_khalid_albums = spotify.artist_albums(khalid_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_khalid_albums)

with open("spotify_output.txt", "w") as file:
    for track in us_top_tracks:
        for key,value in track.items():
            file.write("%s:%s\n" % (key,value))

#output.write(us_top_albums)
