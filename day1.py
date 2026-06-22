# part 1 : variables and data types

name = "Kavin"
age = 28
is_employed = True
salary = 100357.50

print((type(name)))
print((type(age)))
print((type(is_employed)))
print((type(salary)))

greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

employment_status = f"I am currently {'employed' if is_employed else 'not employed'}."
print(employment_status)

print(f"My salary is ${salary:,.2f}")

# ---------------------------------------------------------------------------------------------
# part 2 : if/else comparisons 
score = 80
if score >= 90:
	print("Pass - excellent")
elif score >= 70:
	print("Pass - acceptable")
else:
	print("Fail")

status = "pass" if score >= 70 else "fail"
print(f"test status: {status}")

# ---------------------------------------------------------------------------------------------
# part 3 : for loops
test_names = ["login_test", "logout_test", "signup_test", "payment_test"]
for test in test_names:
    print(f"running : {test}")

for i, test in enumerate(test_names):
    print(f"Test {i + 1}: {test}")
	
results = [True, True, False, True]
passed = [t for t,r in zip(test_names, results) if r]
print(f"passed tests : {passed}")
# ---------------------------------------------------------------------------------------------
# part 4 : functions
def greet(name):
    return (f"Hello, {name}!")
 
def add(a,b):
    return a + b

def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]

def is_valid_email(email):
    #   there must be exactly 1 "@" symbol
    if email.count("@") != 1:
        return False
    
    #  split into username and domain 
    username, domain = email.split("@")

    #  neither username nor domain can be empty
    if not username or not domain :
         return False
    
    #  domain must contain a dot and it can't be at the start or end
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False


print(greet("Kavin"))
print(add(5,10))
print(is_valid_email("test@.yopmail"))
print(is_valid_email("notanemail"))      

# ---------------------------------------------------------------------------------------------

