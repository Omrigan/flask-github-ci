#Github docker CI
Simple script allows you to update your docker-compose project on every git push
##Installation
1. `git clone https://github.com/Omrigan/flask-github-ci/`
1. `cd flask-github-ci`
1. `pip3 install -r requirements.txt`
1. Change value of `directory` variable to locate root folder of your compose project
1. Change path in startup.sh and add it to startup (for example, in rc.local)
1. Set up github webhooks on 'push' event to yourdomain.com:8005
1. Execute startup.sh once