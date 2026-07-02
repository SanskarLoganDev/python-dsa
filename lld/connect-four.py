# General path for LLD
# Requirements --> Entities --> Class Design --> Implementation --> Extensibility


"""
Build a two-player Connect Four game. Players take turns dropping discs into a 7-column, 6-row board. 
The first to align four of their own discs vertically, horizontally, or diagonally wins.
"""

"""
Step 1: Requirements

Use these points to generate requirements

1. primary capabilities
Ask questions like, how does a user insert the disc? does he choose a column name?
different ways a game can end? are there any draw conditions? (like the baord is completely filled and no one could align 4)

2. error handling
Can someone go out of turn? or what happens when someone inserts in a column already filled? (handle grecefully and reject)

3. scope boundaries
single game at a time? or concurrent games?
Is the UI in scope?

Requirements:
1. Two players take turns dropping discs into a 7-column, 6-row board
2. A disc falls to the lowest available row in the chosen column
3. The game ends when:
   - A player gets four discs in a row (vertical, horizontal, or diagonal). They win.
   - The board is full. It's a draw.
4. Invalid moves should be rejected clearly:
   - Dropping in a full column.
   - Moving out of turn.
   - Moving after the game is over.

Out of scope:
- UI support
- Concurrent games
"""

"""
Step 2: Entities
- Game
- Board
- Players
- Disc
"""

# Step 3: Class Design
# Use SRP: Single Responsibilty Principle

class Game:
   # start with mentioning the states
   player1: Player
   player2: Player
   currentPlayer: Player
   board: Board
   state: GameState # IN_PROGRESS, WON, DRAW. Use Enum for this
   # avoid using bool states like isDraw, isOver, hasWinner as they give a lot of invalid combinations like isDraw and hasWinner both True. Use Enum as above instead.
   
   # now mention public methods
   + Game(player1, player2) # class constructor
   + makeMove(player, column)
   
   # now the private ones, these are less important
   - getCurrentPlayer()
   - getGameState()
   - getWinner() 
    
    
class Board:
   - rows: int # 6
   - columns: int # 7
   - grid: DiscColor?[row][columns]  # use ENUM for color instead of using this -grid: Player?[row][columns]
   
   + canPlace(column) -> bool
   + placeDisc(column, color) -> int # return row the disc lands in or -1
   + isFull() -> bool
   + checkWin(row, column, color) -> bool
   
   - getRow()
   - getCol()
   .... and more
   
enum DiscColor:
   RED
   BLUE
   
   
class Player:
   color: DiscColor
   name: string
   
   + getName() -> string
   + getColor() -> DiscColor
 
 
 
# Step 4: Implementation
# 1. Defining the core logic
# 2. Consider the edge cases

# The interviewer mostly asks to implement the most important functions
# here Game.makeMove, board.placeDisc, baord.checkWin

class Game:
   def makemove(player, column):
      """
      Core logic:
      - placeDisc
      - checkWin
      - if not, check for a draw
      - switch turns
      
      Edge cases:
      - game is already over
      - wrong player turn
      
      # this is actually for board
      - column index it out of bounds
      - column is full
      """
      row = board.placeDisc(column, player.getColor())
      
      if board.checkWin(row, column, player.getColor()):
         state = WON
         winner = player
      elif board
