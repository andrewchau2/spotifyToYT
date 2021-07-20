IMPORTANT: IF SHARING THIS CODE WITH ANYONE ELSE, PLEASE DO NOT GIVE THEM THE .JSON FILES and secret.py. These
give the person with the key in control of the application.

This application converts a spotify playlist into a youtube playlist. However it is ONLY valid with UTF-8 Encoding.
Also PLEASE do not choose a playlist with over 100 songs, this program will not support it.
If there is an error when running the program, refer to "Troubleshooting.txt"


How to run the program:

The only file that needs to be opened is main.py. You will be prompted to input your playlist id
and uri key of your choice. After that, you'll be prompt to do some verification by signing into
your google/spotify account

---------------------------
GETTING SPOTIFY URI KEY:
---------------------------
Pick a playlist and click the three dots( . . .).
Next, hold the CTRL key in your keyboard and go under "Share" and click "Copy Spotify URI" and use it in
the "spotifyURIKey" variable in main.py. Ex: spotify:playlist:7gWxXtTSlyPlYdZUJ4wNzy

----------------------------
GETTING YOUTUBE PLAYLIST URI
----------------------------

In your browser, pick a youtube playlist that you own and go into the playlist.
Next, look at the URL and ONLY copy the letters & numbers after "list=" and use that to change the
"ytPlaylistKey" variable in main.py.

Ex:
Suppose my playlist url is : https://www.youtube.com/playlist?list=PLD1XonVsUHPZyHAwf6kpnoH6dEr2L0nvZ
Then the key is only: PLD1XonVsUHPZyHAwf6kpnoH6dEr2L0nvZ


------------------------------
HOW TO RUN MAIN.PY - PYCHARM
------------------------------

If you have little to no programming experience, it is recommended to use Pycharm for running this project.
You can download the community version here: https://www.jetbrains.com/pycharm/download/#section=windows

Once it's downloaded, open pycharm and click "File" in the top toolbar and click "Open". After that find the vidTransfer
project and open it. In the left middle section of your page, you should see all the files.
Add the libraries to your venv and set your interpreter

Once that's done, right click the code and click "Run 'main'".

If there is any errors running the program, refer to "Troubleshooting.txt"

------------------------------
HOW TO RUN MAIN.PY - TERMINAL
------------------------------

For windows only. Make sure you have all the libraries installed and run by doing
python main.py

-------------------------------
AUTH CODE and ACCOUNT LOGIN
-------------------------------
When running the program, you will be prompted to login to your spotify and google account. Follow what the popup tells
you and enter the key/url into the terminal.

For google, I need to give you access via email. Msg me at discord fightbattle2#4771

--------------------------------
ADVANCE OPTIONS
--------------------------------

Within searchVid.py, insertSong.py, and getSongs.py, there'll be ######### which is advance settings for the projects.
You will need to create your own keys to run this project. You can do this by going to these websites:

Spotify: https://developer.spotify.com/dashboard/applications
Youtube: https://console.cloud.google.com/home/dashboard
For youtube, you need to enable youtube data api v3





