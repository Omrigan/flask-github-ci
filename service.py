from flask import Flask
from plumbum import local, FG
from threading import Thread

app = Flask(__name__)
directory='/home/oleg/gotosite'
execute=True
def run_by_dir(path):
    global execute
    while execute:
        execute = False
        local.cwd.chdir(path)
        local['git']['pull'] & FG
        local['docker-compose']['build'] & FG
        local['docker-compose']['up']['-d'] & FG
        print('Finished')


t = Thread(target=run_by_dir, args=(directory,))
@app.route('/goto-push',  methods=['GET', 'POST'])
def push_hook():
    global execute
    execute=True
    global t
    if not t.isAlive():
        t = Thread(target=run_by_dir, args=(directory,))
        t.start()

    # run_by_dir(directory)
    return 'OK'
if __name__=='__main__':
    app.run()
