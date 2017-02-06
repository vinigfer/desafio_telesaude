sudo apt-get update
sudo apt-get install -y python3 python3-pip git-core libpq-dev postgresql postgresql-client
sudo pip3 install -r requirements.txt
sudo sed -i '1 i\127.0.0.1      database' /etc/hosts
sudo -u postgres psql -c "CREATE USER usuario WITH PASSWORD 'senha';"
sudo -u postgres psql -c "CREATE DATABASE telesaude;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE telesaude TO usuario;"
python3 manage.py migrate
