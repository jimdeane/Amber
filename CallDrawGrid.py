


import drawgrid as dg
board = dg.Board(size=10)
board.fill_square(0,0)
board.fill_square(0,1)
board.fill_square(1,0)
board.fill_square(1,1)
board.fill_square(2,1)
board.fill_square(2,3)

board.showBoard( )
board.animate_board(frames=50, interval=20)  # Adjust frames and interval as needed