# Connect-4 Decision tree

## Preprocess

### Dataset-preparing

The base dataset contains 67557 lines in the format below:

```
x,b,b,b,b,b,o,o,x,o,x,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,o,b,b,b,b,b,x,b,b,b,b,b,loss
x,x,o,b,b,b,o,o,x,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,x,o,b,b,b,b,loss
x,x,b,b,b,b,o,o,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,o,x,x,o,b,b,loss
x,o,b,b,b,b,o,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,o,x,o,x,x,b,draw
x,o,o,o,x,b,o,b,b,b,b,b,x,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,x,b,b,b,b,b,draw
...
```

Run the command below:

```bash
bash ./preprocess.sh
```

to pre-process dataset (split into train/test sets of proportions: 40/60, 60/40, 80/20, 90/10), so we will gain in folder:

```
dataset
├── basedata
│   └── all-data.dat
└── parsingdata
    ├── feature_label_test_4_6.dat
    ├── feature_label_test_6_4.dat
    ├── feature_label_test_8_2.dat
    ├── feature_label_test_9_1.dat
    ├── feature_label_train_4_6.dat
    ├── feature_label_train_6_4.dat
    ├── feature_label_train_8_2.dat
    └── feature_label_train_9_1.dat
```

### Data-parsing

42 first attributes of each line in dataset will be transform to 1 direction matrix with the mapping format below:

```python
CHAR_TO_NUM = {
	'b': 0,
	'o': 1,
	'x': -1,
}
```

For transforming from:

```
b,b,b,b,b,b,b,b,b,b,b,b,o,b,b,b,b,b,x,o,x,o,x,b,x,o,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,draw
```

to:

```
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 1, -1, 1, -1, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

with label `draw`

Moreover, I also write method to show debugging game's state to console

```python
input = 'b,b,b,b,b,b,b,b,b,b,b,b,o,b,b,b,b,b,x,o,x,o,x,b,x,o,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,draw'
game_state = FourConnectState(str=input)
game_state.show()

# output:
# [' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', 'x', ' ', ' ', ' ']
# [' ', ' ', ' ', 'o', ' ', ' ', ' ']
# [' ', ' ', ' ', 'x', ' ', ' ', ' ']
# [' ', ' ', ' ', 'o', 'o', ' ', ' ']
# [' ', ' ', 'o', 'x', 'x', ' ', ' ']
# draw
```

---

## Decision tree classifiers

The source code is constructed below:

```
./src
├── main.py
├── preprocess.py
├── models
│   ├── CellState.py
│   ├── FourConnectResult.py
│   └── FourConnectState.py
└── utils
    ├── constant.py
    ├── fileUtils.py
    └── plotUtils.py
```

Run

```
bash ./start.sh
```

To execute all required tasks, or run script below in `main.py`:

```python
for dataset in DATASET_BASE:
	process(dataset=dataset, plot_confusion_matrix=True, plot_decision_tree=True)
```

- 40/60 set:

Decision tree of 40/60 set:
max_depth=36 (auto)
(click to image for more detail)
<img src="https://user-images.githubusercontent.com/45004786/145932067-fc4f618a-267d-49db-bc76-bd402b94ad1a.png" width="1000%"/>
Confusion matrix:

<img src="https://user-images.githubusercontent.com/45004786/145932664-8e97a1dd-8094-4877-93e0-9291f6db0e07.png" width="50%"/><br/>
Accuracy: 0.7426668311335882

---

- 60/40 set:

Decision tree of 60/40 set, max_depth=33 (auto) (click to image for more detail)
<img src="https://user-images.githubusercontent.com/45004786/145932986-aa5d9674-c1e8-4953-bda3-c8db4c0300bb.png" width="100%"/>
Confusion matrix:

<img src="https://user-images.githubusercontent.com/45004786/145933238-ec1b3c33-d001-43c2-8720-0b34381cbf49.png" width="50%"/><br/>
Accuracy: 0.7557266032638863

---

- 80/20 set:

Decision tree of 80/20 set,
max_depth=35 (auto)
(click to image for more detail)
<img src="https://user-images.githubusercontent.com/45004786/145933144-d6cbcc8b-0e2d-425f-a6e8-3117e734aacf.png" width="100%"/>
Confusion matrix:

<img src="https://user-images.githubusercontent.com/45004786/145933235-a252a695-20ef-4f06-9e37-2a3396044fd7.png" width="50%"/><br/>

Accuracy: 0.7674659561870929

---

- 90/10 set:

Decision tree of 90/10 set,
max_depth=38 (auto)
(click to image for more detail)
<img src="https://user-images.githubusercontent.com/45004786/145933123-6db4dfc9-06c5-4418-99a3-c61464c9f3d7.png" width="100%"/>
Confusion matrix:

<img src="https://user-images.githubusercontent.com/45004786/145933230-1aecb342-3953-4e0b-ac80-5e107f180b07.png" width="50%"/><br/>

Accuracy: 0.7686500888099467

---

## Decision tree with max_depth

Process on 80/20 set:

max_depth=None (auto set to 34) (click to image for more detail)
<img src="https://user-images.githubusercontent.com/45004786/145931346-fb32155c-592b-4810-bc63-b3e3581a926e.png" width="100%"/>

max_depth=2 (click to image for more detail)
<img src="https://user-images.githubusercontent.com/45004786/145931346-fb32155c-592b-4810-bc63-b3e3581a926e.png" width="100%"/>

max_depth=3 (click to image for more detail)
<img src="https://user-images.githubusercontent.com/45004786/145931552-338ffb4d-c844-400a-a8be-bd12621070f8.png" width="100%"/>

max_depth=4 (click to image for more detail)
<img src="https://user-images.githubusercontent.com/45004786/145931830-cefa0fae-40ff-4ee6-8d41-d3f0055fd5a8.png" width="100%"/>

max_depth=5 (click to image for more detail)
<img src="https://user-images.githubusercontent.com/45004786/145931629-49a9f4d9-61ce-423c-9b0a-6c1834df14c8.png" width="100%"/>

max_depth=6 (click to image for more detail)
<img src="https://user-images.githubusercontent.com/45004786/145931636-226474f2-2c85-4d91-a051-43da60ecbaac.png" width="100%"/>

max_depth=7 (click to image for more detail)
<img src="https://user-images.githubusercontent.com/45004786/145931637-88b5be68-3f35-41f3-bdfb-9c4a3813a306.png" width="100%"/>

### Accuracy table

| max_depth | None  | 2     | 3     | 4     | 5     | 6     | 7     |
| --------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| accuracy  | 0.769 | 0.673 | 0.680 | 0.688 | 0.706 | 0.718 | 0.721 |

---

## Self grading

| No    | Specifications                             | Scores (%) | Complete (%) |
| ----- | ------------------------------------------ | ---------- | ------------ |
| 1     | Preparing the datasets                     | 20         | 20           |
| 2     | Building the decision tree classifiers     | 20         | 20           |
| 3     | Evaluating the decision tree classifiers   |            |              |
|       | Classification report and confusion matrix | 20         | 20           |
|       | Comments                                   | 10         | 10           |
| 4     | The depth and accuracy of a decision tree  |            |              |
|       | Trees, tables, and charts                  | 20         | 20           |
|       | Comments                                   | 10         | 10           |
| Total |                                            | 100        | 100          |
