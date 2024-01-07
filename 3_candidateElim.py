import csv

training_examples = []

with open('trainingexamples.csv') as csv_file:
    for line in csv.reader(csv_file):
        training_examples.append(tuple(line))

def create_domain():
    domain = []
    for i in range(len(training_examples[0])):
        unique_values = []
        for example in training_examples:
            if example[i] not in unique_values:
                unique_values.append(example[i])
        domain.append(unique_values)
    return domain

attribute_domain = create_domain()

def is_consistent(hypothesis1, hypothesis2):
    for attribute_value1, attribute_value2 in zip(hypothesis1, hypothesis2):
        if not (attribute_value1 == "?" or (attribute_value1 != "ɸ" and (attribute_value1 == attribute_value2 or attribute_value2 == "ɸ"))):
            return False
    return True

def candidate_elimination():
    general_hypotheses = {('?',)*(len(training_examples[0]) - 1),}
    specific_hypothesis = ['ɸ'] * (len(training_examples[0]) - 1)
    example_count = 0
    print("\nGeneral Hypotheses:", general_hypotheses)
    print("\nSpecific Hypothesis:", specific_hypothesis)
    
    for example in training_examples:
        example_count += 1
        input_values, result = example[:-1], example[-1]
        
        if result in "Yy":  # For positive examples
            attribute_index = 0 
            general_hypotheses = {h for h in general_hypotheses if is_consistent(h, input_values)}
            for specific_value, input_value in zip(specific_hypothesis, input_values): 
                if not specific_value == input_value:
                    specific_hypothesis[attribute_index] = '?' if specific_value != 'ɸ' else input_value
                attribute_index += 1
        else:  # For negative examples
            specific_hypothesis = specific_hypothesis
        previous_general_hypotheses = general_hypotheses.copy()
        for general_hypothesis in previous_general_hypotheses: 
            for attribute_index in range(len(general_hypothesis)): 
                if general_hypothesis[attribute_index] == "?": 
                    for value in attribute_domain[attribute_index]: 
                        if input_values[attribute_index] != value and value == specific_hypothesis[attribute_index]: 
                            new_hypothesis = general_hypothesis[:attribute_index] + (value,) + general_hypothesis[attribute_index+1:]
                            general_hypotheses.add(new_hypothesis)
                else:
                    general_hypotheses.add(general_hypothesis)
        

        print("\nGeneral Hypotheses:", general_hypotheses)
        print("\nSpecific Hypothesis:", specific_hypothesis)

candidate_elimination()
