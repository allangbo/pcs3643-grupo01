Para executar o sistema de leilão:

1) Entrar no diretório eAuction: cd eAuction

2) Instalar as dependencias atraves do comando: pip install -r requirements.txt

3) O nome do banco é dbleilao, usuario: root, senha: admin (essas configurações podem ser modificadas em settings.py)

4) Comentar as linhas 6 a 11 do arquivo /eAuctions/urls.py 
(para funcionar, comentar com # ou remover as linhas salvando-as em outro lugar para inserí-las novamente no passo 7)

5) Rodar o comando: python manage.py makemigrations

6) Rodar o comando: python manage.py migrate

7) Descomentar as linhas comentadas no passo 4.

8) Criar um super usuário para gerência inicial do sistema através do comando: python manage.py createsuperuser

9) Para rodar o servidor localmente, execute o comando: python manage.py runserver, o servidor estará na porta 8000 do localhost.

10) Para executar os testes automatizados unitários, execute: python manage.py test

11) Os testes de tela se encontram no diretório Documents/05-11-2021, eles pressupõem que o usuário esteja loggado no sistema. Pode-se logar utilizando as credenciais de superusuário criadas no passo 8.
(Há três tipos de usuário: comprador/vendedor; leiloeiro e administrador). O usuário administrador é o único que conseguirá realizar todos os testes pois ele tem acesso a todas as funcionalidades)