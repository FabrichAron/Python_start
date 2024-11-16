g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"""
                         {g[0]} | {g[1]} | {g[2]} 
                        -----------
                         {g[3]} | {g[4]} | {g[5]}
                        -----------
                         {g[6]} | {g[7]} | {g[8]} 
"""
      )
son = 0
while True:
    if son == 0:
        son = 1
        x = int(input('x= '))
        if 0 < x < 10 and type(g[x - 1]) != type("str"):
            g[x - 1] = 'X'
            print(f"""
                         {g[0]} | {g[1]} | {g[2]} 
                        -----------
                         {g[3]} | {g[4]} | {g[5]}
                        -----------
                         {g[6]} | {g[7]} | {g[8]} 
            """
                  )
            if g[0] == g[1] and g[1] == g[2] or g[3] == g[4] and g[4] == g[5] or g[6] == g[7] and g[7] == g[8] or g[
                0] == g[3] and g[3] == g[6] or g[1] == g[4] and g[4] == g[7] or g[2] == g[5] and g[5] == g[8] or g[0] == \
                    g[4] and g[4] == g[8] or g[2] == g[4] and g[4] == g[6]:
                print('X yutdi! tamom')
                break
            elif type(g[0]) == type(g[1]) == type(g[2]) == type(g[3]) == type(g[4]) == type(g[5]) == type(g[6]) == type(
                    g[7]) == type(g[8]) == type("str"):
                print('Durrang! tamom')
                break
        else:
            son = 0
            print("Kiritgan raqamingiz 1 va 9 orasidan tanlanmagan bolsin!")
    else:
        son = 0
        o = int(input('o= '))
        if 0 < o < 10 and type(g[o - 1]) != type("str"):
            g[o - 1] = 'O'
            print(f"""
                         {g[0]} | {g[1]} | {g[2]} 
                        -----------
                         {g[3]} | {g[4]} | {g[5]}
                        -----------
                         {g[6]} | {g[7]} | {g[8]} 
            """
                  )
            if g[0] == g[1] and g[1] == g[2] or g[3] == g[4] and g[4] == g[5] or g[6] == g[7] and g[7] == g[8] or g[
                0] == g[3] and g[3] == g[6] or g[1] == g[4] and g[4] == g[7] or g[2] == g[5] and g[5] == g[8] or g[0] == \
                    g[4] and g[4] == g[8] or g[2] == g[4] and g[4] == g[6]:
                print('0 yutdi! tamom')
                break
            elif type(g[0]) == type(g[1]) == type(g[2]) == type(g[3]) == type(g[4]) == type(g[5]) == type(g[6]) == type(
                    g[7]) == type(g[8]) == type("str"):
                print('Durrang! tamom')
                break
        else:
            son = 1
            print("Kiritgan raqamingiz 1 va 9 orasidan tanlanmagan bolsin!")