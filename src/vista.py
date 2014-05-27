__author__ = 'cetoli'
#FACE = 'http://upload.wikimedia.org/wikipedia/commons/9/9b/Poker-sm-212-Ks.png'
FACE = 'http://upload.wikimedia.org/wikipedia/commons/3/36/Playing_card_club_%s.svg'
CARDS = 'ace 2 3 4 5 6 7 8 9 10 jack2 queen2 king2'.split()
CH = CV = 80
FACESVG = 'http://upload.wikimedia.org/wikipedia/commons/7/78/Contemporary_playing_cards.svg'
FACE = "/lib/cards/%s_of_%s.svg"
NAIPES = "clubs hearts spades diamonds".split()

class Carta:
    def __init__(self, html, xy, deque, face=FACE % ('ace', 'clubs')):
        x, y = self.pos = xy
        self.deque = deque
        ct = self.e_carta = html.IMG(src=face, width=CH, heigth=CV)
        ct.style.position = "absolute"
        ct.style.left, ct.style.top = xy
        x /= 8
        d = 0.6
        ct.style.transition = "left %fs linear %fs, top %fs linear %fs" % (d, x, d, x)
        deque <= ct
        ct.onclick = self.voa

    def voa(self, evento):
        self.deque.voa()

    def voar(self, delta):
        dx, dy = delta
        x, y = self.pos
        xy = self.pos = x + dx, y + dy
        ct = self.e_carta
        ct.style.left, ct.style.top = xy


class Deque:
    def __init__(self, html, tela):
        self.tela = tela
        self.deque = [
            Carta(html, ((n*13+x)*4, 10), self, FACE % (CARDS[x], naipe))
            for n, naipe in enumerate(NAIPES) for x in range(13)]

    def voa(self):
        [carta.voar((100, 100)) for carta in self.deque[::-1]]

    def __le__(self, other):
        self.tela <= other


def tabuleiro(tela, html):
    tabul = html.DIV()
    tela <= tabul


def embaralha(tela, html):
    pass


def voa(tela, html):
    pass


def main(html, doc):
    tela = doc["main"]
    #html = gui.html
    splash = html.DIV("VOADORAS")
    tela <= splash
    #tabuleiro(tela, html)
    #embaralha(tela, html)
    #voa(tela, html)
    deque = Deque(html, tela)