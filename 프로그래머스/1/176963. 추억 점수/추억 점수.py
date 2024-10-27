def solution(name, yearning, photo):
    answer = []
    name_yearning_dict = {name[i]: yearning[i] for i in range(len(name))}
    
    for people_in_photo in photo:
        score = sum(name_yearning_dict.get(person, 0) for person in people_in_photo)
        answer.append(score)
    return answer