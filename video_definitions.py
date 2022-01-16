video_formats = [
	'mp4','avi','mov','3gp','vob','rmvb','wmv','flv','swf','webm','mkv'
]

def get_video_extension(filename:str):
    dot_extension = filename[filename.rfind("."):] # e.g .mp4
    if dot_extension == -1:
        return None
    extension = dot_extension[1:] # e.g mp4
    if extension in video_formats:
        return dot_extension
    return None
    