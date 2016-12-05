def print_Hijos(_hijos, _tag):

    # import ipdb; ipdb.set_trace()

    # Obter hijos:
    _tag += "--"

    for hijo in _hijos:
        print "{} Hijo: {}".format(_tag, hijo)
        hijos = Equipo.objects.filter(padre=hijo)
        if len(hijos) > 0:
            print_Hijos(hijos, _tag)

    return None


daddies = Equipo.objects.filter(padre=None)
tag = "--"

for daddy in daddies:

    print "Padre: {}".format(daddy)
    hijos = Equipo.objects.filter(padre=daddy)
    print_Hijos(hijos, tag)
