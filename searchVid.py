# -*- coding: utf-8 -*-
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def searchYTSongs():


    ############################
    # Replace your YT json file here
    readFileName = 'songs.txt'
    writeFileName = 'songsConvert.txt'
    yt_secret = "yt_secret.json"

    ############################


    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = yt_secret

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    readF = open(readFileName,'r',encoding='utf-8')
    writeF = open(writeFileName,'w',encoding='utf-8')
    line = readF.readline()

    while line:
        try:
            
            print("Searching up",line)
            request = youtube.search().list(
                part="snippet",
                maxResults=25,
                q=line
            )
            response = request.execute()
            print(response['items'][0]['id']['videoId'])
            writeF.write(response['items'][0]['id']['videoId'] + ' ')
            line = readF.readline()
        except:
            line = False


