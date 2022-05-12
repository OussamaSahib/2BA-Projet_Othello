import pytest
import IA_aleatoire

def test_ia1():
    #CURRENT: 0= NOIR DE JOUER ET 1=BLANC DE JOUER
    assert IA_aleatoire.ia1({"players": ["LUR", "Ouss"],"current": 0,"board": [[28,35],[27,36]]}) == {'message': 'Ouss le + beau', 'move': 19, 'response':'move'} or {'message': 'Ouss le + beau', 'move': 26, 'response':'move'} or {'message': 'Ouss le + beau', 'move': 37, 'response':'move'} or {'message': 'Ouss le + beau', 'move': 44, 'response':'move'}
    assert IA_aleatoire.ia1({"players": ["LUR", "Ouss"],"current": 0,"board": [[35],[34]]}) == {'message': 'Ouss le + beau', 'move': 33, 'response':'move'} 
    assert IA_aleatoire.ia1({"players": ["LUR", "Ouss"],"current": 0,"board": [[62],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63]]}) == {'message': 'Ouss le + beau', 'move': 46, 'response':'move'} 