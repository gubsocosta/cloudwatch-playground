FROM mysql:8.4

COPY ./create-testing-database.sh /docker-entrypoint-initdb.d/10-create-testing-database.sh

RUN chmod 755 /docker-entrypoint-initdb.d/10-create-testing-database.sh
