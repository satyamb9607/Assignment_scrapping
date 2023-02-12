# Assignment
## Prerequesties
python >= 3.7 <br />
pip <br />
node js <br />

## Backend

for Backend first create the virtual enviornment and then activate it. Install the dependencies.
### Following commands
### For running the django server
python manage.py runserver <br />
### For migrations
Python manage.py makemigrations <br />
python manage.py migrate <br />

### For running the scrapping service
If u have redis server installed in the use the celery otherwise use the python script in the backend folder

### For Celery
### Use this inside the backend folder
celery -A assignment beat -l info <br />
celery -A assignment worker -l info --pool=solo <br />


### if u don't have redis server try the Scrapping_script.py using python
python Scrapping_script.py  <br />

## For react
Run these commands inside the frontend folder

### for Start the react app
npm run start <br />

### for creating the build
npm run build  <br />

### For installing the dependencies
npm i <br />
