1. Start with cloneing the withoutDatabase branch
```
python manage.py startapp proto3
```
  _ copy paste templates folder from proto1 to proto3
  _ copy paste urls.py file from proto1 to proto3
  _ copy paste veiws.py file from proto1 to proto3
2. check in settings.py
   _ check "Installed apps" variabe , add proto3 in installed apps
   _ If there are other proto apps , comment them
   _ Create a new database inn pgadmin 4 ,give name test4 make youself the owner.
2.1 go to urls.py in dbms folder
  _ add in urlspatterns 
  ```
    path('', include("proto1.urls")),
  ```

3. from the basic_models.py file outside copy paste all the classes as it is in models.py of proto3
4. ```
   python manage.py makemigrations proto3
   python manage.py migrate
   python manage.py createsuperuser
   ```

NOTE: If you can use your previous user , that we created in canteen , it means your database is not changed , you'll have to check settings.py again
