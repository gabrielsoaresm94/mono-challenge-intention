FROM postgres:12

# Variáveis de ambiente
ENV POSTGRES_USER="${CHALLENGE_INTENTION_DB_USER}"
ENV POSTGRES_PASSWORD="${CHALLENGE_INTENTION_DB_PASSWORD}"
ENV POSTGRES_DB="${CHALLENGE_INTENTION_DB_NAME}"
ENV PGDATA="/var/lib/postgresql/data"

# Copiar arquivo SQL para criar o banco de dados
COPY create_database.sql /docker-entrypoint-initdb.d/
