a = 8
b = 0
try:
    print("Resource open")
    print(a/b)
    print("Resource Closed")
except Exception as e:
    print("Hey, Error due to ZERO in divisable:", e)
finally:
    print("Resouce Closed")

print("Bye")