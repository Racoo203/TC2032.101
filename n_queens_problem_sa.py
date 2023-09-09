#------------------------------------------------------------------------------------------------------------------
#   Simulated annealing solver for the n-queen problem
#   Modified by Dr. Santiago Enrique Conant Pablos, May 3, 2023
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------
import time
import random
import math

#------------------------------------------------------------------------------------------------------------------
#   Class definitions
#------------------------------------------------------------------------------------------------------------------

class Board(object):
    """ 
        Class that represents n-queens placed on a chess board. Each queen is located in a 
        different column. The board is represented by a list of n rows.
    """
    
    def __init__(self, n, randomize = True):        
        """ 
            This constructor initializes the board with n queens. 

            n: The number of rows and columns of the chess.
            randomize: True indicates that the initial queen positions are choosen randomly.
                       False indicates that the queens are placed on the first row.
        """
        self.n = n
        self.queens = []
        # Place the queens on the first row
        for col in range(n):
            if randomize:
                row = random.choice(range(n))
            else:
                row = 0
            self.queens.append(row)

    def show(self):        
        """ This method prints the current board. """               
        for row in range(self.n):
            for col in range(self.n):
                if self.queens[col] == row:
                    print (' Q ', end = '')
                else:
                    print (' - ', end = '')
            print('')
        print('')
    
    def cost(self):
        """ This method calculates the cost of this solution (the number of queens that are not safe). """
        c = 0
        for queen in range(self.n-1):
            for other_queen in range(queen+1,self.n):
                if (self.queens[queen] == self.queens[other_queen]):
                    # The queens are on the same row
                    c += 1
                elif (other_queen - queen) == abs(self.queens[queen] - self.queens[other_queen]):
                    # The queens are on the same diagonal
                    c += 1
        return c

    def neighbor(self):
        """ This method returns a board instance like this one but with one random move made. """        
        
        # Copy current board
        new_board = Board(self.n, False)
        new_board.queens = self.queens.copy()
             
        # Select one queen randomly
        queen = random.choice(range(self.n))
        
        # Select a new row randomly
        rows = list(range(self.n))
        rows.remove(self.queens[queen])
        new_row = random.choice(rows)
        
        # Update new_board
        new_board.queens[queen] = new_row

        return new_board
    
                                       
#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------
random.seed(time.time()*1000)

board = Board(30, False)      # Initialize board
board.show()    

cost = board.cost()         # Initial cost  
print("Initial Cost: ", cost)
  
step = 0                    # Step count

alpha = 0.9995              # Coefficient of the exponential temperature schedule        
t0 = 1                      # Initial temperature
t = t0    

while t > 0.005 and cost > 0:

    # Calculate temperature
    t = t0 * math.pow(alpha, step)
    step += 1
        
    # Get random neighbor
    neighbor = board.neighbor()
    new_cost = neighbor.cost()

    # Test neighbor
    if new_cost < cost:
        board = neighbor
        cost = new_cost
    else:
        # Calculate probability of accepting the neighbor
        p = math.exp(-(new_cost - cost)/t)
        if p >= random.random():
            board = neighbor
            cost = new_cost

    print("Iteration: ", step, "    Cost: ", cost, "    Temperature: ", t)

print("\n--------Solution-----------")
board.show()         

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------