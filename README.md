# my_airbnb_project
In this project, I clean airbnb data, put the clean data in postgresql db and create and api that serves that data using fast api

## To use the project

1. clone the repository
```
git clone https://github.com/DaliDalmas/my_airbnb_project.git
```
2. activate python 3.9.9 using pyenv. Ensure python 3.9.9 is installed in pyenv
```
pyenv local 3.9.9
```
3. create a python virtual environment
```
python -m venv venv
```
4. activate the virtual environment
```
source venv/bin/activate
```
5. Install the requirements
```
pip install -r requirements.txt
```

## To use the notebooks for cleaning
1. activate the virtual environment you created above
```
source venv/bin/activate
```
2. launch jupyter lab
```
jupyter lab
```
3. open the notebooks
4. ...

## To use the api
1. ensure you have the clean data in a postgresql database
2. create connection parameters file `connection_params.py` that contains user of that database and password and put the file in api folder.
3. activate the environment ou created above.
```
source venv/bin/activate
```
4. run the api
```
uvicorn api.main:app --reload
```
5. access the data.