import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify client with user authorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="f974da21e2444e569517532cc1c99b3e",
                                               client_secret="71ded5b046e94b0482321c9b6fe4272f",
                                               redirect_uri="http://localhost:5000/callback",
                                               scope="user-library-read"))

# Function to fetch user's liked songs
def get_users_liked_songs():
    results = sp.current_user_saved_tracks()
    liked_songs = []
    for idx, item in enumerate(results['items']):
        track = item['track']
        liked_songs.append(track['name'] + ' - ' + track['artists'][0]['name'])
    return liked_songs

# Function to recommend songs based on user's liked songs
def recommend_songs(based_on_songs):
    recommendations = sp.recommendations(seed_tracks=based_on_songs, limit=10)
    recommended_songs = []
    for track in recommendations['tracks']:
        recommended_songs.append(track['name'] + ' - ' + track['artists'][0]['name'])
    return recommended_songs

# Main Program
liked_songs = get_users_liked_songs()
recommended_songs = recommend_songs(liked_songs)
print("Recommended Songs:")
for song in recommended_songs:
    print(song)
