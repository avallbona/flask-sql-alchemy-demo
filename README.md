# flask-sql-alchemy

## requirements

* pipenv or pip
* python 3.6+

## Installation

* clone repo https://github.com/avallbona/flask-sql-alchemy-demo
* change to folder where you cloned the repo
* with pipenv
    * `pipenv install`
    * `pipenv shell`
* with pip
    * python -m venv myenv
    * source bin/activate
    * pip install -r requirements.txt
* `export FLASK_APP=app.py`
* `flask run`

## migrations

* to initializate the migratioins

    `flask db init`
    
* to generate the needed migrations

    `flask db migrate`
    
* to apply the generated migrations

    `flask db upgrade`

* to unapply the applied migrations

    `flask db downgrade`
