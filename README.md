# Reversi

This app plays [Reversi](https://en.wikipedia.org/wiki/Reversi). The code is all in [Python](https://www.python.org/), 
but then compiled into JavaScript using [Transcrypt](https://transcrypt.org/).

The game is hosted at: https://keithrieck.github.io/transcrypt_reversi/

This app represents a modest combination of [Symbolic Artifical Intelligence](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)
and [Machine Learning](https://en.wikipedia.org/wiki/Machine_learning).

## Basic Game Play Algorithm

Suppose that the app is trying to decide what move to make.  Suppose that the current board has 
four possible places on which to place a black piece.  Each of those moves results in a new board.
The program might evaluate each of those boards in decide which is more advantageous to the black
and then make the corresponding move.  We pick the move which results in the _maximum_ value for 
the black player.

In AI, this is called a "state space search".  We are searching the space of all possible results
to pick the best move.  To determine the value of any of the given board, we create a 
"static evaluation function", which is a programmed function that takes a board as input and outputs 
a number for the relative value of the board.  The black player wants to pick the move resulting in 
the _maximum_ number from the static evaluation function.  The white player wants the move
resulting in the _minimum_ value from the same static evaluation function.

To make our app a better player, we should find better static evaluation functions and we should
also make our state space search more sophisticated.

We can improve the state space search by searching multiple moves into the future.  To search
two moves ahead, we would consider all the possible black moves from the current board and generate the 
resulting boards.  For each of those boards we would consider all possible white moves and generate
those boards.  Then we would apply the static evaluation function to all resulting white boards.  We 
then assign a value to each of the black boards as the _minimum_ value of all the white boards (since
the white player will be trying to minimize the static board value).  Then, the black player picks
the move which results in the _maximum_ static value (since black wants to maximize the board value).  We 
can look forward more than two moves and then apply the static evaluation function to the final boards, 
but we must then alternate minimum/maximum as we back the values up through the graph.  This is known 
as a [Minimax](https://en.wikipedia.org/wiki/Minimax) search algorithm.

The big problem with this kind of state space search is that the time consumed increases exponentially
with the number of moves forward.  To play an entertaining game, it might be reasonable to search
forward four moves, but painful to wait while the program searches forward six moves.  One 
technique for improving game search is to prune away parts of the search tree which cannot find a better
move.  The most common optimization is called 
[Alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) which can, in the best
cases, halve the exponent.

State space search has been well researched (decades ago), and is in fact considered "Old Fashioned AI".
At this point, the greatest opportunity to improve a game playing program is to improve the
static evaluation function.  With Reversi, you can apply lots of clever insights into your function,
considering which parts of the board to attack and which patterns of pieces are most advantageous.
This is also an area where Machine Learning can be brought in, allowing us to _learn_ better
functions by processing large data sets of boards.

## Reversi

This app does minimax search with alpha-beta pruning.  The basic app searches four moves into the future.
It can be easily reconfigured to more or fewer moves forward, but it bogs down and becomes less
entertaining at more than four moves.

### Version 0

The [initial version](https://keithrieck.github.io/transcrypt_reversi/?d=1&f=0) I wrote has a static 
evaluation function that always returns zero for all boards. The result plays completely at random.
This version is kind of fun, since it's easy to beat.

### Version 1

The [first serious verison](https://keithrieck.github.io/transcrypt_reversi/?f=1) I wrote uses a
hand-crafted static evaluation function.  It prioritizes capturing corners and edges, but then
tries to maximize the number of black pieces captured.

### Version 2

The [second version](https://keithrieck.github.io/transcrypt_reversi/?f=2) uses machine learning
to craft a better evaluation function.  I ran the program against itself to randomly generate
boards, throwing out all boards from the beginning and end of the game.  This gave me a data
set of unique boards from the middle of the games.  Then I evaluated each board with a search
depth of six moves and the static evaluation function from version 1.

The result was a data set of 100,000 boards each of which was tagged with the searched values at
zero, two, four, and six moves into the future.  On this data set, I applied the many correlation 
algorithms from [scikit-learn](https://scikit-learn.org/) attempting to find a better static
evaluation function that might return the six-move value based on characteristics of the board.

The best function I have found so far was created by sklearn's 
[DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html). I 
translated the decision tree back into Python for use in the final version of this app.



