find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
rm -rf zappa_package/ zappa_package.zip
