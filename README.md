
Sistema Eventos Curso WTTD

## Como Desenvolver

1. Clone o Repositório
2. Crie uma Virtualenv
3. Ative a Virtualenv
4. Instalar Dependências
5. Configure a instância no arquivo .env
6. Execute os Testes

```console
git clone https://github.com/pcego/wttd.git wttd2
cd wttd2
python -m venv .wttd2
source .wttd2/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```


## Como Fazer Deploy

1. Crie uma instância no Heroku
2. Envie as Configurações par o Heroku
3. Defina uma SECRET_KEY para a instância
4. defina DEBUG=False
5. Configure o serviço de Email
6. Envie o código para o Heroku

```console
heroku create minhaInstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
# Configure Email
git push heroku master --force
```

