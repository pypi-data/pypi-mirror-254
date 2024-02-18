import unittest
from prototypal.prototype import constructor


# Define the Person constructor for testing purposes
@constructor
def Person(this, first, last):
    this.firstName = first
    this.lastName = last


# Add methods and properties to the Person prototype
def getName(this):
    if hasattr(this, 'firstName') and hasattr(this, 'lastName'):
        return f"{this.firstName} {this.lastName}"
    raise AttributeError("Name attributes are not set.")


def setName(this, name):
    first, last = name.split(' ')
    this.firstName = first
    this.lastName = last


# Define the deleter for the fullName property
def deleteName(this):
    if hasattr(this, 'firstName'):
        del this.firstName
    if hasattr(this, 'lastName'):
        del this.lastName



Person.prototype.getName = getName
# Now, set the fullName property with the proper getter, setter, and deleter
Person.prototype.fullName = property(getName, setName, deleteName)


class TestPrototypeOOP(unittest.TestCase):

    def test_person_initialization(self):
        person = Person("John", "Doe")
        self.assertEqual(person.firstName, "John")
        self.assertEqual(person.lastName, "Doe")

    def test_person_full_name_property(self):
        person = Person("Jane", "Doe")
        self.assertEqual(person.fullName, "Jane Doe")

        person.fullName = "Janet Smith"
        self.assertEqual(person.firstName, "Janet")
        self.assertEqual(person.lastName, "Smith")

        # Delete the fullName and check for AttributeError on firstName and lastName
        del person.fullName
        with self.assertRaises(AttributeError):
            _ = person.firstName
        with self.assertRaises(AttributeError):
            _ = person.lastName

    def test_prototype_inheritance(self):
        father = Person("John", "Doe")
        son = Person("Johnny", "Doe")
        son.__proto__ = father  # Setting the prototype chain

        father.eyeColor = "blue"
        self.assertEqual(son.eyeColor, "blue")

    def test_prototype_method(self):
        person = Person("Jane", "Doe")
        self.assertEqual(person.getName(), "Jane Doe")


# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
