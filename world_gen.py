import random

def GenerateMap(width, height):
    count = 1500
    drunk = {
        'wallCountdown': count,
        'padding': 0,
        'x': int( width / 2 ),
        'y': int( height / 2 )
    }
    
    def getLevelRow():
        return ['0'] * width
    
    level = [getLevelRow() for _ in range(height)]
    
    while drunk['wallCountdown'] >= 0:
        x = drunk['x']
        y = drunk['y']
        
        if level[y][x] == '0':
            level[y][x] = '1'
            drunk['wallCountdown'] -= 1
        
        roll = random.randint(1, 4)
        
        if roll == 1 and x > drunk['padding']:
            drunk['x'] -= 1
        
        if roll == 2 and x < width - 1 - drunk['padding']:
            drunk['x'] += 1
        
        if roll == 3 and y > drunk['padding']:
            drunk['y'] -= 1
        
        if roll == 4 and y < height - 1 - drunk['padding']:
            drunk['y'] += 1

    for y in range(width):
        for x in range(height):
            if random.randint(1,20) == 1 and level[x][y] == '1':
                level[x][y] = 'E'
    return level

if __name__ == "__main__":
    level = GenerateMap(95,35)
    for row in level:
            print( ''.join(row) )