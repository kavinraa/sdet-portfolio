# Day 2 
# Part 1 — Lists
tests = ["login", "logout", "signup", "payment", "search"]

print(tests[0])
print(tests[-1])
print(tests[1:3])

tests.append("checkout")
tests.insert(0, "homepage")
tests.remove("logout")

print(tests)

print(f"total tests : {len(tests)}")
print(f"is 'login' in suite? {'login' in tests}")

scores = [88, 72, 95, 61, 80]
print(f"highest score : {max(scores)}")
print(f"average score : {sum(scores)/len(scores):.1f}")

passed =[s for s in scores if s >= 80]
print(f"Passed scores : {passed}")

