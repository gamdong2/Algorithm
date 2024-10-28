def solution(park, routes):

    for i, row in enumerate(park):
        if "S" in row:
            x, y = i, row.index("S")
            break
    
    directions = {
        "E": (0, 1),
        "W": (0, -1),
        "S": (1, 0),
        "N": (-1, 0)
    }

    for route in routes:
        dir, dist = route.split()
        dx, dy = directions[dir]
        dist = int(dist)
        
        can_move = True
        for step in range(1, dist + 1):
            nx, ny = x + dx * step, y + dy * step
            if not (0 <= nx < len(park) and 0 <= ny < len(park[0])) or park[nx][ny] == "X":
                can_move = False
                break
        
        if can_move:
            x, y = x + dx * dist, y + dy * dist

    return [x, y]
