import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Function {} took {:.6f} seconds to execute".format(func.__name__, end_time - start_time))
        return result
    return wrapper

@timer
def sum_numbers(a, b):
    time.sleep(1) # simulate some processing time
    result = a + b
    print("The sum of {} and {} is {}".format(a, b, result))

@timer
def read_and_sum_numbers():
    with open("input.txt", "r") as f:
        a = int(f.readline())
        b = int(f.readline())
    result = a + b
    with open("output.txt", "w") as f:
        f.write(str(result))
    print("The sum of {} and {} has been written to output.txt".format(a, b))

# example usage
sum_numbers(5, 10)
read_and_sum_numbers()