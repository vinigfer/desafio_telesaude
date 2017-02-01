FROM ubuntu:14.04

ADD configure.sh /root/configure.sh
RUN /root/configure.sh
#Inicia App django quando o container terminar de subir. Importante adicionar 
#0.0.0.0:8000, do contrario o container acessa apenas localhost interno
CMD python3 /desafio_telesaude/manage.py runserver 0.0.0.0:8000
