# Get to root of Git repo (for me: /Users/hunter/workspace/dg-internals)
rm -rf /usr/src/public_api/zappa_venv/
cd /usr/src/public_api/
pip3 install virtualenv
python3 -m venv zappa_venv
source ./zappa_venv/bin/activate
pip install --upgrade pip
pip3 install zappa
pip3 install -r /usr/src/public_api/requirements.txt
zappa package -s ./zappa_settings.json --output /usr/src/public_api/zappa_package.zip
exit 0