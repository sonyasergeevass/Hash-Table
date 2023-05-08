def multipl(key, size):
    rndnum = 0.4689432983
    r = key * rndnum
    r = r - int(r)
    return int(r * size)


def hash_function_ost(key, size):
    return key % size


def hash_fun_additive(key, size):
    summ = 0
    nkey = key
    while nkey > 0:
        ost = nkey % 10
        summ += ost
        nkey //= 10
    return summ % size

def hash_fun_square(key):
    k = len(str(key))
    keys = str(key*key)
    if 2*k == len(keys):
        return int(keys[k-2:k+2])
    else:
        zero = 2*k - len(keys)
        add = '0'*zero
        finalk = add + keys
        return int(finalk[k-2:k+2])

def type_of_hash(num_method, key, size):
    if num_method == 1:
        return hash_function_ost(key, size)
    elif num_method == 2:
        return hash_fun_additive(key, size)
    elif num_method == 3:
        return hash_fun_square(key)
    else:
        return multipl(key, size)

print(hash_function_ost(10, 89))
print(hash_fun_additive(10, 5))
print(hash_fun_square(4))
print(hash_fun_square(7))


