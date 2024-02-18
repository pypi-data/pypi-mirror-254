import honyx



sequences = [['a','d','e'],
             ['a','d','e'],
             ['d','e'],
             ['b','d','e'],
             ['b','d','e'],
             ['b','d','e'],
             ['d','f'],
             ['d','f'],
             ['b','d','f'],
             ['b','d','f'],
             ['b','d','f'],
             ['b','d','f'],
             ['b','d','c'],
             ['b','d','c'],
             ['b','d','c'],
             ['c','d','c'],
             ['c','d','c'],
             ['c','d','c']]

fon1 = honyx.generate_hon(sequences, "fix-order", max_order = 1, min_support = 1)
print('FON 1')
for n, d in fon1.nodes(data=True):
    print(f'{n} : {d}')
    for e in fon1.out_edges(n, data=True):
        print(f'    {e[1]} : {e[2]}')
rt_prob1 = honyx.average_round_trip(fon1)
print(f' Fon1 avg round trip prob : {rt_prob1}')


fon2 = honyx.generate_hon(sequences, "fix-order", max_order = 2, min_support = 1)
print('FON 2')
for n, d in fon2.nodes(data=True):
    print(f'{n} : {d}')
    for e in fon2.out_edges(n, data=True):
        print(f'    {e[1]} : {e[2]}')
rt_prob2 = honyx.average_round_trip(fon2)
print(f' Fon2 avg round trip prob : {rt_prob2}')