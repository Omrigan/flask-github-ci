from flask import Flask
from plumbum import local, FG
from threading import Thread

app = Flask(__name__)
directory = '/home/oleg/example'
execute = True


def run_by_dir(path):
    global execute
    while execute:
        execute = False
        local.cwd.chdir(path)
        g = local['git']
        dc = local['docker-compose']
        gs = g['submodule']
        g['pull'] & FG
        dc['build'] & FG
        dc['up']['-d'] & FG
        gs['update'] & FG
        print('Finished build')


t = Thread(target=run_by_dir, args=(directory,))


@app.route('/goto-push', methods=['GET', 'POST'])
def push_hook():
    global execute, t
    execute = True
    if not t.isAlive():
        t = Thread(target=run_by_dir, args=(directory,))
        t.start()
    return 'OK'


if __name__ == '__main__':
    app.run(port=8005)
