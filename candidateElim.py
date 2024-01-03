import csv

training_data = []

with open('trainingexamples.csv') as csv_file:
    for line in csv.reader(csv_file):
        training_data.append(tuple(line))

def create_domain():
    domain = []
    for i in range(len(training_data[0])):
        unique_values = []
        for example in training_data:
            if example[i] not in unique_values:
                unique_values.append(example[i])
        domain.append(unique_values)
    return domain

D = create_domain()

def is_consistent(hypothesis1, hypothesis2):
    for x, y in zip(hypothesis1, hypothesis2):
        if not (x == "?" or (x != "ɸ" and (x == y or y == "ɸ"))):
            return False
    return True

def candidate_elimination():
    general_hypotheses = {('?',)*(len(training_data[0]) - 1),}
    specific_hypothesis = ['ɸ'] * (len(training_data[0]) - 1)
    example_count = 0
    print("\nGeneral Hypotheses:", general_hypotheses)
    print("\nSpecific Hypothesis:", specific_hypothesis)
    
    for example in training_data:
        example_count += 1
        input_values, result = example[:-1], example[-1]
        
        if result in "Yy":  # For positive examples
            i = 0 
            general_hypotheses = {h for h in general_hypotheses if is_consistent(h, input_values)}
            for s, x in zip(specific_hypothesis, input_values): 
                if not s == x:
                    specific_hypothesis[i] = '?' if s != 'ɸ' else x
                i += 1
        else:  # For negative examples
            specific_hypothesis = specific_hypothesis
        previous_general_hypotheses = general_hypotheses.copy()
        for g in previous_general_hypotheses: 
            for i in range(len(g)): 
                if g[i] == "?": 
                    for val in D[i]: 
                        if input_values[i] != val and val == specific_hypothesis[i]: 
                            new_hypothesis = g[:i] + (val,) + g[i+1:]
                            general_hypotheses.add(new_hypothesis)
                else:
                    general_hypotheses.add(g)
        if ('?', '?', '?', '?', '?', '?') in general_hypotheses :
            general_hypotheses.remove(('?', '?', '?', '?', '?', '?'))

        print("\nGeneral Hypotheses:", general_hypotheses)
        print("\nSpecific Hypothesis:", specific_hypothesis)

candidate_elimination()
