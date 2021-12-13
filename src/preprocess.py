from os import error
from utils.fileUtils import getAllLineFromDataset, getDatasetDir
from utils.constant import DATASET_BASE
import random

try:
    print('Start spliting dataset')

    all_data = getAllLineFromDataset('/basedata/all-data.dat')
    random.shuffle(all_data)

    for dataset in DATASET_BASE:
        filename_train = dataset["filename_train"]
        filename_test = dataset["filename_test"]
        ratio = dataset["ratio"]

        index = int(ratio[0] / 100 * len(all_data))

        file = open(getDatasetDir() + "/parsingdata/" + filename_train, "w")
        file.write(''.join(all_data[ :index]))
        file.close()


        file = open(getDatasetDir() + "/parsingdata/" + filename_test, "w")
        file.write(''.join(all_data[index: ]))
        file.close()

        print('Created dataset for ' + str(ratio) + ' in folder: ' + getDatasetDir())
except error:
    print("Please run preprocess.sh before hand")
