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
