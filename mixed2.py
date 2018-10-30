dlevel = 0

def main():
    r = range(11)
    l = [1, 'two', 3, {'4': 'four'}, 5]
    t = ('one', 'two', None, 'four', 'five')
    s = set('It`s a bird! It`s a plane! It`s a superman!')
    d = dict(one = r, two = l, three = s)
    mixed = [l, r, s, d, t]
    disp(mixed)

def disp(o):
    global dlevel
    
    dlevel += 1
    if isinstance(o, list): print_list(o)
    elif isinstance(o, range): print_list(o)
    elif isinstance(o, tuple): print_tuple(o)
    elif isinstance(o, set): print_set(o)
    elif isinstance(o, dict): print_dict(o)