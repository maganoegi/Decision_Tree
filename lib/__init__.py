
import math
from lib.Question import Question

def process_classes(data_rows) -> list:
    """ calculates the number of different classes in the matrix.

    Returns:
    * total number of items
    * list with counts of every item (class is index)
    * probability of class 0
    * probability of class 1
    """
    total_classes = len(data_rows)
    count_0 = [row[0] for row in data_rows].count(0)
    count_1 = total_classes - count_0

    proba_0 = count_0 / float(total_classes)
    proba_1 = count_1 / float(total_classes)

    return total_classes, [count_0, count_1], proba_0, proba_1

def gini(data_rows):
    """ calculates the gini impurity for the input matrix
    
    Gini impurity: degree of 'unmixing' of the (sub-)dataset 
    """
    _, _, proba_0, proba_1 = process_classes(data_rows)
    return 1.0 - (proba_0**2) - (proba_1**2)

def entropy(data_rows):
    """ calculates the entropy for the input matrix """
    _, _, proba_0, proba_1 = process_classes(data_rows)
    return -1 * (proba_0 * math.log2(proba_0) + proba_1 * math.log2(proba_1))

def info_gain(lhs, rhs, entropy):
    #TODO: additional research on this one from the class
    weight = float(len(lhs)) / (len(lhs) + len(rhs))
    return entropy - weight * gini(lhs) - (1 - weight) * gini(rhs)

def split(data_rows, question):
    true_rows, false_rows = [], []
    for row in data_rows:
        if question.compare(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    
    return true_rows, false_rows

def make_optimal_split(data_rows):
    """ checks for all possible splits, evaluates them by their entropy and information gain, then splits """
    # TODO: check for relationships in entropy, information gain and gini impurity
    best_gain, best_question = 0, None
    entr = entropy(data_rows)
    
    # goes over every feature column (1 to len-1)...
    for feature_index in range(len(1, data_rows - 1)):
        # gets all the unique values for that feature. Set() guarantees uniqueness
        potential_values = set([row[feature_index] for row in data_rows])

        # create a question from each one of these unique values for a feature
        for value in potential_values:
            question = Question(feature_index, value)

            # split the dataset at this question, in order to test the performance
            true_rows, false_rows = split(data_rows, question)

            # if no split has been made - skip this value
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # evaluate this split
            gain = info_gain(true_rows, false_rows, entr)

            # update the best results
            if gain > best_gain:
                best_gain = gain
                best_question = question
        
    return best_question








if __name__ == "__main__":
    pass