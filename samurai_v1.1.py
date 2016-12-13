##################################################################
##                                                              ##
##      CODIGO CRIADO PELO GRUPO TURING - POLI USP 2016         ##
##      https://www.facebook.com/grupoturing.poliusp            ##
##      Todos podem usar este codigo livremente                 ##
##                                                              ##
##################################################################


class Game:
    #criar tabuleiro:
    def __init__(self):

        #definindo o Turno
        self.turn = 0

        #definindo o Tabuleiro
        size = 15
        self.size = size
        row = size*[8]
        tabuleiro = []
        for i in range(size):
            tabuleiro.append(row[:])
        self.tab = tabuleiro

        #definindo os Jogadores
        #MUDAR PARA 1 e 2
        self.p1 = Jogador(0)
        self.p2 = Jogador(1)

        #Definindo as Homes Positions
        homes = []
        for i in range(len(self.p1.samurais)):
            self.tab[self.p1.samurais[i].y][self.p1.samurais[i].x] = i
            homes.append([(self.p1.samurais[i].y),(self.p1.samurais[i].x)])
        for i in range(len(self.p2.samurais)):
            self.tab[self.p2.samurais[i].y][self.p2.samurais[i].x] = i + 3
            homes.append([(self.p2.samurais[i].y),(self.p2.samurais[i].x)])
       
        self.homes = homes

    def view(self,player):
        #recebe todos os dados (turno, samurais, tabuleiro)
        
        print([self.turn])

        for i in range (3):
            s = []
            s.append(self.p1.samurais[i].x)#x
            s.append(self.p1.samurais[i].y)#y
            s.append(self.p1.samurais[i].order)#orderstatus
            s.append(self.p1.samurais[i].hide)#showingstatus
            s.append(self.p1.samurais[i].treat)#treatmentturns   
            print(s)

        for i in range (3):
            s = []
            s.append(self.p2.samurais[i].x)#x
            s.append(self.p2.samurais[i].y)#y
            s.append(self.p2.samurais[i].order)#orderstatus
            s.append(self.p2.samurais[i].hide)#showingstatus
            s.append(self.p2.samurais[i].treat)#treatmentturns   
            print(s)

        if player == -1:

            print(self.tab)

        else:
                
            size = self.size
            row = size*[9]
            newTab = []
            for i in range(size):
                newTab.append(row[:])

            if player == 0:
                for y1 in range (size):
                    for x1 in range (size):
                        for i in range(len(self.p1.samurais)):
                            x2 = self.p1.samurais[i].x
                            y2 = self.p1.samurais[i].y
                            if self.distancia(x1,x2,y1,y2)<=5:
                                newTab[y1][x1] = self.tab[y1][x1]

            if player == 1:
                for y1 in range (size):
                    for x1 in range (size):
                        for i in range(len(self.p1.samurais)):
                            x2 = self.p2.samurais[i].x
                            y2 = self.p2.samurais[i].y
                            if self.distancia(x1,x2,y1,y2)<=5:
                                newTab[y1][x1] = self.tab[y1][x1]


            for i in range (len(self.homes)):
                x = self.homes[i][1]
                y = self.homes[i][0]
                newTab[y][x] = self.tab[y][x]

            print(newTab)

    def score(self,player):

        size = self.size

        count = 0
        if player == 0:
            for y in range (size):
                for x in range (size):
                    for i in range(len(self.p1.samurais)):
                        if self.p1.samurais[i].ID == self.tab[y][x]:
                            count += 1
        elif player == 1:
            for y in range (size):
                for x in range (size):
                    for i in range(len(self.p2.samurais)):
                        if self.p2.samurais[i].ID + 3 == self.tab[y][x]:
                            count += 1
        return count
                       
 

    def distancia(self,x1,x2,y1,y2):
        d = abs(x1-x2)+abs(y1-y2)
        return d
               


class Jogador:
    def __init__(self,player):

        #self.p1 = player
        
        samurais = []
        if player == 0:
            samurais.append(Samurai(0,0,0))
            samurais.append(Samurai(1,0,7))
            samurais.append(Samurai(2,7,0))
        elif player == 1:
            samurais.append(Samurai(0,14,14))
            samurais.append(Samurai(1,14,7))
            samurais.append(Samurai(2,7,14))                
        self.samurais = samurais

    def order(self, order):
        #verifica se eh valido
        #order = order.split(' ')
        
        ID = order[0]
        
        for i in range(1,len(order)):
            self.samurais[ID].action(order)
            
class Samurai:
    def __init__(self,weaponID,x,y):
        self.ID = weaponID      
        self.homeX = x
        self.homeY = y
        self.x = x
        self.y = y
        self.order = 0
        self.hide = 0
        self.treat = 0

        if self.ID == 0:
            mask = [[0,1],[0,2],[0,3],[0,4]]
        elif self.ID == 1:
            mask = [[0,2],[0,1],[1,1],[1,0],[2,0]]
        elif self.ID == 2:
            mask = [[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]

        self.mask = mask

    def action(self,acao,game):

        #validar tretment status e order status
      
        if acao == 0:
            cont = self.stop(self)
        elif acao < 5:
            cont = self.occupy(self,acao,game)
        elif acao < 9:
            cont = self.move(self,acao,game)
        elif acao == 9:
            cont = self.hide(self,game)


    def stop(self):
        return False

    def move(self, acao):
        if acao == 5: #south
            y = self.y + 1
        elif acao == 6: #east
            x = self.x + 1
        elif acao == 7: #north
            y = self.y - 1
        elif acao == 8: #west
            x = self.x - 1

        if (valido):
            ''' fora do tabuleiro, 2 jogadores nao aparecendo e na mesma casa, nao eh home position, escondido saindo de area ocupada'''
            self.x = x
            self.y = y
            return True
        return False

    def occupy(self, acao):

        if acao == 1: #south
            #aplicar mascara no tabuleiro
            pass
        elif acao == 2: #east
            #aplicar mascara no tabuleiro
            pass
        elif acao == 3: #north
            #aplicar mascara no tabuleiro
            pass
        elif acao == 4: #west
            #aplicar mascara no tabuleiro
            pass

        return True

    def ocuppy(self, acao):
        ocupar=[]
        ''' condicoes de parada: Estar escondido '''

        if self.hide == 1:
            return False

        if(self.id = 0):
            ocupar = [(self.x, self.y+1), (self.x, self.y+2), (self.x, self.y+3), (self.x, self.y+4)]
        if(self.id = 1):
            ocupar = [(x, y+1), (x, y+2), (x+1, y+1), (x+1, y), (x+2, y)]
        if(self.id = 2):
            ocupar = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
        ''' rotacionar se for norte, leste -> ou oeste <- '''

        if acao == 1: #south
            ocupar = ocupar
        elif acao == 2: #east
            ocupar = ocupar*[(cos0,-sen0),(sen0,con0)]
        elif acao == 3: #north
            #aplicar mascara no tabuleiro
            pass
        elif acao == 4: #west
            #aplicar mascara no tabuleiro
            pass

    def hide(self):
        #verificar se possivel
        self.hide = 1-self.hide

        return True

def main():
    score1 = 0
    score2 = 0
    game = Game()
    
        
    
