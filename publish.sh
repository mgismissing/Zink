cleanup.sh &&
poetry export -f requirements.txt --output requirements.txt &&
poetry publish --build &&
rm -rf dist