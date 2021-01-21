# API de um CRUD de conta corrente


<p>REST API feita utilizando Django REST framework.</p>

<h1>
    <a href="https://www.django-rest-framework.org/">🔗 Django REST framework</a>
</h1>
<p >🚀 lib para construir REST API's de maneira rápida</p>

Recursos utilizados:
=================
  <ul>
    <li>Python 3.8.5</li>
    <li>Django REST framework 3.12.2</li>
    <li>SQLite 3</li>
  </ul>
<br>

Tabela de conteúdos
=================
* [Recursos utilizados](#recursos)
* [Tabela de conteúdos](#tabela-de-contéudos)
* [Iniciando a aplicação](#inciando-a-aplicação)
* [Rotas da aplicação](#rotas-da-aplicação)
* [Funções da aplicação](#funções-da-aplicação)

Iniciando a aplicação
=================
No terminal, clone a aplicação:
```bash
$ git clone https://github.com/xandeft/API-REST-Django.git
```
Entre na pasta da aplicação
```bash
$ cd API-REST-Django
```
Inicie a virtual env:
```bash
$ source ./env/bin/activate
```
Inicie a aplicação, usando:
```bash
$ python manage.py runserver
```

Pronto, agora é possível acessar a aplicação a partir da rota http://localhost:8000/api/contas

![Screenshot from 2021-01-21 01-23-36](https://user-images.githubusercontent.com/57076602/105279935-6cdbf880-5b87-11eb-85cd-02fd0aa4be4b.png)
<br>

Rotas da aplicação
=================
Todas as rotas do aplicação estão contidas no arquivo urls.py que está na pasta myapi.
![Screenshot from 2021-01-21 01-15-57](https://user-images.githubusercontent.com/57076602/105279469-58e3c700-5b86-11eb-8f40-2eb870b09ed4.png)
<br>
PS: A primeira rota da imagem é a mesma que você usa para acessar a aplicação assim que se inicia.

Funções da aplicação
=================
Na rota http://localhost:8000/api/contas, você consegue as informações (id, número da conta e saldo) de todas as contas existentes.
```bash
$ curl --location --request GET 'localhost:8000/api/contas/'
```
Nesta rota http://localhost:8000/api/contas/create, você consegue criar uma nova conta. Dos campos que constituem a "Conta", o único obrigatório a ser passado é o número da conta, onde a uma validação deste número para não termos números de contas repetidas. O campo id é gerado automaticamente, e o campo saldo é iniciado por padrão sendo 0.00. 
```bash
$ curl --location --request POST 'localhost:8000/api/contas/create' \ --form 'accountNumber="1000"'
```
Na rota http://localhost:8000/api/contas/detail/{número-da-conta}, é retornada as informações sobre a conta específica a ser consultada.
```bash
$ curl --location --request GET 'localhost:8000/api/contas/detail/1000'
```
A função de atualização da conta é relacionado ao saldo da conta, no qual existe duas funcionalidades sobre esse dado, a de depositar e a de debitar valores da conta.
Nesta rota http://localhost:8000/api/contas/update/{número-da-conta}/deposit/{valor}, é possível adicionar um quantia no saldo de cada conta.
```bash
$ curl --location --request PUT 'localhost:8000/api/contas/update/1000/deposit/10' \
--form 'accountNumber="1000"'
```
Já nesta http://localhost:8000/api/contas/update/{número-da-conta}/debit/{valor}, é possível debitar um valor da conta desejada. Mas antes de debitar ele valida se a conta possuí saldo maior ou igual ao que quer ser debitado.
```bash
$ curl --location --request PUT 'localhost:8000/api/contas/update/1000/debit/10' \
--form 'accountNumber="1000"'
```
Por fim na rota http://localhost:8000/api/contas/delete/{número-da-conta}, dá a possibilidade de deletar uma conta a partir do seu número.
```bash
$ curl --location --request DELETE 'localhost:8000/api/contas/delete/1000'
```
