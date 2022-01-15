

import episode_parser
import re
import os

episodes_directory = os.getcwd()

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

# get all the filenames to give something like this 
# (taking only files with video formats -- recognized by file extension)
# episodes = {
#     "fairytale 011.mp4": None,
#     "fairytale 0101.mp4": None,
#     "fairytale 0102.rmvb": None,
#     "fairytale 0103.mp4": None,
#     "fairytale s01ep04.mp4": None,
#     "fairytale s01ep17.mp4": None
# }

episodes = {}
for dirpath, dirnames, filenames in os.walk(episodes_directory):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        # only files in the episodes_directory, not in any sub-directory
        if full_path == os.path.join(episodes_directory, filename):            
            path_video_extension = get_video_extension(full_path)
            # only video formats
            if path_video_extension:
                print(f"Adding file '{filename}' as episode from path: {full_path}")
                # add the video filename into the episodes dictionary
                episodes[filename] = None


desired_title = "FairyTail"

result = episode_parser.parse_episodes(episodes=episodes.keys())
print("\n\n")
for pattern, pattern_positions in result:
    for episode in episodes.keys():
        match = re.match(pattern, episode)
        if match:
            new_title = f"{desired_title} - "
            video_extension = get_video_extension(episode)
            episode_digits = ""

            # get the episode digits
            for position in pattern_positions:
                episode_digit = match.group(position + 1)
                episode_digits += episode_digit
                
            # 1 will become 01, 9 will become 09 etc
            if int(episode_digits) < 10 and not episode_digits.startswith("0"):  
                episode_digits = f"0{episode_digits}"
            
            new_title += episode_digits

            # add the extension to the filename
            new_title += video_extension

            # safety measure to ensure no duplicate name entries that can 
            # cause file overwrites
            # if new_title not in renamed_episodes:
            #     renamed_episodes.append(new_title)
            if new_title not in episodes.values():
                episodes[episode] = new_title
            print(new_title)
    print(f"Pattern: {pattern},  Positions: {pattern_positions}")


# print("\n\nRenamed episodes:")
# for each in episodes.values():
#     print(each)

print("\n\n----Expected Renaming Result----")
for episode, new_name in episodes.items():
    print(f"{episode}   ---- renames to ---->     {new_name}")


# final safety check to ensure no duplicate or Null names will be given

print(f"\nNumber of original episodes: {len(episodes)}")
# total elements in values - number of null values
num_renamed_episodes = len(episodes.values()) - sum(1 for v in episodes.values() if v == None)
print(f"Number of renamed episodes: {num_renamed_episodes}")

if len(episodes) != num_renamed_episodes:
    print("Renaming conflicts present. Abort renaming process.")
else:
    print("No renaming conflicts. Renaming can safely proceed")
    # proceed to carry out actual renaming of files
    print("\n\n")
    for episode, new_name in episodes.items():
        os.rename(episode, new_name)