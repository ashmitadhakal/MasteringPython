

def outer(func):
    print("outer")

    def inner(msg2):
        print("inner")
        func(msg2)
    
    return inner

#outer()

def cool(msg):
    print(msg)
fn = outer(cool)
fn("fun")