def hanoi_solver(n):
    # Initialize the three pegs:
    # Peg 0 starts with disks from n down to 1, while Peg 1 and Peg 2 are empty.
    pegs = [list(range(n, 0, -1)), [], []]
    
    states = []
    
    # Helper function to capture and format the current peg configuration
    def record_state():
        states.append(f"{pegs[0]} {pegs[1]} {pegs[2]}")
        
    # Record the initial state
    record_state()
