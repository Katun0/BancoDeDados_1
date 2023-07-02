# PHP + MySQL + Docker

### Configurando & Executando Ambiente
`docker compose up` no shell dentro da pasta  root do projeto. 

> Se tiver erro: `Fatal error: Uncaught Error: Call to undefined function mysqli_report() in /var/www/html/services/conexoes.php:5 Stack trace: #0 /var/www/html/consulta.php(2): require_once() #1 {main} thrown in /var/www/html/services/conexoes.php on line 5`
> 
> Abra o terminal interativo com o container que está rodando o serviço `www` (`docker exec -it bd-1-crud-php-mysql-www-1 "bash"`) e execute o comando: `docker-php-ext-install mysqli && docker-php-ext-enable mysqli && apachectl restart`

