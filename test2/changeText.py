
import re
from glob import glob
import os
from pathlib import Path


if __name__ == '__main__':

    os.chdir(r'C:\Users\assof\test1\test2')
    sub_path = Path(os.getcwd()) / 'complete'

    filenames = glob("*.txt")

    ptrn_meaningless_words = ['(\n[^A-Za-z][0-9 \-\n]*[0-9]+)[a-zA-Z]*', '능률보카 어원편']
    ptrn_symbol_words = '( *G[1-4-]+ T4 U[0-9]+[\s\S]*?\n*)(?=(n|adv|v|adj)\.)'
    ptrn_symbol_words_92_93 = '( *G[\S]* U[0-9]+[\s\S]*?\n*)(?=(n|adv|v|adj)\.)'

    for filename in filenames:
        with open(filename) as f1:
            content = f1.read()
            for word in ptrn_meaningless_words:
                content = re.sub(word, '', content)
            if '92' in filename or '93' in filename:
                content = re.sub(ptrn_symbol_words_92_93, '::: ', content)
            else:
                content = re.sub(ptrn_symbol_words, '::: ', content)

            with open(str(sub_path) + '/' + filename.split('.')[0]+'_m.txt', mode = 'w') as f2:
                f2.write(content)

