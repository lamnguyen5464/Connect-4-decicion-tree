from sklearn import tree, metrics
import matplotlib.pyplot as plt
import graphviz
from models.FourConnectState import FourConnectState
from utils.fileUtils import getAllLineFromDataset
from utils.constant import DATASET_BASE, LABEL_NODES

def process(
	dataset=DATASET_BASE[2],
	max_depth=None, 
	plot_decision_tree=False,
	plot_confusion_matrix=False):

	print('Running on ' +  str(dataset['ratio']) + ' dataset...',)
	print('With max_depth = ' + str(max_depth))

	try:
		training_set = getAllLineFromDataset('/parsingdata/' + dataset["filename_train"])
		testing_set = getAllLineFromDataset('/parsingdata/' + dataset["filename_test"])
	except:
		print('Please run preprocess.sh to prepare dataset')
		return


	print("Start training phase...")

	training_set_states = list(map(lambda str: FourConnectState(str=str), training_set))

	X_train = list(map(lambda state: state.state, training_set_states))
	Y_train = list(map(lambda state: state.result, training_set_states))

	decision_tree = tree.DecisionTreeClassifier(max_depth=max_depth).fit(X_train, Y_train)
	print('max_depth', decision_tree.tree_.max_depth)


	print("Start testing phase...")

	testing_set_states = list(map(lambda str: FourConnectState(str=str), testing_set))
	X_test = list(map(lambda state: state.state, testing_set_states))
	Y_test = list(map(lambda state: state.result, testing_set_states))

	Y_test_pred = decision_tree.predict(X_test)

	accuracy_score = metrics.accuracy_score(Y_test, Y_test_pred)

	print('Accuracy: ', accuracy_score)


	if plot_confusion_matrix:
		print('Start plotting confusion matrix phase...')
		view =  metrics.ConfusionMatrixDisplay.from_predictions(Y_test, Y_test_pred, labels=decision_tree.classes_)
		plt.savefig('output/' + dataset["filename_confusion_matrix"] + '.png')




	if plot_decision_tree:
		print('Start plotting tree phase...')
		dot_data = tree.export_graphviz(
			filled=True,
			rounded=True,
			max_depth=max_depth,
			feature_names=LABEL_NODES,
			decision_tree=decision_tree
		) 

		graph = graphviz.Source(dot_data) 
		graph.render(filename=dataset["filename_decision_tree"] + "_with_maxdepth_" + str(max_depth),format='png',directory="output")

	return (accuracy_score)


for dataset in DATASET_BASE:
	process(dataset=dataset, plot_confusion_matrix=True, plot_decision_tree=True)
	print('\n')


accuracy_list = []
for i in range(1, 8):
	(accuracy_score) = process(max_depth=i == 1 and None or i, plot_decision_tree=True)
	accuracy_list.append(accuracy_score)
	print('\n')

