# tapp-project
Timesheet app for HHOM

To install python packages:
* Create Conda Environment
```
conda create --name tapp-project python=3.6
source activate tapp-project
```

* Install packages:
```
pip install -r requirements.txt
```

CD into ./project_tapp 
`cd project_tapp` 

Make migrations before running server
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Access admin site at http://127.0.0.1:8000/admin
