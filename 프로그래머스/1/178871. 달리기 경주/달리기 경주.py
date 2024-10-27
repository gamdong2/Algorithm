def solution(players, callings):
    player_dict = {player: i for i, player in enumerate(players)}
    
    for called_player in callings:
        current_rank = player_dict[called_player]
        
        if current_rank > 0:
            front_player = players[current_rank - 1]
            players[current_rank], players[current_rank - 1] = players[current_rank - 1], players[current_rank]
            
            player_dict[called_player] = current_rank - 1
            player_dict[front_player] = current_rank

    return players

