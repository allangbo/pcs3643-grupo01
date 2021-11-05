Para executar o sistema de leilão (diretório eAuction):

1) Instalar mysql através do pip install pymysql

2) O nome do banco é dbleilao, usuario: root, senha: admin (essas configurações podem ser modificadas em settings.py)

3) Criar um super usuário para gerência inicial do sistema através do comando: python manage.py createsuperuser

4) Rodar o comando: python manage.py makemigrations

5) Rodar o comando: python manage.py migrate