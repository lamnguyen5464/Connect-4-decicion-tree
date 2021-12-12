from sklearn import tree
import graphviz

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

dot_data = tree.export_graphviz(clf, out_file=None, 
                     filled=True, rounded=True,  
                      special_characters=True) 

graph = graphviz.Source(dot_data) 
graph.render(filename="test",format='png',directory="img")
