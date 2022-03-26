from pytube import YouTube

def fetch_yt(url):
    '''creates youtube object with given video url'''
    return YouTube(url)

def fetch_download(stream, is_video, filename, path):
    '''downloads filtered youtube stream object'''
    if stream:
        if is_video:
            stream.download(output_path=path, filename=filename + ".mp4")
        else:
            stream.download(output_path=path, filename=filename + ".mp3")

def fetch_audio(yt, filename, path=None):
    '''filters youtube object to get best quality audio stream'''
    stream = yt.streams.get_audio_only()
    return fetch_download(stream, False, filename, path)

def fetch_video_highest_res(yt, filename, path=None):
    '''filters youtube object to get best quality video stream'''
    stream = yt.streams.get_highest_resolution()
    return fetch_download(stream, True, filename, path)

def fetch_video(yt, filename, res="720p", path=None):
    '''filters youtube object to get video stream of supplied resolution'''
    stream = yt.streams.get_by_resolution(res)
    return fetch_download(stream, True, filename, path)

def fetch_meta(stream):
    '''retrieves metadata of given video stream'''
    return {
        "title": stream.title,
        "thumbnail": stream.thumbnail_url
    }

def execute_yt(url, format, path, name, res):
    '''creates youtube object and downloads filtered stream'''
    yt = fetch_yt(url)
    if format == "mp3":
        return fetch_audio(yt, name, path)
    return fetch_video(yt, name, res, path)

if __name__ == "__main__":
    yt = fetch_yt("https://www.youtube.com/watch?v=LXb3EKWsInQ&t=41s&ab_channel=Jacob%2BKatieSchwarz")
    fetch_video(yt, "test3", "1080p")