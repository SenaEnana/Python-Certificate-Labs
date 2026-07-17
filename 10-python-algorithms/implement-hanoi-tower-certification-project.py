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
    
    # Recursive helper to perform the Tower of Hanoi moves
    def solve(disks, src, dst, aux):
        if disks == 1:
            # Move the smallest disk from the source peg to the destination peg
            pegs[dst].append(pegs[src].pop())
            record_state()
            return
        
        # Step 1: Move the top n-1 disks from src to aux using dst
        solve(disks - 1, src, aux, dst)
        
        # Step 2: Move the remaining largest disk from src to dst
        pegs[dst].append(pegs[src].pop())
        record_state()
