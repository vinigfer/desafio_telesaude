set -x
apt-get update
apt-get install -y python3 python3-pip git-core libpq-dev postgresql-client
git clone https://github.com/vinigfer/desafio_telessaude.git
cd desafio_telessaude
pip3 install -r requirements.txt
