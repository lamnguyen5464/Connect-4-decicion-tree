from sklearn import tree
import numpy
import matplotlib.pyplot as plt
import graphviz

# X = [[0, 0], [1, 1]]
# Y = [0, 1]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, Y)



data = [['Asset Flip', 100, 1000],
['Text Based', 500, 3000],
['Visual Novel', 1500, 5000],
['2D Pixel Art', 3500, 8000],
['2D Vector Art', 5000, 6500],
['Strategy', 6000, 7000],
['First Person Shooter', 8000, 15000],
['Simulator', 9500, 20000],
['Racing', 12000, 21000],
['RPG', 14000, 25000],
['Sandbox', 15500, 27000],
['Open-World', 16500, 30000],
['MMOFPS', 25000, 52000],
['MMORPG', 30000, 80000]
]
dataset = numpy.array(data)

X = (dataset[:, 1:2])
Y = (dataset[:, 2])

decision_tree = tree.DecisionTreeClassifier().fit(X, Y)

print(decision_tree.predict([[50]]))


dot_data = tree.export_graphviz(
	decision_tree=decision_tree,
    filled=True,
	rounded=True,
    special_characters=True,
	feature_names =['Production Cost']
) 

graph = graphviz.Source(dot_data) 
graph.render(filename="test",format='png',directory="img")
