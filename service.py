from flask import Flask
from plumbum import local


app = Flask(__name__)
master_directory='~oleg/test'

def run_by_dir(path):
    local.cwd(path)
    local['git']['pull']()
    local['docker-compose']['up']['--build']()



@app.route('goto-push')
def push_hook():
    run_by_dir(master_directory)

if __name__=='__main__':
    app.run()
