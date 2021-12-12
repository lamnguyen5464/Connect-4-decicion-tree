from sklearn import tree
import numpy
import matplotlib.pyplot as plt
import graphviz
from models.FourConnectState import FourConnectState
from utils.fileUtils  import getDatasetFile, getAllLineFromDataset

print('start...')

all_data = getAllLineFromDataset()

training_set = all_data[ : 30]
testing_set = all_data[-10: -1]

print("Read file done")

training_set_states = list(map(lambda str: FourConnectState(str=str), training_set))
testing_set_states = list(map(lambda str: FourConnectState(str=str), testing_set))
# for s in states:
# 	s.show()


X = list(map(lambda state: state.state, training_set_states))
Y = list(map(lambda state: state.result, training_set_states))

decision_tree = tree.DecisionTreeClassifier().fit(X, Y)

res = decision_tree.predict(
	list(map(lambda state: state.state, testing_set_states))	
)

ans = (list(map(lambda state: state.result, testing_set_states)))

cnt = 0
for i in range(0, len(res)):
	if res[i] == ans[i]:
		cnt = cnt + 1
	
print(cnt / len(res))

labels = ['A1', ' A2', ' A3', ' A4', ' A5', ' A6', ' A7', ' A8', ' A9', ' A10', ' A11', ' A12', ' A13', ' A14', ' A15', ' A16', ' A17', ' A18', ' A19', ' A20', ' A21', ' A22', ' A23', ' A24', ' A25', ' A26', ' A27', ' A28', ' A29', ' A30', ' A31', ' A32', ' A33', ' A34', ' A35', ' A36', ' A37', ' A38', ' A39', ' A40', ' A41', ' A42']


dot_data = tree.export_graphviz(
	decision_tree=decision_tree,
    filled=True,
	rounded=True,
    special_characters=True,
	feature_names=labels
) 

graph = graphviz.Source(dot_data) 
graph.render(filename="test1",format='png',directory="img")
