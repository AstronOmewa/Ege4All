#2
"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней. Игроки ходят по очереди, первый ход делает Петя. 
За один ход игрок может

добавить в одну из куч один камень или

увеличить количество камней в куче в два раза.

Например, пусть в одной куче 6 камней, а в другой  — 9 камней; такую позицию мы будем обозначать (6, 9). 
За один ход из позиции (6, 9) можно получить любую из четырёх позиций: (7, 9), (12, 9), (6, 10), (6, 18). Чтобы делать ходы, 
у каждого игрока есть неограниченное количество камней.

Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее 62. Победителем считается игрок, 
сделавший последний ход, то есть первым получивший позицию, в которой в кучах будет 62 или больше камней.

В начальный момент в первой куче было 10 камней, во второй куче  — S камней, 1 ≤ S ≤ 51.

Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника. Описать стратегию игрока  — 
значит, описать, какой ход он должен сделать в любой ситуации, которая ему может встретиться при различной игре противника. 
В описание выигрышной стратегии не следует включать ходы играющего по ней игрока, которые не являются для него безусловно выигрышными, 
то есть не гарантируют выигрыш независимо от игры противника.

Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:

—  Петя не может выиграть за один ход;

—  Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.

Найденные значения запишите в ответе в порядке возрастания без разделительных знаков.
"""

def game(s1, s2, m):
    if s1+s2 >= 52: return m%2==0
    if m==0: return 0

    h = [game(*move,m-1) for move in [(s1+1,s2), (s1*2, s2), (s1,s2+1), (s1,2*s2)]]

    if (m-1)%2==0:
        return any(h)
    else:
        return all(h)
    
print('20: ', *[s for s in range(1,52) if not game(10, s, 1) and game(10, s, 3)], sep='')
f = open('homework/301124/ans/2A.txt','w')
f.write('Answer: {}'.format(''.join([str(s) for s in range(1,52) if not game(10, s, 1) and game(10, s, 3)])))