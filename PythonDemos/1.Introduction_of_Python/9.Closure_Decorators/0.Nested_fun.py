
def outer():
    msg = "outer"
    def inner():
        msg = "inner"
        print(msg)
    inner()
    print(msg)
outer()