from collections import deque

def solution(maps):
    def bfs(x, y):
        queue = deque([(x, y)])
        total_food = 0
        while queue:
            cx, cy = queue.popleft()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            total_food += int(maps[cx][cy])
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maps[nx][ny] != 'X':
                    queue.append((nx, ny))
        return total_food

    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    results = []

    for i in range(rows):
        for j in range(cols):
            if maps[i][j] != 'X' and not visited[i][j]:
                results.append(bfs(i, j))
    
    return sorted(results) if results else [-1]
