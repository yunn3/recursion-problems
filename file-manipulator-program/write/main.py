pathname = "test.txt"
contents = ""

with open(pathname) as f:
    contents = f.read()

with open(pathname, "w") as x:
    f.write(contents + "\n123")
