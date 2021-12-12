from models.FourConnectResult import FourConnectResult
from models.CellState import CellState
from utils.constant import CHAR_TO_NUM, NUM_TO_CHAR


class FourConnectState:

  def __init__(self, str = ''):
    cells = str.split(',')
    parsedCells = list(map(lambda cell: CHAR_TO_NUM.get(cell), cells))
    self.state = parsedCells[ : -1]
    self.result = cells[len(cells) - 1]

  def show(self):
    for i in range(0, 6):
        row = []
        for j in range(0, 7):
            index = 6*(j+1) - i - 1
            row.append(NUM_TO_CHAR[self.state[index]])
        print(row)

    print(self.result)

## test

# input = 'b,b,b,b,b,b,b,b,b,b,b,b,o,b,b,b,b,b,x,o,x,o,x,b,x,o,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,draw'
# a = FourConnectState(str=input)
# a.show()