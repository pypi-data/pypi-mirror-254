import argparse
import urllib.request

FILES = {
    'Dockerfile': 'https://gitlab.com/cloud-colosseum/ez/-/raw/main/cx/Dockerfile',
    'cloudbuild.yaml': 'https://gitlab.com/cloud-colosseum/ez/-/raw/main/cx/cloudbuild.yaml',
    'main.py': 'https://gitlab.com/cloud-colosseum/ez/-/raw/main/cx/main.py'
}

class EZ_CLI:

    def __init__(self):
        self.command_tree = {
            'generate': {
                'scaffolding': self.__scaffolding,
                'quickstart': self.__quickstart
            }
        }
        self.parser = self.setup_parser()

    def setup_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers()
        generate = subparsers.add_parser('generate')
        generate_subparsers = generate.add_subparsers(dest='generate')
        for subcmd in self.command_tree['generate']:
            generate_subparsers.add_parser(subcmd)
        return parser

    def __scaffolding(self):
        files = {'Dockerfile', 'cloudbuild.yaml'}
        for file, url in FILES.items():
            if file not in files:
                continue
            print(f'[ez-cli]: downloading {file}')
            with open(file, 'wb') as dest, urllib.request.urlopen(url) as response:
                dest.write(response.read())
        print()

    def __quickstart(self):
        files = {'Dockerfile', 'cloudbuild.yaml', 'main.py'}
        for file, url in FILES.items():
            if file not in files:
                continue
            print(f'[ez-cli]: downloading {file}')
            with open(file, 'wb') as dest, urllib.request.urlopen(url) as response:
                dest.write(response.read())

    def __call__(self):
        args = self.parser.parse_args()
        subp = self.command_tree['generate'].get(args.generate)
        subp()

cli = EZ_CLI()


