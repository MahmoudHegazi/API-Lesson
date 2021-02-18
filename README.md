# API-Lesson

1. no env needed
2. mkdir [project folder] inside it new folder with name [flaskr] inside it create the __init__.py
3. cd project_folder 
4. ```export FLASK_APP=flaskr```
5. ```export FLASK_ENV=development```
6. ```flask run```
7. very important  create_app it's not optional name it's required 


# notes:
* if you saw this error sqlalchemy.exc.OperationalError  fe_sendauth: no password supplied (problem in the postgres path missing something)

#### CURL USED IN GITBASH for windows CMD deal with error and check windows command below

# CURL post example 


### Data json with post 

1. ```curl -X POST 'http://localhost:5000/post' -d '{"data":"Hello World"}' -H 'Content-Type: application/json'``` (This not in CMD use in Gitbash)
2. in __init__ ```request.get_json(force=True)```

### data json with Post CMD
1. ```curl localhost:5000/post --data "{\"data\": \"bar\"}" -H 'Content-Type: application/json'``` (for unkown reason after work will return error)
2.  Even who created CMD can not solve this error "barcurl: (6) Could not resolve host: application" np use it in GitBash
3. if not content type use ```request.get_json(force=True)```


### data form curl request
1. ``` curl -X POST 'http://localhost:5000/form' --form-string 'hello=world'```
2. in py ```x = request.form['hello']```


### upload file with curl
1. ```curl -X POST -F thename=@the.txt http://localhost:5000/file```
2. in py ```file = request.files['thename'] filename=secure_filename(file.filename) ```


### some bash exp 
1. to make var in bash you do not have to use spaces : x='hello world'  echo $x
2. to store curl in var x=`curl https://pokeapi.co/api/v2/move/47` echo $x

### some hard bash
1. to get a specific value from curl you need to install jq first chocolatey install jq ```chocolatey install jq```
2. example of command to get first value you can change 0 with another index  
*  return with index ```curl 'https://pokeapi.co/api/v2/move/47' | jq '[.[] ] | .[0]'```


### get specific value with name 

1.  return direct value ```curl 'https://pokeapi.co/api/v2/move/47' | jq '[.["accuracy"] ][0]'```  
2. or return all the array ``` curl 'https://pokeapi.co/api/v2/move/47' | jq '[.["accuracy"] ]'```


### Patch Request Curl
1.  ```curl http://127.0.0.1:5000/books/8 -X PATCH -H "Content-Type:application/json" -d '{"rating":"3"}'```


### Successful API test Without any problems
1. ![api test](https://github.com/MahmoudHegazi/API-Lesson/blob/main/my_api_test.JPG?raw=true)


### secure API from scraper and abusers (We can not gma will return our mac noob internet)
1. if some one exceed API limit block his mac address 
2. IF you need scrape site blocked you just restart the router
```
from getmac import get_mac_address as gma
print(gma())
```

## unit test notes

1. create another Database with same tables and insert some data to make your tests
2. in py2 use this to send json data in request the_data = json.dumps(dict(search='worngbook'))
3. big important not if result = 0 even if True it will equal to false
4. dont use assertTrue if u know the result is false
5. if query will return empty list do not test it direct test the len or just add [] ```self.assertEqual(data['books'],[])``` or ```self.assertEqual(len(data['books']),0)```
