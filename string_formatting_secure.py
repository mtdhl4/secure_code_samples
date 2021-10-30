CONFIG = {
  "API_KEY": "771df488714111d39138eb60df756e6b"
}
 
class Person(object):
  def __init__(self, name):
    self.name = name
 
def print_nametag(format_string, person):
  return format_string.format(person=person)
 
person = Person("Vickie")
 
# Okay call that will print: Hi, my name is Vickie. I am a Person.
greeting = print_nametag("Hi, my name is {person.name}. I am a {person.__class__.__name__}.", person)
print(greeting)
 
# Malicious call: the format may be read as a user input:
# print_nametag(input("Please format your nametag: "), person)
greeting = print_nametag("{person.__init__.__globals__[CONFIG][API_KEY]}", person)
print(greeting)