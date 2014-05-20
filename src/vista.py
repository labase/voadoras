__author__ = 'cetoli'
FACE = 'http://thumbs.dreamstime.com/z/joker-playing-card-19231679.jpg'
CH = CV = 50


class Carta:
    def __init__(self, html, xy, deque):
        x, y = self.pos = xy
        self.deque = deque
        ct = self.e_carta = html.IMG(src=FACE, width=CH, heigth=CV)
        ct.style.position = "absolute"
        ct.style.left, ct.style.top = xy
        x = x / 5
        ct.style.transition = "left 2s linear %fs, top 2s linear %fs" % (x, x)
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
        self.deque = [Carta(html, (x*4, 10), self) for x in range(10)]

    def voa(self):
        [carta.voar((100, 100)) for carta in self.deque]

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