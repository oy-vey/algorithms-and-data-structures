# python3
from sys import stdin
import copy

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
        if pivot_element.column == len(a):
            return None
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
        if pivot_element is None:
            return None
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b

def getSubsets(x):
  if x == 0:
    return [[]]
  else:
    old_sets = getSubsets(x-1)
    new_sets = copy.deepcopy(old_sets)
    for s in new_sets:
        s.append(x-1)
    old_sets.extend(new_sets)
    return old_sets


def getEquation(A, b, set=None):
    if set is None:
        return Equation(A, b)
    A_filtered = []
    b_filtered = []
    for i, row in enumerate(A):
        if i in set:
            row_copy = copy.deepcopy(row)
            A_filtered.append(row_copy)
            b_filtered.append(b[i])
    return Equation(A_filtered, b_filtered)


def identity(n):
    mat = [[0 for x in range(n)] for y in range(n)]
    for i in range(0, n):
        mat[i][i] = -1
    return mat

def multiplyTwoLists(list_a, list_b):
    return sum([a * b for a, b in zip(list_a,list_b)])


def checkSolution(A, b, solution):
    for i, row in enumerate(A):
        v_i = multiplyTwoLists(row, solution)
        if round(v_i, 3) > b[i]:
            return False
    return True


def solve_diet_problem(n, m, A, b, c):
  # Adding n + 1 inequality
  n += 1
  A.append([1] * m)
  b.append(10 ** 9)

  # Adding m new constraints
  A_additional = identity(m)
  b_additional = [0] * m
  A.extend(A_additional)
  b.extend(b_additional)

  # Finding all the subsets of n + m inequalities having the size of m
  all_subsets = getSubsets(n + m)
  needed_subsets = [s for s in all_subsets if len(s) == m]

  # # Finding a solution for one of the sets
  # equation = getEquation(A, b, needed_subsets[0])
  # solution = SolveEquation(equation)
  # if checkSolution(A, b, solution):
  best_value = None
  best_set = None
  ansx = None



  # Finding the best solution across all subsets of size m
  for ns in needed_subsets:
      equation = getEquation(A, b, ns)
      solution = SolveEquation(equation)
      if solution is None:
          continue
      if checkSolution(A, b, solution):
          res = multiplyTwoLists(solution, c)
          if best_value is None or res > best_value or (res == best_value and n - 1 not in ns):
              best_value = res
              best_set = ns
              ansx = solution


  #anst = best_value
  # ansx = solution

  if best_value is None:
      anst = -1
  # Check if it's infinity
  elif n - 1 in best_set:
      anst = 1
  else:
      anst = 0


  return [anst, ansx]

n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
  A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

anst, ansx = solve_diet_problem(n, m, A, b, c)

if anst == -1:
  print("No solution")
if anst == 0:
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")

