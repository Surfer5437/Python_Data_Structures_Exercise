def calculate(op, a, b, make_int=False, message='The result is'):
    if op == "add":
        r=add(a,b,make_int,message)    
    elif op == 'subtract':
        r=subtract(a,b,make_int,message)
    elif op == 'multiply':
        r=multiply(a,b,make_int,message)
    elif op == 'divide':
        r=divide(a,b,make_int,message) 
    else:
        r=None   
    print(r)
    
    # result = op(a,b,make_int,message)
    # return result

def add(x,y,make_int,message):
    if make_int==True:
        x=round(x)
        y=round(y)
    return f'{message} {x + y}'

def subtract(x,y,make_int,message):
    if make_int==True:
        x=round(x)
        y=round(y)
    return f'{message} {x - y}'

def multiply(x,y,make_int,message):
    if make_int==True:
        x=round(x)
        y=round(y)
    return f'{message} {x * y}'

def divide(x,y,make_int,message):
    if make_int==True:
        x=round(x)
        y=round(y)
    return f'{message} {x/y}'


    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
