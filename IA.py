import game
import copy


#A partir du de la bibli "game.py" et de fonction venant de Mr.Lurkin, j'ai des fonctions permettant à mon IA 
# de jouer avec l'interface graphique et effectuer des mouvements légal à mon tour.
directions = [
    ( 0,  1),
    ( 0, -1),
    ( 1,  0),
    (-1,  0),
    ( 1,  1),
    (-1,  1),
    ( 1, -1),
    (-1, -1)
]

def add(p1, p2):
    l1, c1 = p1
    l2, c2 = p2
    return l1 + l2, c1 + c2

def coord(index):
    return index // 8, index % 8

def index(coord):
    l, c = coord
    return l*8+c

def isInside(coord):
    l, c = coord
    return 0 <= l < 8 and 0 <= c < 8

def walk(start, direction):
    current = start
    while isInside(current):
        current = add(current, direction)
        yield current

def isGameOver(state):
    playerIndex = state['current']
    otherIndex = (playerIndex+1)%2

    res = False
    if len(possibleMoves(state)) == 0:
        state['current'] = otherIndex
        if  len(possibleMoves(state)) == 0:
            res = True
    state['current'] = playerIndex
    return res

def willBeTaken(state, move):
    playerIndex = state['current']
    otherIndex = (playerIndex+1)%2

    if not (0 <= move < 64):
        raise game.BadMove('Your must be between 0 inclusive and 64 exclusive')

    if move in state['board'][0] + state['board'][1]:
        raise game.BadMove('This case is not free')

    board = []
    for i in range(2):
        board.append(set((coord(index) for index in state['board'][i])))

    move = coord(move)

    cases = set()
    for direction in directions:
        mayBe = set()
        for case in walk(move, direction):
            if case in board[otherIndex]:
                mayBe.add(case)
            elif case in board[playerIndex]:
                cases |= mayBe
                break
            else:
                break

    if len(cases) == 0:
        raise game.BadMove('Your move must take opponent\'s pieces')
    
    return [index(case) for case in cases]

def possibleMoves(state):
    res = []
    for move in range(64):
        try:
            willBeTaken(state, move)
            res.append(move)
            
        except game.BadMove:
            pass
    return res

def Othello(players):
    # 00 01 02 03 04 05 06 07
    # 08 09 10 11 12 13 14 15
    # 16 17 18 19 20 21 22 23
    # 24 25 26 27 28 29 30 31
    # 32 33 34 35 36 37 38 39
    # 40 41 42 43 44 45 46 47
    # 48 49 50 51 52 53 54 55
    # 56 57 58 59 60 61 62 63

    state = {
        'players': players,
        'current': 0,
        'board': [
            [28, 35],
            [27, 36]
        ]
    }

    def next(state, move):
        newState = copy.deepcopy(state)
        playerIndex = state['current']
        otherIndex = (playerIndex+1)%2

        if len(possibleMoves(state)) > 0 and move is None:
            raise game.BadMove('You cannot pass your turn if there are possible moves')

        if move is not None:
            cases = willBeTaken(state, move)

            newState['board'][playerIndex].append(move)

            for case in cases:
                newState['board'][otherIndex].remove(case)
                newState['board'][playerIndex].append(case)
            
        newState['current'] = otherIndex

        if isGameOver(newState):
            if len(newState['board'][playerIndex]) > len(newState['board'][otherIndex]):
                winner = playerIndex
            elif len(newState['board'][playerIndex]) < len(newState['board'][otherIndex]):
                winner = otherIndex
            else:
                raise game.GameDraw(newState)
            raise game.GameWin(winner, newState)
        
        return newState
    return state, next

Game = Othello




#FCT DE MON IA
def ia1(state): 
    #A mon tour, parmi les mouvements possibles, je choisis les cases à jouer en priorité.
    mvt_possible= possibleMoves(state)
    reponse_ia ={"response": "move","move": [],"message": "Ouss le + beau"}
    
    #SITUATION 1: Tour où j'ai minimum 1 case où je peux jouer
    if len(mvt_possible)!=0:
        #Dans le plateau du jeu, l'IA joue en priorité: 1)Coins, 2)Cases aux murs, 3)Carrée central, 
        #4)Avant dernier carrée sauf ses coins, 5)Coins de l'avant dernier carrée
                                
        coins= [0,7,56,63]
        mur= [8,16,24,32,40,48,57,58,59,60,61,62,55,47,39,31,23,15,6,5,4,3,2,1]
        carre_central= [18,19,20,21,29,37,45,44,43,42,34,26]
        avantdernier_carrée= [10,11,12,13,22,30,38,46,53,52,51,50,41,33,25,17]
        interdit= [9,14,49,54]  
        
        for i in mvt_possible:
            if i in coins:                                                                                                   
                move= i
                reponse_ia["move"]=move
                return reponse_ia

        for i in mvt_possible:
            if i in mur:                                                                                                   
                move= i
                reponse_ia["move"]=move
                return reponse_ia

        for i in mvt_possible:                                
            if i in carre_central: 
                move= i
                reponse_ia["move"]=move
                return reponse_ia
        
        for i in mvt_possible:
            if i in avantdernier_carrée:                                                                                                   
                move= i
                reponse_ia["move"]=move
                return reponse_ia      
        
        for i in mvt_possible:
            if i in interdit:                                                                                                   
                move= i
                reponse_ia["move"]=move
                return reponse_ia                        

    #SITUATION 2: Tour où je n'ai pas de cases où je peux jouer    
    if len(mvt_possible)==0:
        #Je passe mon tour
        reponse_ia["move"]= None
        reponse_ia["message"]= "Passe"
        return reponse_ia