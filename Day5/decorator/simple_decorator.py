

TAP_INTERNSITY = 2
def tap(move):
    def tap_move_fn(x):
        print("insider def_move_tap")
        result= move(x,TAP_INTERNSITY)
        print("called move function")
        return result
    
    return tap_move_fn

@tap
def left(a,b):
    return a-b
@tap
def right(a,b):
    return a+b

# tap_left = tap(left)
# tap_right = tap(right)

# print(tap_left(2))
# print(tap_right(3))

print(left(2))
print(right(3))
