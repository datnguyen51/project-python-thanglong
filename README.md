- python3 -m venv .
- source bin/activate
- git clone https://github.com/datnguyen51/python-home-work.git repo
- cd repo
- pip install -r requirements.txt
- database postgresql
$ sudo -su postgres psql
$ create user dbadmin with password 'admin1234';
$ create database python_project;
$ alter user dbadmin with superuser;

- python3 run.py
