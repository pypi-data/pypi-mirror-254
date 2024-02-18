"""Play MP3 files from a directory."""
import contextlib
import os
import sys
import random
import multiprocessing
from playsound import playsound


__version__ = '2024.1.0.0'


def PlaySongs(path: str, repeat: int = 0, shuffle: bool = False) -> str:
    """
    Play MP3 files from a directory.

    return str
    """
    # Create song list.
    try:
        # Create the list of files from a directory of songs.
        file_list = os.listdir(path)
        # Filter list to only include MP3 files.
        song_list = [f'{path}/{i}' for i in file_list if i.endswith('.mp3')]
    
        # Initialize repeat counter.
        counter = 0
        play = True

        print('Press CTRL+C for options')

        # Play all songs and repeat as necessary.
        while counter <= repeat and play:

            try:

                # Shuffle list if necessary.
                if shuffle:
                    random.shuffle(song_list)

                # Play songs.
                for song in song_list:
                    print(f'Playing: {song}...')
                    # Start playing.
                    p = multiprocessing.Process(target = playsound, args = (song, ))
                    p.start()
                    try:
                        while True:
                            if p.exitcode != None:
                                p.terminate()
                                break
                    except KeyboardInterrupt:
                        p.terminate()
                        control = input('Skip() or Exit(x): ')
                        if control in ['x', 'X']:
                            p.terminate()
                            play = False
                            return 'Stopped'
                    except Exception as e:
                        p.terminate()
                        play = False
                        return str(e)

            except KeyboardInterrupt:
                p.terminate()
                play = False
                return 'Stopped'

            except Exception as e:
                with contextlib.suppress(Exception):
                    p.terminate()
                play = False
                return str(e)

            # Increment counter.
            counter += 1
        
        response = 'Done'

    except Exception as e:
        response = str(e)

    return response


def main():
    """Execute module as a script."""
    response = PlaySongs(sys.argv[1])
    print(response)
