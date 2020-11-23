
from lib.question import Question
import math


class Node():
    
    __slots__ = [
        'data',
        'children',
        'isLeaf',
        'question',
        'best_gain'
    ]

    def __init__(self, dataset):
        self.data = dataset
        self.children = []
        self.isLeaf = False
        

    def build_tree(self):
        optimal_question = self.__find_optimal_split_question(self.data)
        if not optimal_question:
            self.isLeaf = True
        else:
            true_rows, false_rows = self.__split(optimal_question, self.data)
            self.children = [Node(true_rows), Node(false_rows)]
            for child in self.children:
                child.build_tree()
        
    def display(self, level=0):
        print('\t' * level + str(self))
        if not self.isLeaf:
            for child in self.children:
                child.display(level+1)

    def __str__(self, level=0):
        count_0, count_1, _ = self.__getClassCounts(self.data)
        isLeafString = "LEAF" if self.isLeaf else "NODE"
        color = "\033[42m" if self.isLeaf else ""
        end_color = "\033[0m"
        display_question = self.question if self.question else ""
        best_gain = round(self.best_gain, 2) if self.best_gain else ""

        return f"{color}{isLeafString}{end_color} {count_0}/{count_1} {display_question} {best_gain}"

    def __getClassCounts(self, data):
        total_classes = len(data)
        count_0 = [row[0] for row in data].count(0)
        count_1 = total_classes - count_0
        return count_0, count_1, total_classes


    def __process_classes(self, data_rows) -> list:
        """ calculates the number of different classes in the matrix.

        Returns:
        * total number of items
        * list with counts of every item (class is index)
        * probability of class 0
        * probability of class 1
        """
        count_0, count_1, total_classes = self.__getClassCounts(data_rows)

        proba_0 = count_0 / float(total_classes)
        proba_1 = count_1 / float(total_classes)

        return total_classes, [count_0, count_1], proba_0, proba_1

    def __gini(self, data_rows):
        """ calculates the split impurity for the input matrix
        
        split impurity: degree of 'unmixing' of the (sub-)dataset 
        """
        _, _, proba_0, proba_1 = self.__process_classes(data_rows)
        return 1.0 - (proba_0**2) - (proba_1**2)

    def __entropy(self, data_rows):
        """ calculates the entropy for the input matrix """
        _, _, proba_0, proba_1 = self.__process_classes(data_rows)
        return -1 * (0 if (proba_0 == 0.0 or proba_1 == 0) else (proba_0 * math.log2(proba_0) + proba_1 * math.log2(proba_1)))

    def __info_gain(self, lhs, rhs, entropy, q):
        weight = float(len(lhs)) / (len(lhs) + len(rhs))
        return entropy - weight * self.__entropy(lhs) - (1 - weight) * self.__entropy(rhs)

    def __split(self, q, data_row):
        true_rows, false_rows = [], []
        for row in data_row:
            if q.compare(row):
                true_rows.append(row)
            else:
                false_rows.append(row)
        
        return true_rows, false_rows

    def __find_optimal_split_question(self, data_rows):
        """ checks for all possible splits, evaluates them by their entropy and information gain, then splits """
        best_gain, best_question = 0, None
        entr = self.__entropy(data_rows)
        
        # goes over every feature column (1 to len-1)...
        for feature_index in range(1, len(data_rows[0]) - 1):
            # gets all the unique values for that feature. Set() guarantees uniqueness
            potential_values = set([row[feature_index] for row in data_rows])

            # create a question from each one of these unique values for a feature
            for value in potential_values:
                q = Question(feature_index, value)

                # split the dataset at this question, in order to test the performance
                true_rows, false_rows = self.__split(q, self.data)

                # if no split has been made - skip this value
                if true_rows == data_rows or false_rows == data_rows: continue

                # evaluate this split
                gain = self.__info_gain(true_rows, false_rows, entr, q)

                # update the best results
                if gain > best_gain:
                    best_gain = gain
                    best_question = q

        self.best_gain = best_gain
        self.question = best_question
        
        return best_question


