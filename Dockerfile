FROM mysql:8.0


ENV SQL /web_homework_hw6\


WORKDIR $SQL


COPY . .


EXPOSE 3306

# docker pull maxxbondarenko/hw6
# run -d -p 3306:3306 --name hw6-sql-cont -e MYSQL_ROOT_PASSWORD=pass123 -e MYSQL_DATABASE=students maxxbondarenko/hw6:latest