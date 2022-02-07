def outer():
    msg = "outer"
    
    def inner():
        nonlocal msg
        msg = "inner"
        print(msg)
    return inner


output = outer()
print(outer.__closure__)
print(output.__closure__[0].cell_contents)