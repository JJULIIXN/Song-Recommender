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
    liked_songs_ids = []
    for idx, item in enumerate(results['items']):
        track = item['track']
        liked_songs_ids.append(track['id'])  # Append only the track ID
    return liked_songs_ids

# Function to recommend songs based on user's liked songs
def recommend_songs(based_on_songs_ids):
    # Limit the number of seed tracks to 5 (or another number within Spotify's limits)
    seed_tracks_limited = based_on_songs_ids[:5]  
    recommendations = sp.recommendations(seed_tracks=seed_tracks_limited, limit=10)
    recommended_songs = []
    for track in recommendations['tracks']:
        recommended_songs.append(track['name'] + ' - ' + track['artists'][0]['name'])
    return recommended_songs



# Main Program
liked_songs_ids = get_users_liked_songs()
recommended_songs = recommend_songs(liked_songs_ids)
print("Recommended Songs:")
for song in recommended_songs:
    print(song)