import re
from glob import glob
import os
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass
class State:

    previous:str
    current:str


if __name__ == '__main__':

    os.chdir(r'C:\Users\assof\test1\sr_sel')
    sub_path = Path(os.getcwd()) / 'complete'

    filenames = glob("*.md")

    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    tomorrow_str = tomorrow.strftime('%Y-%m-%d')
        
    
    sr_lines = []

    for filename in filenames:

        state = State(previous=None, current=None)
        with open(filename) as f1:
            words_lines = f1.readlines()
            selected_lines = []
            for line in words_lines:

                # 단어인 경우
                if ':::' in line:

                    state.current = 'word'
                    current_word = line

                elif '!--SR' in line:

                    state.current = 'sr_line'
                    sr_lines.append(line)

                if (state.previous == 'sr_line') and (state.current == 'word'):
                    
                    # 그간의 평가결과 취합
                    sr_line_str = ''.join(sr_lines)

                    if tomorrow_str in sr_line_str:
                        selected_lines.append(previous_word)
                        sr_lines = []

                if state.current == 'word':
                    previous_word = current_word

                state.previous = state.current
            
            selected_lines_str = ''.join(selected_lines)

            with open(str(sub_path) + '/' + filename.split('.')[0]+'_m.md', mode = 'w') as f2:
                f2.write(selected_lines_str)
