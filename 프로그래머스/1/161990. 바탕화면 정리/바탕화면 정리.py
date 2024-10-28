def solution(wallpaper):

    min_row, min_col = float('inf'), float('inf')
    max_row, max_col = -1, -1
    
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == '#':

                min_row = min(min_row, r)
                min_col = min(min_col, c)
                max_row = max(max_row, r)
                max_col = max(max_col, c)
    
    return [min_row, min_col, max_row + 1, max_col + 1]
