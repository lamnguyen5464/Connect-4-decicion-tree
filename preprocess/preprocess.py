
def show_row(input=''):
    input = 'b,b,b,b,b,b,b,b,b,b,b,b,o,b,b,b,b,b,x,o,x,o,x,b,x,o,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,draw'

    cells = input.split(',')

    result = []

    for i in range(0, 6):
        row = []
        for j in range(0, 7):
            index = 6*(j+1) - i - 1
            tick = not(cells[index] == 'b') and cells[index] or '_'
            row.append(tick)
        print(row)

    print(cells[len(cells)-1])


show_row()
