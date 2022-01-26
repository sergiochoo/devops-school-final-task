# Start app locally
Clone this repo.

```
python3 -m venv venv
. venv/bin/source
pip install -r requirements.txt
python manage.py migrate
```

## Run
`python manage.py migrate`

# Sync
http://127.0.0.1:8000/residents/sync/

# Report
http://127.0.0.1:8000/residents/report/

# After updating models schema
```
python manage.py makemigrations
python manage.py migrate
```