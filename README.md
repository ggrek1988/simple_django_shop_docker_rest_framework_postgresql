# Django Shop 

## **Tools**
Project is created with:
* Python 3.0
* asgiref==3.4.1
* Django==3.2.7
* djangorestframework==3.12.4
* psycopg2==2.9.1
* pytz==2021.1
* sqlparse==0.4.2

## **Run**

uruchomienie serwera:

    python manage.py runserver

budowanie projektu

    django-admin startproject Django_sklep

budowanie kategorii

    python manage.py startapp Produkty

zaakceptowanie/przebudowanie modelu w pliku models.py

    python manage.py makemigrations
    python manage.py migrate

listuje wszystkie pakiety potrzebne do uruchomienia projektu

    pip freeze 
################################################################################
1) Listing available containers 
    docker ps
2) to enter container
    
    docker exec -it {id} bash

3) to rebuild container  
    
    docker-compose build {nazwa}

4)  start project containers
    
    docker-compose up

#tworzenie superusera
    
    python manage.py createsuperuser

   
