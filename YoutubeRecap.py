import json

def pretty_video_name(item):
    title = item["title"]
    if title.startswith("Watched"):
        return title[8:]
    return title

def print_top_channels(number, videos_2022, type):
    print("##### Top %s %s #####" % (number, type))
    viewed_channels = {}
    for video in videos_2022:
        if 'subtitles' not in video:
            continue
        key = video["subtitles"][0]["name"]
        if key not in viewed_channels:
            viewed_channels[key] = 1
        else:
            viewed_channels[key] += 1

    top = sorted(viewed_channels, key=viewed_channels.get, reverse=True)[:number]

    for index, channel in enumerate(top):
        print("%s: %s (%s times)" % (index+1, channel, viewed_channels[channel]))

    the_one = 'cocadmin'
    if the_one in viewed_channels and the_one not in top:
        print()
        print("!!!!!!!!!!! The one without this repo would not exist: %s watched %s time" %(the_one, viewed_channels[the_one]))

def print_top_item(number, videos_2022, type):
    print("##### Top %s %s #####" % (number, type))
    viewed_channels = {}
    for video in videos_2022:
        key = video["title"]
        if key not in viewed_channels:
            viewed_channels[key] = 1
        else:
            viewed_channels[key] += 1

    top = sorted(viewed_channels, key=viewed_channels.get, reverse=True)[:number]

    for index, channel in enumerate(top):
        print("%s: %s (%s times)" % (index+1, channel.replace("Watched", ""), viewed_channels[channel]))

def print_first_and_last(videos_2022):
    #sort by time...it is supposed to be already sorted
    #videos_2022.reverse()
    #time attribute looks like "time": "2022-06-18T13:19:15.732Z"
    videos_2022.sort(key=lambda item: item["time"])
    print("First Video of the year:", pretty_video_name(videos_2022[0]))
    print("Last Video of the year:", pretty_video_name(videos_2022[len(videos_2022)-1]))




if __name__ == '__main__':
    #Using python I/O open function to read the json file named Data_File.
    history = json.load(open("watch-history.json", encoding="utf8"))

    #keep only 2022, video, and filter Youtube Music
    videos_2022 = [item for item in history if item["title"] != 'Visited YouTube Music' and item["time"].startswith('2022') and item["header"] == 'YouTube']
    print("Number of Videos watched in 2022: ", len(videos_2022))
    print()

    print_first_and_last(videos_2022)

    print()

    print_top_channels(10, videos_2022, "channels")

    print()

    print_top_item(10, videos_2022, "videos")

    print()

    #Now do the same for Music
    #keep only 2022, video, and filter Youtube Music
    videos_2022 = [item for item in history if item["title"] != 'Visited YouTube Music' and item["time"].startswith('2022') and item["header"] == 'YouTube Music']
    print("Number of music listened in 2022: ", len(videos_2022))
    print()

    print_first_and_last(videos_2022)

    print()

    print_top_channels(10, videos_2022, "artists")

    print()

    print_top_item(10, videos_2022, "musics")

    print()