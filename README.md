![]
(https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201105T000106Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cadbf3a9ac8419b261d6c28da8da9627cc354334855570eb0cdd7f36d5cd10e7)

# AirBnB Console

This project is a project from foundations year for Holberton School students. The objective of this project is to be an enrichment exerceise to 
improve and applicate the most concepts of higher-level programing done before and consists to do an specific command line interpreter to manage all 
of the functions and features of our HBnB.

### Command interpreter 🧐

This interpreter is capable of doing operations such as:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### Getting started 👩🏽‍💻

At first, you have to clone the repository in your machine

```
$ git clone git@github.com:Andres802/AirBnB_clone.git
```

Go inside to the directory
``` 
$ cd AirBnB_clone
```
Execute the console
```
./console.py
```

### Working 👩🏽‍🔧

Interactive mode
```
$ ./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb) quit
$
```
Non-interactive mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Authors 🙋🏼‍♂️

* **Andrés Barrera** - [Github](https://github.com/Andres802)
* **Laura Castillo** - [Github](https://github.com/laucaslop)

From [Holberton School](https://www.holbertonschool.com/co) ❤️
