# These imports will only be valid when the files are all in the same location/directory
import getSongs
import insertSong
import searchVid


print("Enter spotify URI: ",end = '')
spotifyURIKey = input()
print()
print("Enter youtube playlist ID: ",end='')
ytPlaylistKey = input()


if __name__ == '__main__':
    print("Spot:", spotifyURIKey)
    print("yt:", ytPlaylistKey)
    print("\n\n\n\n\n\n\n\n\n\n\n\nProgram Finished!")

#getSongs.getSpotifySongs(spotPlaylistID=spotifyURIKey)
#searchVid.searchYTSongs()
#insertSong.insertYTSongs(ytPlaylistID=ytPlaylistKey)




