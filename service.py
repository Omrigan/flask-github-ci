from flask import Flask
from plumbum import local, FG


app = Flask(__name__)
directory='/home/oleg/gotosite'

def run_by_dir(path):
    local.cwd.chdir(path)
    local['git']['pull'] & FG
    local['docker-compose']['build']['--no-cache'] & FG
    local['docker-compose']['up']['-d'] & FG



@app.route('/goto-push',  methods=['GET', 'POST'])
def push_hook():
    run_by_dir(directory)
    return 'OK'
if __name__=='__main__':
    app.run()
