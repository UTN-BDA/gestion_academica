# Software Gestion Academica
## COMO FUNCIONA
- 1. Clonar el siguiente repositorio con el siguiente link: https://github.com/UTN-BDA/gestion_academica con el comando git clone
- 2. Una vez descargado ingresar desde un entorno como puede ser Visual Studio Code
- 3. IMPORTANTE | Descargar / tener instalado DOCKER DESKTOP
- 4. Crear un archivo .env dentro de la carpeta gestion_academica, el cual tendrá el siguiente formato:
    POSTGRES_DB=main_db
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    POSTGRES_USER=(introduzca su usuario)
    POSTGRES_PASSWORD=(introduzca una contraseña)

    PGADMIN_DEFAULT_EMAIL=admin@admin.com
    PGADMIN_DEFAULT_PASSWORD=admin
- 5. Ejecutar en la terminal los siguientes comandos para levantar los contenedores:
    - docker compose up --build 
    Una vez levantado, abrir otra terminal para crear un superusuario, se deberá poner los siguientes comandos:
    - docker exec -it djangoapp /bin/bash
    - python manage.py createsuperuser
    - A continuacion se le pediran datos como usuario, mail y contraseña, el cual queda a su disposición
- 6. Para verificar el funcionamiento visitar los siguientes sitios:
    1) localhost:8000 (Pagina inicial de la app, con diseña a terminar)
    2) localhost:8000/admin (Panel de administracion, ingresar con las credenciales ingresadas en el paso N°5)
    3) localhost:5050 (Panel de PgAdmin para visualizar la base de datos) 
        SE INGRESA CON LAS CREDENCIALES QUE SE ENCUENTRAN EN EL ARCHIVO .ENV
        Para registrar la BD:
        1) registrar servidor: ((esto se encuentra definido en las variables de entorno))
            nombre del servidor: opcional
            host: db
            puerto: 5432
            user: user
            password: password


## Team Members:

- Alvarado, Matias
- Diaz, Agustin
- Godoy, Santiago
- Marin, Franco
- Valdivieso, Gabriel

## Technologies

- Python
- Django
- Bootstrap
- PostgreSQL
- Docker