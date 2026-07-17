def hanoi_solver(n):
    pegs = [list(range(n, 0, -1)), [], []]
    
    states = []
    def record_state():
        states.append(f"{pegs[0]} {pegs[1]} {pegs[2]}")
    record_state()
    def solve(disks, src, dst, aux):
        if disks == 1:
            pegs[dst].append(pegs[src].pop())
            record_state()
            return
        solve(disks - 1, src, aux, dst)

        pegs[dst].append(pegs[src].pop())
        record_state()
        
        solve(disks - 1, aux, dst, src)

    solve(n, 0, 2, 1)

    return "\n".join(states)