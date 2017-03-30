# Desafio Telessaúde

Repositório para a prova técnica de vaga no projeto Telessaúde UFRGS. Código em Python Django, com deploy para Heroku, Docker, e VirtualBox (usando Ansible). Distribuído livremente sobre licença MIT.

Requisitos:
- Acesso admin/sudo para instalar pacotes caso os mesmos não estejam instalados
- Docker (versão 1.13.0+)
- Docker Compose (versão 1.10.1+)
- Vagrant (versão 1.9.1+)
- Ansible (versão 2.2.1.0+)
- Python (versão 3.4.3+)
- Python pip3 (versão 1.5.4+)
- Heroku CLI para rodar migrations dentro do Heroku (versão 5.6.14+)

Como executar o projeto:
- Usando Docker
    * Abra um terminal, acesse o diretório Docker do projeto, e execute ```docker-compose up -d```
    * Abra o seu navegador e digite ```http://localhost:8000/```
- Usando Vagrant, VirtualBox e Ansible
    * Abra um terminal, acesse o diretório Vagrant do projeto, e execute ```vagrant up```
    * Abra o seu navegador e digite ```http://localhost:8000/```
- Localmente (sem VMs ou containers)
    * Abra um terminal, e no diretório do projeto execute ```sudo ./install.sh```
    * Execute ```python3 manage.py runserver```
    * Abra o seu navegador e digite ```http://localhost:8000/```

Limitações:
- Usando Docker ou Vagrant/Ansible, ao destruir os containers/VMs todos os dados são perdidos.
- Ao usar Vagrant, assume-se que o endereço de rede 192.168.1.147 está disponível para criar VM com o database. Se o mesmo nao estiver disponível ou o computador estiver em outra faixa de rede, escolha outro endereço disponível e atualize Vagrantfile e playbook_web.yml
- Testado apenas em ambiente Ubuntu 14.04, mas deve funcionar em versões posteriores ou debian-like.
