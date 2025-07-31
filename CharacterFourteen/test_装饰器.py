def outer(func):
    def inner():
        print("I'm sleeping")
        func()
        print("I'm waking up")

    return inner

@outer
def sleep():
    import random
    import time
    print("sleeping......")
    time.sleep(random.randint(1, 5))

sleep()