def hello():
    print("Hello")


print(hello)  # print function address
hi = hello  # assign mem. addr. of hello to hi
print(hi)
hi()  # call hi()

say = print
say("Amazing...")
