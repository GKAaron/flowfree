# flowfree
a simple game in Android and iOS. The aim is to fill in colors on all empty grid cells to form "pipes" such that the colors are able to flow between two given sources. \
The pipes cannot intersect with each other, and a complete solution cannot contain any empty grid cell. \
The other constraint for this assignment is that no zigzag pattern is allowed. This means that for each non-source cell, its four-connected neighborhood should have exactly two cells filled with the same color. For each source cell, its neighborhood should have exactly one cell filled with the same color. \
The dumb search will randomly choose a variable and a value to assign, The smart one will use back tracking search with some strategies such as selecting variables and values in 
particular order and with forward checking. The smarter one will implement an arc consistency strategy to check the tailure much faster tahn smart one.
