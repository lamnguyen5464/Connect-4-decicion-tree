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
		"ratio": [40,60],
		"filename_train": 'feature_label_train_4_6.dat',
		"filename_test": 'feature_label_test_4_6.dat'
	},
	{
		"ratio": [60,40],
		"filename_train": 'feature_label_train_6_4.dat',
		"filename_test": 'feature_label_test_6_4.dat'
	},
	{
		"ratio": [80, 20],
		"filename_train": 'feature_label_train_8_2.dat',
		"filename_test": 'feature_label_test_8_2.dat'
	},
	{
		"ratio": [90,10],
		"filename_train": 'feature_label_train_9_1.dat',
		"filename_test": 'feature_label_test_9_1.dat'
	},

]