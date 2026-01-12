Objective: Use ChatGPT to document the code

$ cat factorial_recursive.py
#!/usr/bin/python3
import sys

def factorial(n):
        if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)

$ ./factorial_recursive.py 4
24
You can download the code here.

Add the comments to this code.

You should have 3 sections: function description, parameters and returns.