import getpass

def cli():
    msg = f'Running missionctl as {getpass.getuser()}.'
    print(msg)
    print('You are running an outdated version of missionctl - please contact platform@missioncloud.com for assistance.')


if __name__ == '__main__':
    cli()
