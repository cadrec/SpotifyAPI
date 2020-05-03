# Program to find top tracks and albums from certain artists
# Programs generates data for four countries
# Data is converted to csv file to be analyzed


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

ID =     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

client_credentials_manager = SpotifyClientCredentials(client_id = ID, client_secret = SECRET)
spotify = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

drake_id = "3TVXtAsR1Inumwj472S9r4"
billie_id = "6qqNVTkY8uBg9cP3Jd7DAH"
zeppelin_id = "36QJpDe2go2KgaRleHCDTp"
combs_id = "718COspgdWOnwOFpJHRZHS"
slipknot_id = "05fG473iIaoy82BF1aGhL8"
marshmello_id = "64KEffDW9EtZ1y2vBYgq8T"
khalid_id = "6LuN9FCkKOj5PcnpouEgny"
badbunny_id = "4q3ewBCX7sLwd24euuV69X"

us_top_tracks = [] #united stated
us_top_albums = []
gb_top_tracks = [] #great britain
gb_top_albums = []
de_top_tracks = [] #germany
de_top_albums = []
br_top_tracks = [] #brazil
br_top_albums = []

us_drake_tracks = spotify.artist_top_tracks(drake_id, country="US")
us_top_tracks.append(us_drake_tracks)
us_drake_albums = spotify.artist_albums(drake_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_drake_albums)

gb_drake_tracks = spotify.artist_top_tracks(drake_id, country="GB")
gb_top_tracks.append(gb_drake_tracks)
gb_drake_albums = spotify.artist_albums(drake_id, album_type="album", country="GB", limit=3)
gb_top_albums.append(gb_drake_albums)

de_drake_tracks = spotify.artist_top_tracks(drake_id, country="DE")
de_top_tracks.append(de_drake_tracks)
de_drake_albums = spotify.artist_albums(drake_id, album_type="album", country="DE", limit=3)
de_top_albums.append(de_drake_albums)

br_drake_tracks = spotify.artist_top_tracks(drake_id, country="BR")
br_top_tracks.append(br_drake_tracks)
br_drake_albums = spotify.artist_albums(drake_id, album_type="album", country="BR", limit=3)
br_top_albums.append(br_drake_albums)




us_billie_tracks = spotify.artist_top_tracks(billie_id, country="US")
us_top_tracks.append(us_billie_tracks)
us_billie_albums = spotify.artist_albums(billie_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_billie_albums)

gb_billie_tracks = spotify.artist_top_tracks(billie_id, country="GB")
gb_top_tracks.append(gb_billie_tracks)
gb_billie_albums = spotify.artist_albums(billie_id, album_type="album", country="GB", limit=3)
gb_top_albums.append(gb_billie_albums)

de_billie_tracks = spotify.artist_top_tracks(billie_id, country="DE")
de_top_tracks.append(de_billie_tracks)
de_billie_albums = spotify.artist_albums(billie_id, album_type="album", country="DE", limit=3)
de_top_albums.append(de_billie_albums)

br_billie_tracks = spotify.artist_top_tracks(billie_id, country="BR")
br_top_tracks.append(br_billie_tracks)
br_billie_albums = spotify.artist_albums(billie_id, album_type="album", country="BR", limit=3)
br_top_albums.append(br_billie_albums)




us_zeppelin_tracks = spotify.artist_top_tracks(zeppelin_id, country="US")
us_top_tracks.append(us_zeppelin_tracks)
us_zeppelin_albums = spotify.artist_albums(zeppelin_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_zeppelin_albums)

gb_zeppelin_tracks = spotify.artist_top_tracks(zeppelin_id, country="GB")
gb_top_tracks.append(gb_zeppelin_tracks)
gb_zeppelin_albums = spotify.artist_albums(zeppelin_id, album_type="album", country="GB", limit=3)
gb_top_albums.append(gb_zeppelin_albums)

de_zeppelin_tracks = spotify.artist_top_tracks(zeppelin_id, country="DE")
de_top_tracks.append(de_zeppelin_tracks)
de_zeppelin_albums = spotify.artist_albums(zeppelin_id, album_type="album", country="DE", limit=3)
de_top_albums.append(de_zeppelin_albums)

br_zeppelin_tracks = spotify.artist_top_tracks(zeppelin_id, country="BR")
br_top_tracks.append(br_zeppelin_tracks)
br_zeppelin_albums = spotify.artist_albums(zeppelin_id, album_type="album", country="BR", limit=3)
br_top_albums.append(br_zeppelin_albums)




us_combs_tracks = spotify.artist_top_tracks(combs_id, country="US")
us_top_tracks.append(us_combs_tracks)
us_combs_albums = spotify.artist_albums(combs_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_combs_albums)

gb_combs_tracks = spotify.artist_top_tracks(combs_id, country="GB")
gb_top_tracks.append(gb_combs_tracks)
gb_combs_albums = spotify.artist_albums(combs_id, album_type="album", country="GB", limit=3)
gb_top_albums.append(gb_combs_albums)

de_combs_tracks = spotify.artist_top_tracks(combs_id, country="DE")
de_top_tracks.append(de_combs_tracks)
de_combs_albums = spotify.artist_albums(combs_id, album_type="album", country="DE", limit=3)
de_top_albums.append(de_combs_albums)

br_combs_tracks = spotify.artist_top_tracks(combs_id, country="BR")
br_top_tracks.append(br_combs_tracks)
br_combs_albums = spotify.artist_albums(combs_id, album_type="album", country="BR", limit=3)
br_top_albums.append(br_combs_albums)




us_slipknot_tracks = spotify.artist_top_tracks(slipknot_id, country="US")
us_top_tracks.append(us_slipknot_tracks)
us_slipknot_albums = spotify.artist_albums(slipknot_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_slipknot_albums)

gb_slipknot_tracks = spotify.artist_top_tracks(slipknot_id, country="GB")
gb_top_tracks.append(gb_slipknot_tracks)
gb_slipknot_albums = spotify.artist_albums(slipknot_id, album_type="album", country="GB", limit=3)
gb_top_albums.append(gb_slipknot_albums)

de_slipknot_tracks = spotify.artist_top_tracks(slipknot_id, country="DE")
de_top_tracks.append(de_slipknot_tracks)
de_slipknot_albums = spotify.artist_albums(slipknot_id, album_type="album", country="DE", limit=3)
de_top_albums.append(de_slipknot_albums)

br_slipknot_tracks = spotify.artist_top_tracks(slipknot_id, country="BR")
br_top_tracks.append(br_slipknot_tracks)
br_slipknot_albums = spotify.artist_albums(slipknot_id, album_type="album", country="BR", limit=3)
br_top_albums.append(br_slipknot_albums)




us_marshmello_tracks = spotify.artist_top_tracks(marshmello_id, country="US")
us_top_tracks.append(us_marshmello_tracks)
us_marshmello_albums = spotify.artist_albums(marshmello_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_marshmello_albums)

gb_marshmello_tracks = spotify.artist_top_tracks(marshmello_id, country="GB")
gb_top_tracks.append(gb_marshmello_tracks)
gb_marshmello_albums = spotify.artist_albums(marshmello_id, album_type="album", country="GB", limit=3)
gb_top_albums.append(gb_marshmello_albums)

de_marshmello_tracks = spotify.artist_top_tracks(marshmello_id, country="DE")
de_top_tracks.append(de_marshmello_tracks)
de_marshmello_albums = spotify.artist_albums(marshmello_id, album_type="album", country="DE", limit=3)
de_top_albums.append(de_marshmello_albums)

br_marshmello_tracks = spotify.artist_top_tracks(marshmello_id, country="BR")
br_top_tracks.append(br_marshmello_tracks)
br_marshmello_albums = spotify.artist_albums(marshmello_id, album_type="album", country="BR", limit=3)
br_top_albums.append(br_marshmello_albums)




us_khalid_tracks = spotify.artist_top_tracks(khalid_id, country="US")
us_top_tracks.append(us_khalid_tracks)
us_khalid_albums = spotify.artist_albums(khalid_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_khalid_albums)

gb_khalid_tracks = spotify.artist_top_tracks(khalid_id, country="GB")
gb_top_tracks.append(gb_khalid_tracks)
gb_khalid_albums = spotify.artist_albums(khalid_id, album_type="album", country="GB", limit=3)
gb_top_albums.append(gb_khalid_albums)

de_khalid_tracks = spotify.artist_top_tracks(khalid_id, country="DE")
de_top_tracks.append(de_khalid_tracks)
de_khalid_albums = spotify.artist_albums(khalid_id, album_type="album", country="DE", limit=3)
de_top_albums.append(de_khalid_albums)

br_khalid_tracks = spotify.artist_top_tracks(khalid_id, country="BR")
br_top_tracks.append(br_khalid_tracks)
br_khalid_albums = spotify.artist_albums(khalid_id, album_type="album", country="BR", limit=3)
br_top_albums.append(br_khalid_albums)




us_badbunny_tracks = spotify.artist_top_tracks(badbunny_id, country="US")
us_top_tracks.append(us_badbunny_tracks)
us_badbunny_albums = spotify.artist_albums(badbunny_id, album_type="album", country="US", limit=3)
us_top_albums.append(us_badbunny_albums)

gb_badbunny_tracks = spotify.artist_top_tracks(badbunny_id, country="GB")
gb_top_tracks.append(gb_badbunny_tracks)
gb_badbunny_albums = spotify.artist_albums(badbunny_id, album_type="album", country="GB", limit=3)
gb_top_albums.append(gb_badbunny_albums)

de_badbunny_tracks = spotify.artist_top_tracks(badbunny_id, country="DE")
de_top_tracks.append(de_badbunny_tracks)
de_badbunny_albums = spotify.artist_albums(badbunny_id, album_type="album", country="DE", limit=3)
de_top_albums.append(de_badbunny_albums)

br_badbunny_tracks = spotify.artist_top_tracks(badbunny_id, country="BR")
br_top_tracks.append(br_badbunny_tracks)
br_badbunny_albums = spotify.artist_albums(badbunny_id, album_type="album", country="BR", limit=3)
br_top_albums.append(br_badbunny_albums)




with open("spotify_us_output.txt", "w") as file:
    for track in us_top_tracks:
        for key,value in track.items():
            file.write("%s:%s\n" % (key,value))

with open("spotify_gb_output.txt", "w") as file:
    for track in gb_top_tracks:
        for key,value in track.items():
            file.write("%s:%s\n" % (key,value))

with open("spotify_de_output.txt", "w") as file:
    for track in de_top_tracks:
        for key,value in track.items():
            file.write("%s:%s\n" % (key,value))

with open("spotify_br_output.txt", "w") as file:
    for track in br_top_tracks:
        for key,value in track.items():
            file.write("%s:%s\n" % (key,value))
