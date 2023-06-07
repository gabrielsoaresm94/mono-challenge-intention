# Como rodar o projeto
Necessário ter docker e docker compose na máquina, dependendo da versão o comando `docker-compose up` pode ser rodado como `docker compose up` e logo depois rodar as migrations:

```bash
docker-compose up

docker exec -it intentions-service bash -c "flask db upgrade"
```

## Acessando serviços de APIs
Para rodar o projeto acessar a documentação do Swagger, lá tem as informações para rodar os endpoint lá mesmo, ou em outra aplicação caso prefira

```
http://localhost:5000/v1/docs/
http://localhost:3001/v1/docs/
```

## Caso os comandos falhem:
Outra maneira de iniciar a aplicação é com o próprio docker, sem a necessidade de composer:

```bash
docker build -t intentions-service ./intentions
docker build -t products-service ./products

docker network create challenge-intention-network

docker run -d --name intentions-service --network=challenge-intention-network -p 5000:5000 -v ./intentions/src:/app --env-file .env intentions-service

docker run -d --name products-service --network=challenge-intention-network -p 3001:3001 -v ./products:/app products-service

docker run -d --name challenge-intention-db --network=challenge-intention-network -p 5432:5432 -v challenge-intention-db:/var/lib/postgresql/data -e POSTGRES_PASSWORD=${CHALLENGE_INTENTION_DB_PASSWORD} -e POSTGRES_USER=${CHALLENGE_INTENTION_DB_USER} -e POSTGRES_DB=${CHALLENGE_INTENTION_DB_NAME} postgres:12

# docker run -d --name challenge-intention-messenger --network=challenge-intention-network -p 5672:5672 -p 25676:25676 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=${CHALLENGE_INTENTION_MESSENGER_USER} -e RABBITMQ_DEFAULT_PASS=${CHALLENGE_INTENTION_MESSENGER_PASS} rabbitmq:3-management

docker exec -it intentions-service bash -c "flask db upgrade"
```

## Ordem para testar a aplicação

1. Criar cliente, necessita de nome e um endereço;
2. Ler produtos;
3. Buscar produto (não é obrigatório);
4. Cria uma intenção de compra, necessita do identificador do cliente, do identificar do endereço do cliente e dos identificadores dos produtos;
5. Listar intenções de compra;