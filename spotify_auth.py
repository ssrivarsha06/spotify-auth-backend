import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="f39352bfae6b44d1805848b81396cd1d",
    client_secret="881f8af97ae443e1a2f7f51309a924dc",
    redirect_uri="https://jolly-taffy-99923a.netlify.app/",
    scope="user-library-read user-read-playback-state user-modify-playback-state"
))

# Example API call
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")
