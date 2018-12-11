def hello(fn):
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodbyte, %s" % fn.__name__)
    return wrapper

@hello
def Philip():
    print("i am Philip Tung")

Philip()
