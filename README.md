# Desafio Telesaúde

Repositório para a prova técnica de vaga no projeto Telesaúde UFRGS. Código em Python Django, com deploy para Heroku, Docker, e VirtualBox (usando Ansible). Distribuído livremente sobre licença MIT.

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
    * Acesse o diretório Docker do projeto e execute ```docker-compose up -d```
- Usando Vagrant, VirtualBox e Ansible
    * Acesse o diretório Vagrant do projeto e execute ```vagrant up```
- Localmente (sem VMs ou containers)
    * 

Limitações:
- Testado apenas em ambiente Ubuntu 14.04, mas deve funcionar em versões posteriores ou debian-like.
