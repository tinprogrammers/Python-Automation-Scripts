import instaloader

L = instaloader.Instaloader()

# Replace with the username of any public profile
username = "nasa"

# This will download all posts of the profile
L.download_profile(username, profile_pic_only=False)
