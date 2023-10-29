def announce(f):
    def wrapper():
        print("Beginning")
        f()
        print("Ending")
    return wrapper
@announce
def hello():
    print("main")
hello() 