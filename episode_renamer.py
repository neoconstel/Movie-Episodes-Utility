
import re
from ui import Ui


def get_episode_positions():
    positions = []
    while True:
        position = (input("Enter next episode position (counting from 1): "))
        if position.isdigit():
            positions.append(int(position))
        elif position:
            print("Enter only digits!")
            return None
        else:
            if positions:
                return positions
            else:
                return None

# print(get_episode_positions())
# exit()
        

episodes = [
    "fairytale 0101",
    "fairytale 0102",
    "fairytale 0103",
    "fairytale s01ep04",
    "fairytale s01ep05"
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
            pattern_position = get_episode_positions()
            pattern_positions.append(pattern_positions)
            print(f"Pattern positions: {pattern_position}")
            break
