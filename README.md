# Software Gestion Academica

## Miembros del equipo:

- Alvarado, Matias
- Diaz, Agustin
- Godoy, Santiago
- Marin, Franco
- Valdivieso, Gabriel

## Tecnologias

- Python
- Django
- Bootstrap
- PostgreSQL
- Docker

## Instalacion
### Clonar repositorio ejecutando los siguientes comandos en la terminal:
```
git clone https://github.com/UTN-BDA/gestion_academica.git
cd gestion_academica
```
### Definir las siguientes variables de entorno en un archivo .env
```
    POSTGRES_DB=main_db
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password

    PGADMIN_DEFAULT_EMAIL=admin@admin.com
    PGADMIN_DEFAULT_PASSWORD=admin
```
### Levantar los contenedores:
```
docker compose up -d --build
```
En caso de ver el siguiente error: djangoapp  | exec /app/run.sh: no such file or directory
Ingresar desde Visual Studio Code al archivo run.sh y cambiar en la parte inferior derecha del formato CRLF a LF. Luego reintentar levantar los contenedores.
-  Crear superusuario para panel de administracion
```
docker exec -it djangoapp /bin/bash
python manage.py createsuperuser
```
### Ver el funcionamiento de la aplicacion en los siguientes sitios:
- **Pagina principal**: `localhost:8000`
- **Panel de administracion**: `localhost:8000/admin` 
    * Iniciar sesion con las credenciales de superusuario
- **Panel de pgadmin**: `localhost:5050` 
    * Iniciar sesion con las credenciales *PG_ADMIN* definidas en el archivo .env
    * Registrar servidor con las credenciales definidas en el archivo .env:
    ```
        name: <opcional>
        host name: db
        port: 5432
        username: user
        password: password
    ```