playlist ={}

while True:
    print ("\n -----------------Personalized Playlist Manager---------------")
    print("1.Add Song")
    print("2.Remove Song")
    print("3.View Playlist")
    print("4.Search Song")
    print("5.Exit")

    choice = input("Enter your choice(1-5): ")

    if choice=="1":
        title=input("Enter song title: ").strip()
        artist = input("Enter artist name: ").strip()

        if title in playlist:
            print("This song is already in the playlist!")
        else:
            playlist[title]=artist
            print(f"'{title}'by {artist} added to the playlists")
    elif choice=="2":
        title = input("Enter song title to remove: ").strip()

        if title in playlist:
            del playlist[title]
            print(f"'{title} removed from the playlist.")
        else:
            print("Song not found in the playlist")

    elif choice=="3":
        if playlist:
            print("\n Your Playlist:")
            for song,artist in playlist.items():
                print(f"-{song} by {artist}")
        else:
            print("Your playlist is empty!")

    elif choice =="4":
        search = input("Enter song title to search: ").strip()
        if search in playlist:
            print(f"{search} is in your playlist, song by {playlist[search]}")
        else:
            print("Song not found in the Playlist!")

    elif choice =="5":
        print("GoodBy")
        break

    else:
        print("Wrong number!Enter a number between 1-5")



