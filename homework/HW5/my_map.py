def my_map(func, lst):
    if not lst:
        return []
    return [func(lst[0])] + my_map(func, lst[1:])

def my_filter(func, lst):
    if not lst:
        return []
    if func(lst[0]):
        return [lst[0]] + my_filter(func, lst[1:])
    else:
        return my_filter(func, lst[1:])

def my_reduce(func, lst, initial):
    if not lst:
        return initial
    return my_reduce(func, lst[1:], func(initial, lst[0]))

def bubble_pass(lst):
    if len(lst) <= 1:
        return lst
    
    if lst[0] > lst[1]:
        return [lst[1]] + bubble_pass([lst[0]] + lst[2:])
    else:
        return [lst[0]] + bubble_pass(lst[1:])

def bubble_sort_no_loop(lst):
    return my_reduce(lambda acc, _: bubble_pass(acc), lst, lst)