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

def binary_search_score_colors(score_color_list, input_score):
    
    left = 0
    right = len(score_color_list) - 1
    nearest = None
    
    while left <= right:
        mid = (left + right) // 2
        if score_color_list[mid].score == input_score:
            return score_color_list[mid].color
        elif score_color_list[mid].score > input_score:
            left = mid + 1
        else:
            right = mid -1
        if nearest is None or abs(score_color_list[mid].score - input_score) < abs(nearest.score - input_score):
            nearest = score_color_list[mid]
    
    return nearest.color
        
        

list = getScoreColors()
print('List Length:' + str(len(list)))

print(binary_search_score_colors(list, int(0)))
print(binary_search_score_colors(list, int(1000)))
