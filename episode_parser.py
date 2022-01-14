
import re
from episodeparse_ui import EpisodeParseUi   

def parse_episodes(episodes) -> list:
    
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

    all_pattern_positions = []  # same length as patterns

    print("\n\nsample_matches:")
    for pattern in patterns:
        for episode in episodes:
            match = re.match(pattern, episode)
            if match:
                print(f"Sample: {match.group()},  Numbers: {match.groups()}")
                pattern_positions = []
                gui = EpisodeParseUi(episode, gui_output=pattern_positions)
                # the ui blocks the code at this point until it is destroyed
                
                all_pattern_positions.append(pattern_positions)
                print(f"All pattern positions: {all_pattern_positions}")
                break
    return list(zip(patterns, all_pattern_positions))