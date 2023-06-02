#!/bin/bash

# Aguardar a disponibilidade do servidor PostgreSQL
until psql -h localhost -U "$CHALLENGE_INTENTION_DB_USER" -c '\q'; do
  echo "Aguardando o servidor PostgreSQL..."
  sleep 1
done

# Executar o script SQL para criar o banco de dados
psql -h localhost -U "$CHALLENGE_INTENTION_DB_USER" -d "$CHALLENGE_INTENTION_DB_NAME" -f /docker-entrypoint-initdb.d/create_database.sql
