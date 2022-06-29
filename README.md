# Welcome to the AirBnB clone project!
# 0x00. AirBnB clone - The console

## Command interpreter to manage AirBnB objects.
## What’s a command interpreter?

It’s exactly the Shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object


## Technologies
* Python interpreter `python3 version 3.8.5`
* Python code use `pycodestyle (version 2.8.*)`
* Tested on `Ubuntu 20.04 LTS`

## Tasks
Each task is linked and will help to:

* Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances
* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all our classes and storage engine


| Filename | Description |
| -------- | ----------- |
| `tests/` | Directory containing unit testing for all the project files. |
| `models/base_model.py, models/__init__.py` | `models` folder containing `__init__.py` empty file and `base_model.py` module defining the first class `BaseModel` that defines all common attributes/methods for other classes. |
| `models/engine/file_storage.py` | Class `FileStorage`  that serializes instances to a JSON file and deserializes JSON file to instances. |
| `console.py` | Program called `console.py` that contains the entry point of the command interpreter. |
| `models/user.py` | class `User` that inherits from `BaseModel`. |
| `models/state.py` | Class `State` that inherit from `BaseModel`. |
| `models/city.py` | Class `City` that inherit from `BaseModel`. |
| `models/amenity.py` | Class `Amenity` that inherit from `BaseModel`. |
| `models/place.py` | Class `Place` that inherit from `BaseModel`. |
| `models/review.py` | Class `Review` that inherit from `BaseModel`. |
| `console.py, models/engine/file_storage.py` | Update `FileStorage` to manage correctly serialization and deserialization of all new classes: `Place`, `State`, `City`, `Amenity` and `Review`. Update your command interpreter (`console.py`) to allow those actions: show, create, destroy, update and all with all classes created previously. |

### Advanced
| Filename | Description |
| -------- | ----------- |
| `console.py` | Update command interpreter (`console.py`) to retrieve all instances of a class by using: `<class name>.all()`. |
| `console.py` | Update command interpreter (`console.py`) to retrieve the number of instances of a class: `<class name>.count()`. |
| `console.py` | Update command interpreter (`console.py`) to retrieve an instance based on its ID: `<class name>.show(<id>)`. |
| `console.py` | Update command interpreter (`console.py`) to update an instance based on his ID: `<class name>.update(<id>, <attribute name>, <attribute value>)`. |
| `console.py` | Update command interpreter (`console.py`) to update an instance based on his ID with a dictionary: `<class name>.update(<id>, <dictionary representation>)`. |
| `tests/test_console.py` | Unittests for all `console.py` features!. |
