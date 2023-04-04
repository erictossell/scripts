import requests

class ScoreColor:
    def __init__(self, score, color):        
        self.score = score
        self.color = color
    def __lt__(self, other):
        return self.score < other.score

def getScoreColors():
        scoreColors = []
        try:        
            request = requests.get('https://raider.io/api/v1/mythic-plus/score-tiers')
            
            for score in request.json():
                scoreColors.append(ScoreColor(score['score'], score['rgbHex']))
            
        except:
            print('Error: Score colors not found.')
        return scoreColors

import bisect

def binary_search_score_colors(score_color_list, item):
    if not isinstance(item, int):
        raise TypeError("item must be an integer")
    for i in range(len(score_color_list) - 1):
        if score_color_list[i].score < score_color_list[i + 1].score:
            raise ValueError("score_color_list must be sorted in descending order by score")
    index = bisect.bisect_left(score_color_list, ScoreColor(item, None))
    if index == len(score_color_list):
        return score_color_list[-1].color
    if score_color_list[index].score == item:
        return score_color_list[index].color
    low_bound = score_color_list[index].score
    high_bound = score_color_list[index - 1].score
    if low_bound <= item <= high_bound:
        return score_color_list[index].color
    return score_color_list[-1].color
        
        

list = getScoreColors()
print('List Length:' + str(len(list)))

print(binary_search_score_colors(list, int(207.5)))
