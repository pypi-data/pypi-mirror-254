def version_to_tuple(version, sep='.'):
    array = []
    for x in version.split(sep):
        try:
            x = int(x)
        except ValueError:
            pass
        array.append(x)
    return tuple(array)
