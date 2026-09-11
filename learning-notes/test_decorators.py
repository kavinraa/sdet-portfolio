import time
# Part 1 : decorator
def timer(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = func(*args , **kwargs)
        end = time.time()
        print(f"[{func.__name__} took {end - start:.4f} seconds]")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

# explanation : slow_function = timer(slow_function) == @timer /n def slow_function():

print(slow_function())

# Part 2 — Context managers:

class Timer:
    def __enter__(self):
        self.start = time.time()
        print(f"\n[Initiating timer]")
        return self

    def __exit__(self, exc_type, exc, tb):
        elapsed = time.time() - self.start
        print(f"[Elapsed : {elapsed:.4f}s]")

with Timer():
    time.sleep(1)
    print("[Doing work...]")