from sklearn import tree, metrics
import numpy
import matplotlib.pyplot as plt
import graphviz
from models.FourConnectState import FourConnectState
from utils.fileUtils  import getAllLineFromDataset

print('start...')

all_data = getAllLineFromDataset()

training_set = all_data[ : 800]
testing_set = all_data[-200: -1]

print("Read file done")

training_set_states = list(map(lambda str: FourConnectState(str=str), training_set))
testing_set_states = list(map(lambda str: FourConnectState(str=str), testing_set))
# for s in states:
# 	s.show()


X = list(map(lambda state: state.state, training_set_states))
Y = list(map(lambda state: state.result, training_set_states))

max_depth = 10
decision_tree = tree.DecisionTreeClassifier(max_depth=max_depth).fit(X, Y)
print('max_depth', decision_tree.tree_.max_depth)

res_pred = decision_tree.predict(
	list(map(lambda state: state.state, testing_set_states))	
)
res_truth = (list(map(lambda state: state.result, testing_set_states)))

cnt = 0
for i in range(0, len(res_pred)):
	if res_pred[i] == res_truth[i]:
		cnt = cnt + 1
	
print('accuracy', cnt / len(res_pred))

confusion_matric = metrics.confusion_matrix(res_truth, res_pred, labels=['win', 'loss', 'draw'])
print(confusion_matric)






labels = ['A1', ' A2', ' A3', ' A4', ' A5', ' A6', ' A7', ' A8', ' A9', ' A10', ' A11', ' A12', ' A13', ' A14', ' A15', ' A16', ' A17', ' A18', ' A19', ' A20', ' A21', ' A22', ' A23', ' A24', ' A25', ' A26', ' A27', ' A28', ' A29', ' A30', ' A31', ' A32', ' A33', ' A34', ' A35', ' A36', ' A37', ' A38', ' A39', ' A40', ' A41', ' A42']


dot_data = tree.export_graphviz(
    filled=True,
	rounded=True,
	max_depth=max_depth,
	feature_names=labels,
	decision_tree=decision_tree
) 

graph = graphviz.Source(dot_data) 
graph.render(filename="test",format='png',directory="img")
