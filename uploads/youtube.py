
"""
check the docs for the youtube api
https://developers.google.com/youtube/v3/getting-started

for implementing the youtube api auth feature -uses 0auth2.0
https://developers.google.com/youtube/v3/quickstart/python
https://developers.google.com/youtube/v3/guides/uploading_a_video
"""

# from utils.console import print_step

import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload

# The scopes required by the API
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

# The client_secrets.json file is obtained from the Google Cloud Console
CLIENT_SECRET_FILE = r'.\uploads\yt-secrets.json'

# YouTube API service name and version
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def authenticate_youtube():
    # Load client secrets file, put the path of your file
    print('Authenticating YouTube...')
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_local_server()

    youtube = build(
        "youtube", "v3", credentials=credentials)

    return youtube

def upload_video(VIDEO_FILE_PATH,TITLE,DESCRIPTION,CATEGORY_ID,TAGS):
    youtube = authenticate_youtube()
    """Upload a video to YouTube."""
    # Prepare the file for upload
    media = MediaFileUpload(VIDEO_FILE_PATH, mimetype='video/mp4', chunksize=-1, resumable=True)

    # Request body for the upload
    request_body = {
        'snippet': {
            'title': TITLE,
            'description': DESCRIPTION,
            'tags': TAGS,
            'categoryId': CATEGORY_ID,
        },
        'status': {
            'privacyStatus': 'private',  # TODOYou can change it to 'public' or 'unlisted'
        }
    }

    # Upload the video
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    # Monitor the upload process
    response = request.execute()
    print(f'Upload successful to youtube! Video ID: {response["id"]}')


if __name__ == '__main__':
    # The video you want to upload
    VIDEO_FILE_PATH = 'test.mp4'
    TITLE = 'this is a Title'
    DESCRIPTION = 'Video Description'
    CATEGORY_ID = '24'  # 24 = Entertainment
    TAGS = ['tags', 'tags', 'tags', 'tags']
    vid_id=upload_video(VIDEO_FILE_PATH,TITLE,DESCRIPTION,CATEGORY_ID,TAGS)
