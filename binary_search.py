import requests

class ScoreColor:
    def __init__(self, score, color):        
        self.score = score
        self.color = color

def getScoreColors():
        scoreColors = []
        try:        
            request = requests.get('https://raider.io/api/v1/mythic-plus/score-tiers')
            
            for score in request.json():
                scoreColors.append(ScoreColor(score['score'], score['rgbHex']))
            
        except:
            print('Error: Score colors not found.')
        return scoreColors

def binary_search(list, item):
    
    print('First item score value: ' + str(list[0].score))
    print('Last item score value: ' + str(list[len(list)-1].score))
    if item > int(list[0].score) or item < int(list[len(list)-1].score):
       return None  
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low+high)//2        
        guess = int(list[mid].score)        
        highBound = int(list[mid-1].score)
        lowBound = int(list[mid+1].score)  
        print(guess)     
        if guess == item:           
            return list[mid].color
        elif lowBound < item < highBound:            
            return list[mid].color
        elif guess > item:
            low = mid - 1
        elif guess < item:
            high = mid + 1
        else:
            return None
        
        

list = getScoreColors()
print('List Length:' + str(len(list)))

print(binary_search(list, 2000))
