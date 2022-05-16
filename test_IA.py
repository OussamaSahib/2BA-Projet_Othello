import pytest
import IA

def test_ia1():
    #CURRENT: 0= NOIR DE JOUER ET 1=BLANC DE JOUER
    assert IA.ia1({"players": ["LUR", "Ouss"],"current": 0,"board": [[28,35],[27,36]]}) == {'message': 'Ouss le + beau', 'move': 19, 'response':'move'} or {'message': 'Ouss le + beau', 'move': 26, 'response':'move'} or {'message': 'Ouss le + beau', 'move': 37, 'response':'move'} or {'message': 'Ouss le + beau', 'move': 44, 'response':'move'}
    assert IA.ia1({"players": ["LUR", "Ouss"],"current": 0,"board": [[35],[34]]}) == {'message': 'Ouss le + beau', 'move': 33, 'response':'move'} 
    assert IA.ia1({"players": ["LUR", "Ouss"],"current": 0,"board": [[62],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63]]}) == {'message': 'Ouss le + beau', 'move': 46, 'response':'move'} 
    assert IA.ia1({"players": ["LUR", "Ouss"],"current": 0,"board": [[36],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62]]}) == {'message': 'Ouss le + beau', 'move': 63, 'response':'move'} 
    assert IA.ia1({"players": ["LUR", "Ouss"],"current": 0,"board": [[34],[33]]}) == {'message': 'Ouss le + beau', 'move': 32, 'response':'move'}
    assert IA.ia1({"players": ["LUR", "Ouss"],"current": 0,"board": [[27],[0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]]}) == {'message': 'Ouss le + beau', 'move': 9, 'response':'move'} 
    assert IA.ia1({"players": ["LUR", "Ouss"],"current": 0,"board": [[62],[0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62]]}) == {'message': 'Passe', 'move': None, 'response':'move'} 


def test_add():
    assert IA.add((2,2),(3,3))==(5,5)
    assert IA.add((1,2),(2,4))==(3,6)
    assert IA.add((2,4),(1,1))==(3,5)

def test_coord():
    assert IA.coord(8) == (1,0) 
    assert IA.coord(10) == (1,2)
    assert IA.coord(18) == (2,2)
    
def test_index():
    assert IA.index((1,2)) == 10
    assert IA.index((3,4)) == 28
    assert IA.index((6,8)) == 56

def test_isInside():
    assert IA.isInside((1,2)) == 1 and 2

def test_isGameOver():
    #CURRENT: 0= NOIR DE JOUER ET 1=BLANC DE JOUER
    assert IA.isGameOver({"players": ["LUR", "Ouss"],"current": 0,"board": [[36],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62]]}) == False
    assert IA.isGameOver({"players": ["LUR", "Ouss"],"current": 0,"board": [[36],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]]}) == True

def test_possibleMove():
    #CURRENT: 0= NOIR DE JOUER ET 1=BLANC DE JOUER
    assert IA.possibleMoves({"players": ["LUR", "Ouss"],"current": 0,"board": [[28,35],[27,36]]}) == [19,26,37,44]
    assert IA.possibleMoves({"players": ["LUR", "Ouss"],"current": 0,"board": [[59],[57,58]]}) == [56]
    assert IA.possibleMoves({"players": ["LUR", "Ouss"],"current": 0,"board": [[59],[51,57,58]]}) == [43,56]