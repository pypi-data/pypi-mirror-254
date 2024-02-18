# prototypal

This is an experimental module I created to see if I could get Javascript-like prototypes implemented in Python 3. It's
not Pythonic but it works. Feel free to PR if you want to contribute to it.

## Usage

```python
from prototypal.prototype import *


# create a new type using @constructor
@constructor
def Person(this, first, last):
    this.firstName = first
    this.lastName = last


# initialize an instance
bird = Person('Charlie', 'Parker')
print(bird.firstName)  # Output: 'Charlie'
print(bird.lastName)  # Output: 'Parker'

# dynamically add attributes
bird.instrument = 'alto sax'
print(bird.instrument)  # Output: 'alto sax'

# unset attributes just return None
print(bird.age)  # Output: None


# add methods to the instance
def sing(this):
    print('%s sings!!' % this.lastName)


bird.sing = sing.__get__(bird)
bird.sing()  # Output: 'Parker sings!!'


# use the prototype chain to add properties and methods to the type
def getName(this):
    return '%s %s' % (this.firstName, this.lastName)


Person.prototype.name = property(getName)

print(bird.name)  # Output: 'Charlie Parker'


def greet(this):
    print('Hello, my name is %s' % this.name)


Person.prototype.greet = greet.__get__(bird)
bird.greet()  # Output: 'Hello, my name is Charlie Parker'

monk = Person('Thelonious', 'Monk')
monk.greet = greet.__get__(monk)
monk.greet()  # Output: 'Hello, my name is Thelonious Monk'


# property setter
def setName(this, name):
    first, last = name.split(' ')
    this.firstName = first
    this.lastName = last


Person.prototype.name = property(getName, setName)

bird.name = 'Dizzy Gillespie'
print(bird.firstName)  # Output: 'Dizzy'
print(bird.lastName)  # Output: 'Gillespie'


# property deleter
def deleteName(this):
    print('Deleting %s.' % this.name)
    del this.firstName
    del this.lastName


Person.prototype.name = property(getName, setName, deleteName)
del bird.name  # Output: 'Deleting Dizzy Gillespie.'
print(bird.name)  # Output: 'None None'

# using prototype inheritance
father = Person('Tom', 'Bard')
son = Person('Tommy', 'Bard')
son.__proto__ = father
father.eyeColor = 'blue'
print(son.eyeColor)  # Output: 'blue'

# prototype chain relationships
assert son.__proto__ == father
assert son.constructor == father.constructor == Person
assert father.__proto__ == Person.prototype
assert Object.prototype.constructor == Object
assert Person.prototype.constructor == Person
assert Person.prototype.__proto__ == Object.prototype

# should work with lists
father.children = [son]
print(len(father.children))  # Output: 1

########################################################

# Usage of the new features
# Creating a prototype with attributes
jane = create_prototype(first='Jane', last='Doe')

# Chaining prototypes
parent_proto = create_prototype(eye_color='blue')
child_proto = chain_prototypes(parent_proto)

# Cloning a prototype
clone_jane = clone_prototype(jane)

# Dynamic attribute setting
jane.middle = 'Ann'

# Representation customization
print(jane)  # Output: <Proto object at 0x...>
```