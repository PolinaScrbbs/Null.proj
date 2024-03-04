python -m venv .venv

$acctivateScript = ".\.venv\Scripts\Activate.ps1"

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata fixture/all_fixture