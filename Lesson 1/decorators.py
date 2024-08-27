def announce(f):
    def wrapper():
        print("\nAbout to run the function...")
        f()
        print("Done with the function.\n")
    return wrapper

@announce
def hello():
    print("Hello world")
    print("Hello me")

@announce
def ending():
    print("trying End")

hello()
ending()