
import episode_parser
import re

# get all the filenames to give something like this
episodes = [
    "fairytale 0101.mp4",
    "fairytale 0102.mp4",
    "fairytale 0103.mp4",
    "fairytale s01ep04.mp4",
    "fairytale s01ep17.mp4"
]

renamed_episodes = []

desired_title = "FairyTail"

result = episode_parser.parse_episodes(episodes=episodes)
print("\n\n")
for pattern, pattern_positions in result:
    for episode in episodes:
        match = re.match(pattern, episode)
        if match:
            new_title = f"{desired_title} - "

            for position in pattern_positions:
                new_title += match.group(position + 1)

            renamed_episodes.append(new_title)
            print(new_title)
    print(f"Pattern: {pattern},  Positions: {pattern_positions}")


print("\n\nRenamed episodes:")
for each in renamed_episodes:
    print(each)