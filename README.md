# AirBnB clone
Created By: [Tatiana Fernández](https://github.com/Titania792), [Agustina Hernández](https://github.com/MoonBeeJPG)
### Welcome to our AirBnB clone project!
![HBNB](https://github.com/Titania792/pictures-for-projects/blob/master/hbnb.png)
In this occasion we have to deploy in our own server a simple copy of the AirBnB website to cover all fundamental concepts of the higher level programming track.

### What’s a command interpreter?
Do you know about the Shell? Well this is exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object

## Using our console

First you need to clone our repository...
```
$ git clone https://github.com/Titania792/holbertonschool-AirBnB_clone.git
```
### Easy explaining:
To iniciate our command interpreter you must have to execute our file called console.py with _"python3"_ after that you would see Holberton's prompt _"(hbnb) "_  and from that point you would be inside our console. Here you can execute differents customized commands, to know which ones are able and how do they work you can type the command _"help"_ to show all commands or help followed with one of the options to know how it works  _"help [command]"_.

![Console Example](https://github.com/Titania792/pictures-for-projects/blob/master/console%20example.png)

### Detailed explaining:
After cloning the repository you can use the console in two ways:
- Interactive mode:
```
>>> ./console.py
(hbnb) help

Documented commands (type help <topic>):
==================================================
EOF help quit create show destroy all update count

(hbnb) 
(hbnb) 
(hbnb) quit
```
- Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb) 

Documented commands (type help <topic>):
==================================================
EOF help quit create show destroy all update count
(hbnb) 
$
$ cat test_help
help
$
$ cast test_help | ./console.py
(hbnb) 

Documented commands (type help <topic>):
==================================================
EOF help quit create show destroy all update count
(hbnb) 
$
```
## Examples of command usage

### Create Command
```
root@c272c925f1e0:~/holbertonschool-AirBnB_clone# ./console.py
(hbnb) create User
d0304991-04b8-44a9-982c-0c40832b44b9
(hbnb)
```
### All Command
```
(hbnb) all
["[BaseModel] (6c8f5503-22e7-4265-91c6-b073c499faa6) {'id': '6c8f5503-22e7-4265-91c6-b073c499faa6', 'created_at': datetime.datetime(2022, 7, 4, 5, 47, 12, 722957), 'updated_at': datetime.datetime(2022, 7, 4, 5, 47, 12, 723681), 'name': 'My First Model', 'my_number': 89}", "[User] (ddade81b-4d5a-447a-aac4-f9b9396271e3) {'id': 'ddade81b-4d5a-447a-aac4-f9b9396271e3', 'created_at': datetime.datetime(2022, 7, 4, 10, 25, 26, 705730), 'updated_at': datetime.datetime(2022, 7, 4, 10, 25, 26, 705730)}", "[User] (d0304991-04b8-44a9-982c-0c40832b44b9) {'id': 'd0304991-04b8-44a9-982c-0c40832b44b9', 'created_at': datetime.datetime(2022, 7, 4, 7, 4, 36, 345662), 'updated_at': datetime.datetime(2022, 7, 4, 7, 4, 36, 345674)}"]
(hbnb)
```
### Show Command
```
(hbnb) show User d0304991-04b8-44a9-982c-0c40832b44b9
[User] (d0304991-04b8-44a9-982c-0c40832b44b9) {'id': 'd0304991-04b8-44a9-982c-0c40832b44b9', 'created_at': datetime.datetime(2022, 7, 4, 7, 4, 36, 345662), 'updated_at': datetime.datetime(2022, 7, 4, 7, 4, 36, 345674)}
(hbnb)
```
### Destroy Command
```
(hbnb) destroy User d0304991-04b8-44a9-982c-0c40832b44b9
(hbnb) show User d0304991-04b8-44a9-982c-0c40832b44b9
** no instance found **
(hbnb)
```

## Contact us: 
- [Tatiana Fernández](https://www.linkedin.com/in/tatiana-fern%C3%A1ndez-846b6a230/)
- [Agustina Hernández](https://www.linkedin.com/in/agustina-hern%C3%A1ndez-5b689a230/)
