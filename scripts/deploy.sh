# Run from root of git repo.
rm -rf public_api/zappa_package.zip
docker exec -it public_api bash -c "/usr/src/scripts/create_zappa_package.sh"
docker cp public_api:/usr/src/public_api/zappa_package.zip ./public_api/zappa_package.zip
echo ' --> Manual Step Required:'
echo '      zappa update -s ./public_api/zappa_settings.json -z ./public_api/zappa_package.zip'
