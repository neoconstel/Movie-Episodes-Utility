
import re
from episodeparse_ui import EpisodeParseUi   

# get all the filenames and remove the extension to give something like this
episodes = [
    "fairytale 0101.mp4",
    "fairytale 0102.mp4",
    "fairytale 0103.mp4",
    "fairytale s01ep04.mp4",
    "fairytale s01ep05.mp4"
]

patterns = []

for episode in episodes:
    regex = ""

    for c in episode:
        if c.isdigit():
            regex += "(\d)"
        else:
            regex += "\D"

    if regex not in patterns:
        patterns.append(regex)
    print(f"{episode} ---> {regex}")

# convert regex patterns into compiled regex
patterns = list(map(re.compile, patterns))

print("\n\npatterns:")
for pattern in patterns:
    print(pattern)

pattern_positions = []

print("\n\nsample_matches:")
for pattern in patterns:
    for episode in episodes:
        match = re.match(pattern, episode)
        if match:
            print(f"Sample: {match.group()},  Numbers: {match.groups()}")
            # pattern_position = get_episode_positions()
            pattern_position = []
            gui = EpisodeParseUi(episode, gui_output=pattern_position)
            # the ui blocks the code at this point until it is destroyed
            
            pattern_positions.append(pattern_position)
            print(f"Pattern positions: {pattern_positions}")
            break
        
