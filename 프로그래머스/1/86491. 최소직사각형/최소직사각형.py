def solution(sizes):
    rotated_sizes = [(max(width, height), min(width, height)) for width, height in sizes]
    
    max_width = max(width for width, _ in rotated_sizes)
    max_height = max(height for _, height in rotated_sizes)

    answer = max_width * max_height
    return answer
