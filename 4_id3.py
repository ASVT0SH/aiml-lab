def information_gain(positive_count, negative_count):
    import math
    total_instances = positive_count + negative_count
    if total_instances == 0:
        return 0
    positive_ratio = positive_count / total_instances
    negative_ratio = negative_count / total_instances
    return -positive_ratio * math.log2(positive_ratio) - negative_ratio * math.log2(negative_ratio)

def insert_node(tree, add_to, node_value):
    for key, value in tree.items():
        if isinstance(value, dict):
            tree[key] = insert_node(value, add_to, node_value)
    if add_to in tree:
        if isinstance(tree[add_to], dict):
            tree[add_to][node_value] = 'None'
        else:
            tree[add_to] = {node_value: 'None'}
    return tree

def insert_concept(tree, add_to, concept_value):
    for key, value in tree.items():
        if isinstance(value, dict):
            tree[key] = insert_concept(value, add_to, concept_value)
    if add_to in tree:
        tree[add_to] = concept_value
    return tree

def get_next_node(data, attribute_list, concept, concept_values, tree, add_to):
    total_instances = data.shape[0]
    if total_instances == 0:
        return tree

    count_by_concept = {}
    for c_value in concept_values:
        data_by_concept = data[data[concept] == c_value]
        count_by_concept[c_value] = data_by_concept.shape[0]

    if count_by_concept[concept_values[0]] == 0:
        tree = insert_concept(tree, add_to, concept_values[1])
        return tree

    if count_by_concept[concept_values[1]] == 0:
        tree = insert_concept(tree, add_to, concept_values[0])
        return tree

    class_entropy = information_gain(count_by_concept[concept_values[1]], count_by_concept[concept_values[0]])
    attribute_values = {}
    for attribute in attribute_list:
        attribute_values[attribute] = list(set(data[attribute]))

    attribute_counts = {}
    entropy_by_attribute = {}
    for attr in attribute_values:
        for val in attribute_values[attr]:
            for c in concept_values:
                data_by_attr = data[data[attr] == val]
                data_by_attr_and_concept = data_by_attr[data_by_attr[concept] == c]
                attribute_counts[c] = data_by_attr_and_concept.shape[0]
                total_info = attribute_counts[concept_values[1]] + attribute_counts[concept_values[0]]

                if attribute_counts[concept_values[1]] == 0 or attribute_counts[concept_values[0]] == 0:
                    info_gain = 0
                else:
                    info_gain = information_gain(attribute_counts[concept_values[1]], attribute_counts[concept_values[0]])

                if attr not in entropy_by_attribute:
                    entropy_by_attribute[attr] = (total_info / total_instances) * info_gain
                else:
                    entropy_by_attribute[attr] = entropy_by_attribute[attr] + (total_info / total_instances) * info_gain

    gain_by_attribute = {}
    for gain_attr in entropy_by_attribute:
        gain_by_attribute[gain_attr] = class_entropy - entropy_by_attribute[gain_attr]
    node_to_add = max(gain_by_attribute, key=gain_by_attribute.get)
    tree = insert_node(tree, add_to, node_to_add)

    for next_data in attribute_values[node_to_add]:
        tree = insert_node(tree, node_to_add, next_data)
        new_data = data[data[node_to_add] == next_data].drop(node_to_add, axis=1)
        attribute_list = list(new_data)[:-1]
        tree = get_next_node(new_data, attribute_list, concept, concept_values, tree, next_data)

    return tree

def main():
    import pandas as pd

    data = pd.read_csv('id3.csv')
    attribute_list = list(data)[:-1]
    target_concept = str(list(data)[-1])
    target_concept_values = list(set(data[target_concept]))
    decision_tree = get_next_node(data, attribute_list, target_concept, target_concept_values, {'root': 'None'}, 'root')
    print(decision_tree)
    

main()
