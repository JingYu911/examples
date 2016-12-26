def rename(name):
    if len(name) == 3:
        name = '0' + name + '.jpg'
    elif len(name) == 2:
        name = '00' + name + '.jpg'
    elif len(name) == 1:
        name = '000' + name + '.jpg'
    else:
        name = name + '.jpg'
    return name
