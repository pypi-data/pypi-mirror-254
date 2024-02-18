import honyx

path = './examples/wikispeedia_top100.ngram'

sequences = honyx.read_sequences(path)

print(len(sequences))

fon1 = honyx.generate_hon(sequences, "fix-order", max_order = 1)
von = honyx.generate_hon(sequences, "variable-order")

pr_fon1 = honyx.pagerank_hon(fon1)
pr_von = honyx.pagerank_hon(von)

print('Top 10 Wikipedia articles according to order-1 network')
sorted_pr_fon1= {k: v for k, v in sorted(pr_fon1.items(), key=lambda item: item[1], reverse=True)[:10]}
for item, val in sorted_pr_fon1.items():
	print(f'{item} : {val}')
print('')
print('Top 10 Wikipedia articles according to variable-order network')
sorted_pr_von = {k: v for k, v in sorted(pr_von.items(), key=lambda item: item[1], reverse=True)[:10]}
for item, val in sorted_pr_von.items():
	print(f'{item} : {val}')