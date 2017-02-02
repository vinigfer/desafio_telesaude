set -x
apt-get update
apt-get install -y python3 python3-pip git-core libpq-dev postgresql-client
git clone https://github.com/vinigfer/desafio_telesaude.git
cd desafio_telesaude
pip3 install -r requirements.txt
python3 manage.py migrate
