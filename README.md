# Assignment
## Prerequesties
python >= 3.7
pip
node js

## Backend

for Backend first create the virtual enviornment and then activate it. Install the dependencies.
### Following commands
### For running the django server
python manage.py runserver
### For migrations
Python manage.py makemigrations
python manage.py migrate

### For running the scrapping service
If u have redis server installed in the use the celery otherwise use the python script in the backend folder

### For Celery
### Use this inside the backend folder
celery -A assignment beat -l info
celery -A assignment worker -l info --pool=solo


### if u don't have redis server try the Scrapping_script.py using python
python Scrapping_script.py 

## For react
Run these commands inside the frontend folder

### for Start the react app
npm run start

### for creating the build
npm run build 

### For installing the dependencies
npm i