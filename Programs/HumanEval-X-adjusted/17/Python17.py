import ast
import sys
from typing import List


def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]
if __name__ == "__main__":
    n = sys.argv[1]
    result = parse_music(n)
    result = list(result)
    print(result)
