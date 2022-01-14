
from distutils import extension
import episode_parser
import re

episodes_directory = ""

video_formats = [
	'mp4','avi','mov','3gp','vob','rmvb','wmv','flv','swf','webm','mkv'
]

def get_video_extension(filename:str):
    dot_extension = filename[filename.rindex("."):] # e.g .mp4
    extension = dot_extension[1:] # e.g mp4
    if extension in video_formats:
        return dot_extension
    return None

# get all the filenames to give something like this 
# (taking only files with video formats -- recognized by file extension)
episodes = [
    "fairytale 0101.mp4",
    "fairytale 0102.rmvb",
    "fairytale 0103.mp4",
    "fairytale s01ep04.mp4",
    "fairytale s01ep17.mp4",
]

renamed_episodes = []  # not in the same order as the original episode names

desired_title = "FairyTail"

result = episode_parser.parse_episodes(episodes=episodes)
print("\n\n")
for pattern, pattern_positions in result:
    for index, episode in enumerate(episodes):
        match = re.match(pattern, episode)
        if match:
            new_title = f"{desired_title} - "
            video_extension = get_video_extension(episode)

            for position in pattern_positions:
                episode_digit = match.group(position + 1)
                new_title += episode_digit

            # add the extension to the filename
            new_title += video_extension

            # safety measure to ensure no duplicate name entries that can 
            # cause file overwrites
            if new_title not in renamed_episodes:
                renamed_episodes.append(new_title)
            print(new_title)
    print(f"Pattern: {pattern},  Positions: {pattern_positions}")


print("\n\nRenamed episodes:")
for each in renamed_episodes:
    print(each)

print(f"\nNumber of original episodes: {len(episodes)}")
print(f"Number of renamed episodes: {len(renamed_episodes)}")
if len(episodes) != len(renamed_episodes):
    print("Renaming conflicts present. Abort renaming process.")
else:
    print("No renaming conflicts. Renaming can safely proceed")
    # proceed to carry out actual renaming of files