# python3

EPS = 1e-6
PRECISION = 20


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)


def SelectPivotElement(a, used_rows, used_columns):
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    while not a[pivot_element.row][pivot_element.column]:
        pivot_element.column += 1
    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = (
        a[pivot_element.row],
        a[pivot_element.column],
    )
    b[pivot_element.column], b[pivot_element.row] = (
        b[pivot_element.row],
        b[pivot_element.column],
    )
    used_rows[pivot_element.column], used_rows[pivot_element.row] = (
        used_rows[pivot_element.row],
        used_rows[pivot_element.column],
    )
    pivot_element.row = pivot_element.column


def ProcessPivotElement(a, b, pivot_element):
    # Rescale
    scale_factor = a[pivot_element.row][pivot_element.column]
    a[pivot_element.row] = [number / scale_factor for number in a[pivot_element.row]]
    b[pivot_element.row] = b[pivot_element.row] / scale_factor

    # Add/Subtract
    for i in range(len(a)):
        is_subtract = True
        if i == pivot_element.row:
            continue
        if a[i][pivot_element.column] != 0:
            if a[i][pivot_element.column] < 0:
                is_subtract = False
            c = abs(
                a[i][pivot_element.column] / a[pivot_element.row][pivot_element.column]
            )
            for j in range(len(a)):
                if not is_subtract:
                    a[i][j] = a[i][j] + (a[pivot_element.row][j] * c)
                else:
                    a[i][j] = a[i][j] - (a[pivot_element.row][j] * c)
            if not is_subtract:
                b[i] = b[i] + (b[pivot_element.row] * c)
            else:
                b[i] = b[i] - (b[pivot_element.row] * c)


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b


def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print(column[row])


if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
