# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def insertYTSongs(ytPlaylistID):
    ################################
    # Replace your YT json file here
    readFileName = "songsConvert.txt"
    yt_secret = "yt_secret.json"
    #################################

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = yt_secret

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    readF = open(readFileName, 'r', encoding='utf-8')
    line = readF.read().split()

    for i in range(len(line)):
        redo = True
        while redo == True:
            try:
                request = youtube.playlistItems().insert(
                    part="snippet",
                    body={
                        "snippet": {
                            "playlistId": ytPlaylistID,
                            "position": 0,
                            "resourceId": {
                                "kind": "youtube#video",
                                "videoId": line[i]
                            }
                        }
                    }
                )
                response = request.execute()
                print(response)
                redo = False
            except:
                redo = True
