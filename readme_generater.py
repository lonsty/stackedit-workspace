import json
import os
import time
from urllib.parse import quote

import click

INTRO = """# What's this?
A workspace from [https://stackedit.io](https://stackedit.io/), where you can edit the markdown file and sync to this repository.

## Index
"""


def input_reader(ipt, field='input'):
    if os.path.isfile(ipt):
        with open(ipt, 'r') as f:
            text = json.loads(f.read())
    elif field == 'input_file':
        try:
            text = json.loads(ipt)
        except Exception:
            print(f'Error: <{field}> must be a JSON file or STRING!')
            return False
    else:
        text = ipt

    return text


def generate_readme_for_stackedit(input_file="stackedit.json", output_file='README.md', prefix=INTRO, suffix=''):
    input_file = input_reader(input_file, field='input_file')
    if input_file is False:
        print('Exit due to no input.')
        return
    
    prefix = input_reader(prefix, field='prefix')
    suffix = input_reader(suffix, field='suffix')
    
    cata = []
    content = prefix or ''
    tree = sorted(input_file['tree'], key=lambda x: x['path'].lower(), reverse=False)
    
    for item in tree:
        path = item.get('path')

        if "docs/" in path:
            c = path[5]
            if c.upper() not in cata:
                content += f'\n### {c}\n\n'
                cata.append(c)
            content += f'- [{path[5:]}]({quote(path)})\n'
    
    content += suffix or ''
    
    with open(output_file, 'w') as f:
        f.write(content)
    print(f"{'- - ' * 10}{time.ctime()}{' - -' * 10}")
    print(content)
    

@click.command(help='Automatic index generation for StackEdit.')
@click.option('-i', '--input', 'input_file', default='stackedit.json', show_default=True, help='Input')
@click.option('-o', '--output', 'output_file', default='README.md', show_default=True, help='Output')
@click.option('--prefix', 'prefix', default=INTRO, show_default=True, help='Prefix')
@click.option('--suffix', 'suffix', default='', show_default=True, help='suffix')
def automatic_index(input_file, output_file, prefix, suffix):
    generate_readme_for_stackedit(input_file, output_file, prefix, suffix)
    

if __name__ == '__main__':
    automatic_index()
