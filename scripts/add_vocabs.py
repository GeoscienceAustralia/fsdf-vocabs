from pathlib import Path
import os

vocabs_list = Path('vocabularies').glob('*.ttl')
vocabs_list = [str(p) for p in vocabs_list]

for vocab in vocabs_list:
    os.system(f"python scripts/update_vocabs.py -a {vocab}")