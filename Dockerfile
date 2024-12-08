FROM mysql
COPY db/mysqld.cnf /etc/mysql/conf.d
ADD db/init-db.sql /docker-entrypoint-initdb.d
RUN chown mysql:mysql /docker-entrypoint-initdb.d/*.sql
RUN chown mysql:mysql /etc/mysql/conf.d/*.cnf
ENV MYSQL_ROOT_HOST=%
