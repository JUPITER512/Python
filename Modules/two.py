import one
print("TOP LEVEL TWO.py")
one.func()
if __name__ == '__main__':
    print("TWO IS DIRECTLY RUNNING from __name__")
else:
    print("TWO IS IMPORTED  ")
