# Spotify APIの準備
client_id = 'your id in here'
client_secret = 'your secret in here'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
