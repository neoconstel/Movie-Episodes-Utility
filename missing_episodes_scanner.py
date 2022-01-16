
from episode_renamer import get_rename_map
import os


def report_missing_episodes():
    output_file = 'missing_episodes.txt'

    episode_digits = get_rename_map(desired_title="n/a", 
                                                    output="episode-digits")
    missing_episodes = []
    missing_count = 0

    # convert each entry to actual integer
    episode_digits = list(map(lambda x:int(x), episode_digits))

    first_episode = min(episode_digits)
    last_episode = max(episode_digits)

    for i in range(first_episode, last_episode):
        if i not in episode_digits:
            missing_count += 1
            missing_episodes.append(i)

    # overwrite the file with the output
    with open(output_file, 'w') as file:
        file.write(f'first episode: {first_episode}\n')
        file.write(f'last episode: {last_episode}\n')
        file.write(f'number of missing episodes: {missing_count}\n')
        if missing_count:
            file.write(f'\n{"-" * 30} missing episodes {"-" * 30}\n')
        
        for i in missing_episodes:
            file.write(f'episode {i}\n')

    # open the output file
    try:
        os.system(f"xdg-open {output_file}")
    except:
        print("Not a unix system")
        

if __name__ == "__main__":
    report_missing_episodes()
    