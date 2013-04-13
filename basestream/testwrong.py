from basestream import uniformstream

print([x for x in uniformstream(3,(int(x) for x in '10001000011100010101000111'))])
