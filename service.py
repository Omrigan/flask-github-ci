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
        local['docker-compose']['build']['--no-cache'] & FG
        local['docker-compose']['up']['-d'] & FG



t = Thread(target=run_by_dir, args=(directory,))
@app.route('/goto-push',  methods=['GET', 'POST'])
def push_hook():
    execute=True
    if not t.isAlive():
        t.start()
    # run_by_dir(directory)
    return 'OK'
if __name__=='__main__':
    app.run()
