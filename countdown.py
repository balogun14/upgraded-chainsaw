from traceback import print_tb


def countdown(x):
    """
    docstring
    """
    if x ==0:
        print('done')
        return
    else:
        print(x,'...')
        countdown(x-1)
        
countdown(5)