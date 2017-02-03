set -x
sleep 10
python3 /desafio_telesaude/manage.py migrate
python3 /desafio_telesaude/manage.py runserver 0.0.0.0:8000
