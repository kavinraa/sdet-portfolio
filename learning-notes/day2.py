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


def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# twoSum([2,7,11,15], 9)

def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums :
        if num in seen :
            return True
        seen.add(num)
    return False

    
# print(containsDuplicate([1,2,3,5]))
# print(containsDuplicate([1, 2, 3, 1])) 


