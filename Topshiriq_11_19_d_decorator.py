# import time
#
#
# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f" {func.__name__} took {end_time - start_time:.2f} seconds to execute")
#         return result
#
#     return wrapper
#
#
# @timer_decorator
# def some_function():
#     a = 0
#     for i in range(99999999):
#         a += 5
#     return a / 5
#
#
# c = some_function()
# print(c)


n, count = 5, 0
for _ in range(n):
    n -= 1
    count += 1
print(count)