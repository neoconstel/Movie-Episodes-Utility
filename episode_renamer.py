

import episode_parser
import re
import os
import json
from video_definitions import *

episodes_directory = os.getcwd()
log_file = "rename_log.json"


def get_rename_map(desired_title, output="default"):

    # get all the filenames,
    # (taking only files with video formats -- recognized by file extension)
    episodes = {}
    all_episode_digits = []

    for dirpath, dirnames, filenames in os.walk(episodes_directory):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            # only files in the episodes_directory, not in any sub-directory
            if full_path == os.path.join(episodes_directory, filename):            
                path_video_extension = get_video_extension(full_path)
                # only video formats
                if path_video_extension:
                    print(f"Adding file '{filename}' as episode \
                                        from path: {full_path}")
                    # add the video filename into the episodes dictionary
                    episodes[filename] = None

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
                if int(episode_digits) < 10 \
                                    and not episode_digits.startswith("0"):  
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
                    all_episode_digits.append(episode_digits)
                print(new_title)
        print(f"Pattern: {pattern},  Positions: {pattern_positions}")
    if output == "episode-digits":
        return all_episode_digits
    else:
        return episodes  # default behaviour


def rename_episodes(desired_title, log_file=log_file):
    episodes = get_rename_map(desired_title)

    print("\n\n----Expected Renaming Result----")
    for episode, new_name in episodes.items():
        print(f"{episode}   ---- renames to ---->     {new_name}")


    # final safety check to ensure no duplicate or Null names will be given

    print(f"\nNumber of original episodes: {len(episodes)}")
    # total elements in values - number of null values
    num_renamed_episodes = len(episodes.values()) \
                            - sum(1 for v in episodes.values() if v == None)
    print(f"Number of renamed episodes: {num_renamed_episodes}")

    if len(episodes) != num_renamed_episodes:
        print("Renaming conflicts present. Abort renaming process.")
    else:
        print("No renaming conflicts. Renaming can safely proceed")
        # proceed to carry out actual renaming of files
        for episode, new_name in episodes.items():
            os.rename(episode, new_name)

        # keep a record mapping each old name to its new name
        with open(log_file, "w") as log:
            json.dump(episodes, log)


def unrename_episodes(log_file=log_file):
    if not os.path.exists(log_file):
        print("No record of previous renaming found")
        return

    with open(log_file) as log:
        rename_map = json.load(log)
    
    # do the actual unrenaming
    for old_name, new_name in rename_map.items():
        try:
            os.rename(new_name, old_name)
        except:
            if not os.path.exists(new_name):
                print(f"could not rename {new_name} to {old_name} because \
                the file: {new_name} not found")
            else:
                print(f"could not rename {new_name} to {old_name} for unknown \
                    reason")

    # delete the log_file since renaming has been reversed
    os.remove(log_file)
    