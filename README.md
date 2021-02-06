# API-Lesson

1. no env needed
2. mkdir [project folder] inside it new folder with name [flaskr] inside it create the __init__.py
3. cd project_folder 
4. ```export FLASK_APP=flaskr```
5. ```export FLASK_ENV=development```
6. ```flask run```
7. very important  create_app it's not optional name it's required 


# CURL post example


### Data json with post 

1. ```curl -X POST 'http://localhost:5000/post' -d '{"data":"Hello World"}' -H 'Content-Type: application/json'```
2. in __init__ ```request.get_json(force=True)```


### data form curl request
1. ``` curl -X POST 'http://localhost:5000/form' --form-string 'hello=world'```
2. in py ```x = request.form['hello']```
