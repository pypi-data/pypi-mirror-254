## suko

Suko (a modified Sudoku game) is a popular logic-based number-placement puzzle where the objective is to fill a 3x3 grid with digits that compose the grid (often called regions or boxes) contain all of the digits from 1 to 9 without repetition.

Base position:

 | 1 | 2 | 3 |
 |:-:|:-:|:-:|
 | 4 | 5 | 6 |
 | 7 | 8 | 9 |

Present as array: [1, 2, 3, 4, 5, 6, 7, 8, 9]

This generator is able to generate a random pattern (digits) with sums and color hints.

### install via pip:
```
pip install suko
```
### check user manual:
```
suko -h
```
### execute generator:
```
suko g
```

#### output example

Random Pattern (Answer): [8, 2, 3, 6, 7, 9, 5, 1, 4]

Sums: [23, 21, 19, 21]

Color Range (Green, Orange, Yellow): (2, 4, 3)

Color Pattern: [2, 7, 5, 9, 1, 3, 4, 8, 6]

Green : 7

Orange: 22

Yellow: 16

#### how to read the output above

Random pattern as possible answer (or seed):

 | 8 | 2 | 3 |
 |:-:|:-:|:-:|
 | 6 | 7 | 9 |
 | 5 | 1 | 4 |

Color pattern filled as:

 | O | G | O |
 |:-:|:-:|:-:|
 | Y | O | Y |
 | G | Y | O |


#### full review mode:
```
suko f
```

#### play mode (hidden seed):
```
suko p
```
