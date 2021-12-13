DATASET_LENGTH = 67557

CHAR_TO_NUM = {
	'b': 0,
	'o': 1,
	'x': -1,
}

NUM_TO_CHAR = {
	0: ' ',
	1: 'o',
	-1: 'x',
}

RATIOS = [[40,60], [60,40], [80,20], [90,10]]

DATASET_BASE = [
	{
		"ratio": [40, 60],
		"filename_train": 'feature_label_train_4_6.dat',
		"filename_test": 'feature_label_test_4_6.dat',
		"filename_decision_tree": 'decision_tree_4_6',
		"filename_confusion_matrix": 'confusion_matrix_4_6'
	},
	{
		"ratio": [60,40],
		"filename_train": 'feature_label_train_6_4.dat',
		"filename_test": 'feature_label_test_6_4.dat',
		"filename_decision_tree": 'decision_tree_6_4',
		"filename_confusion_matrix": 'confusion_matrix_6_4'
	},
	{
		"ratio": [80, 20],
		"filename_train": 'feature_label_train_8_2.dat',
		"filename_test": 'feature_label_test_8_2.dat',
		"filename_decision_tree": 'decision_tree_8_2',
		"filename_confusion_matrix": 'confusion_matrix_8_2'
	},
	{
		"ratio": [90,10],
		"filename_train": 'feature_label_train_9_1.dat',
		"filename_test": 'feature_label_test_9_1.dat',
		"filename_decision_tree": 'decision_tree_9_1',
		"filename_confusion_matrix": 'confusion_matrix_9_1'
	},

]

LABEL_NODES = ['A1', ' A2', ' A3', ' A4', ' A5', ' A6', ' A7', ' A8', ' A9', ' A10', ' A11', ' A12', ' A13', ' A14', ' A15', ' A16', ' A17', ' A18', ' A19', ' A20', ' A21', ' A22', ' A23', ' A24', ' A25', ' A26', ' A27', ' A28', ' A29', ' A30', ' A31', ' A32', ' A33', ' A34', ' A35', ' A36', ' A37', ' A38', ' A39', ' A40', ' A41', ' A42']