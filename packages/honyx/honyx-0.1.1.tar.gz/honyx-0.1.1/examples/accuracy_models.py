import honyx
import random

def sampleSequences(sequences, ratio_testing):
	'''
	Cut sequences into training and testing subsets

	Parameters:
		sequences: list(list(str))

	Returns:
		build_seqs: list(list(str))
		test_seqs : list(list(str))
	'''
	build_seqs = []
	test_seqs  = []
	for i in range(len(sequences)):
		if random.random() < ratio_testing:
			test_seqs.append(sequences[i])
		else:
			build_seqs.append(sequences[i])
	return build_seqs, test_seqs


path = './examples/US_flights.ngram'

sequences = honyx.read_sequences(path)

ratio_test = 0.1
nb_test = 20

m_fon1, m_fon2, m_von = 0., 0., 0.
for _ in range(nb_test):
    train, test = sampleSequences(sequences, ratio_test)
    print(len(train))
	
    fon1 = honyx.generate_hon(train, "fix-order", max_order = 1)
    fon2 = honyx.generate_hon(train, "fix-order", max_order = 2)
    von  = honyx.generate_hon(train, "variable-order")

    acc_fon1 = honyx.likelihood(fon1, test, False, True)
    acc_fon2 = honyx.likelihood(fon2, test, False, True)
    acc_von  = honyx.likelihood(von , test, False, True)
    m_fon1 += acc_fon1 / nb_test
    m_fon2 += acc_fon2 / nb_test
    m_von +=  acc_von  / nb_test
	
print(f'FON1 {fon1.number_of_nodes()} acc {m_fon1}')
print(f'FON2 {fon2.number_of_nodes()} acc {m_fon2}')
print(f'VON  {von.number_of_nodes() } acc {m_von}')
