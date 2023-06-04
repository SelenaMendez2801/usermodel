from anytree import Node, RenderTree
import numpy as np
# Object "scenario" containing a title, two options and a set of personal values

class Scenario:

    def __init__(self, title, choice1, choice2, values, context, num_questions):
        self.title = title
        self.option1 = choice1
        self.option2 = choice2
        self.values = values
        self.rates_base = []
        self.rates_context = []
        self.context = context
        self.num_questions = num_questions

    def get_title(self):
        return self.title

    def get_option1(self):
        return self.option1

    def get_option2(self):
        return self.option2

    def get_values(self):
        return self.values

    def get_rates(self):
        return self.rates

    def distance(self, x, y):
        if x >= y:
            result = x - y
        else:
            result = y - x
        return result

    def get_rates_str(self, i):
        if self.rates_base.__getitem__(i) == -10:
            return "very low"
        elif self.rates_base.__getitem__(i) == -5:
            return "low"
        elif self.rates_base.__getitem__(i) == 0:
            return "moderate"
        elif self.rates_base.__getitem__(i) == 5:
            return "high"
        elif self.rates_base.__getitem__(i) == 10:
            return "very high"

    def get_rates_str_context(self, i):
        a = self.rates_base.__getitem__(i)
        b = self.rates_context.__getitem__(i)
        if a > b and self.distance(a,b) == 20:
            return "extremely decreased"
        elif a > b and  self.distance(a,b) == 15:
            return "drastically decreased"
        elif a > b and  self.distance(a,b) == 10:
            return "mediumly decreased"
        elif a > b and  self.distance(a,b) == 5:
            return "slightly decreased"
        elif a == b:
            return "did not change"
        elif a < b and  self.distance(a,b) == 5:
            return "slightly increased"
        elif a < b and  self.distance(a,b) == 10:
            return "mediumly increased"
        elif a < b and  self.distance(a,b) == 15:
            return "drastically increased"
        elif a < b and  self.distance(a,b) == 20:
            return "extremely increased"

    def create_summary(self, title, participant):
        f = open("summary_"+ participant +".txt", "a")
        f.write(title)
        f.write("\n")
        for i,value in  enumerate(self.values):
            f.write("\n")
            f.write("The perceived " + value + " of " + self.option1 + " is " +
                  self.get_rates_str(i) +
                  " in general. The value_action relationship " +
                  self.get_rates_str_context(i) +
                  " with the context: " +  self.context)
            f.write("\n")
            f.write("")

        for i,value in  enumerate(self.values):
            f.write("\n")
            f.write("The perceived " + value + " of " + self.option2 + " is " +
                  self.get_rates_str(i + self.num_questions) +
                  " in general. The value_action relationship " +
                  self.get_rates_str_context( i + self.num_questions) +
                  " with the context: " +  self.context)
            f.write("\n")
            f.write("")
        f.write("\n")
        f.close()

    # Visualize a diagram of the scenarios and their relationships
    def visualize_tree_base(self, participant):
        # Create the tree nodes
        root = Node(self.title)
        o1 = Node(self.option1, parent=root)
        o2 = Node(self.option2, parent=root)

        for value in self.values:
            Node(value + " (" + str(self.rates_base[self.values.index(value)]) + ") ", parent=o1)
            Node(value + " (" + str(self.rates_base[self.values.index(value) + self.num_questions]) + ") ", parent=o2)

        f = open("summary_"+ participant +".txt", "a", encoding="utf-8")
        f.write("Base Tree")
        f.write("\n")
        # Print the tree structure
        for pre, _, node in RenderTree(root):
            f.write(f"{pre}{node.name}")
            f.write("\n")
        f.write("\n")
        f.close()

    def visualize_tree_context(self, participant):
        # Create the tree nodes
        root = Node(self.title)
        o1 = Node(self.option1, parent=root)
        o2 = Node(self.option2, parent=root)

        for value in self.values:
            Node(value + " (" + str( self.rates_context[self.values.index(value)]) + ") ", parent=o1)
            Node(value + " (" + str(self.rates_context[self.values.index(value) + self.num_questions]) + ") ", parent=o2)

        f = open("summary_"+ participant +".txt", "a", encoding="utf-8")
        f.write("Context Tree")
        f.write("\n")
        # Print the tree structure
        for pre, _, node in RenderTree(root):
            f.write(f"{pre}{node.name}")
            f.write("\n")
        f.write("\n")
        f.write("\n")
        f.close()


    def create_summary_file(self, title, participant):
        self.create_summary(title, participant)
        self.visualize_tree_base(participant)
        self.visualize_tree_context(participant)





