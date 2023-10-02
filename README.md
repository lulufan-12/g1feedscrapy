# Crawler do Feed G1

Crawler para pegar os dados do [feed de tecnologia  do G1](https://g1.globo.com/rss/g1/tecnologia) e persistir em um banco de dados não relacional (MongoDB).

## Requisitos

Instalar todas as dependências mencionadas abaixo:

[Docker](https://www.docker.com/products/docker-desktop/)  
[Docker Compose](https://docs.docker.com/compose/install/)  
[Python](https://www.python.org/downloads/)  
[Scrapy](https://scrapy.org/download/)  
[Pymongo](https://www.mongodb.com/docs/drivers/pymongo/)  
[Decouple](https://pypi.org/project/python-decouple/)  

## Instrução de Utilização

1 - Na pasta do projeto, inicie o arquivo docker-compose.yaml para criar um banco de dados básico para teste.

```commandline
docker-compose up -d
```

2 - Aguarde um tempo até que o banco de dados esteja operacional.

3 - Crie um arquivo chamado '.env' no diretório g1feed e adicione os valores das variáveis de ambiente do banco de dados conforme o arquivo '.env.example'

4 - Em seguida, execute o comando do scrapy para executar o Spider, fazer a varredura do feed e persistir os dados no banco.

```commandline
scrapy runspider g1feed/spiders/G1FeedSpider.py
```

5 - Acesse o banco de dados via Mongo Express ou qualquer outro cliente de sua escolha e valide os dados que foram persistidos.