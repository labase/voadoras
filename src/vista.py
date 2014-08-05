__author__ = 'cetoli'
from __random import shuffle, choice, random

CARDS = 'ace 2 3 4 5 6 7 8 9 10 jack2 queen2 king2'.split()
CH = CV = 80
FACE = "/lib/cards/%s_of_%s.svg"
NAIPES = "clubs hearts spades diamonds".split()
PA = 16
SPLASH = None
SHUFFLESPEED = 0.1
SHUFFLEFACTOR = 64


class Carta:
    CLIP = []
    CLIP_POINTS = []
    def __init__(self, html, xy, deque, face=FACE % ('ace', 'clubs')):
        self.deque = deque
        self.clip = choice(Carta.CLIP)
        ct = self.e_carta = html.IMG(src=face, width=CH, heigth=CV, Class=self.clip)
        self.position(xy)
        ct.style.position = "absolute"
        ct.style.left, ct.style.top = xy
        deque <= ct
        ct.onclick = self.clicou
        ct.ontransitionend = self.bota
        self._clicou = self.voa

    def position(self, xy):
        x, y = self.pos = xy
        x /= SHUFFLEFACTOR
        d = SHUFFLESPEED
        self.e_carta.style.transition = \
            "left %fs linear %fs, top %fs linear %fs" % (d, x, d, x)

    def clicou(self, evento):
        self._clicou(evento)

    def centra(self):
        self._clicou = self._centra

    def _centra(self):
        self._clicou = lambda x: None

    def voa(self, evento):
        self.deque.voa()

    def voar(self, delta):
        dx, dy = delta
        x, y = self.pos
        xy = self.pos = x + dx, y + dy
        ct = self.e_carta
        ct.style.left, ct.style.top = xy

    def bota(self, ev=0):
        #SPLASH.html = "onde: %s, foi %s" % (self.pos, self.was)
        self.deque <= self.e_carta
        self.deque.conta()

    def voaraqui(self, xy):
        self.was = self.pos
        self.position(xy)
        ct = self.e_carta
        ct.style.left, ct.style.top = xy


class Deque:
    def __init__(self, html, tela):
        self.tela = tela
        self.count = 0
        self._voa = self.voar
        self.deque = [
            Carta(html, ((n*13+x)*PA, 50), self, FACE % (CARDS[x], naipe))
            for n, naipe in enumerate(NAIPES) for x in range(13)]

    def novoa(self):
        [carta.voar((100, 100)) for carta in self.deque[::-1]]

    def voa(self):
        self._voa()

    def voar(self):
        deque = self.deque[::-1]
        self.count = 0
        self._voa = lambda : None
        shuffle(deque)
        [carta.voaraqui((10+i*PA, 450)) for i, carta in enumerate(deque)]

    def __le__(self, other):
        self.tela <= other
        #if self.count >= 51:
        #    [carta.centra() for carta in enumerate(self.deque)]

    def centra(self):
        print("centra")

    def conta(self):
        self.count += 1
        if self.count >= 51:
            self._voa = self.centra


def main(html, doc, svg):

    def create_clips(tela):
        clip_style = ""
        clips = svg.svg()
        defs = svg.defs()
        clips <= defs

        def create_a_clip(a):
            Carta.CLIP += ["clip%d" % a]
            cs = ".clip%d {clip-path: url(#clipping%d);}\n" % (a, a)
            pt = "80,0 0,0" + "".join([" %d,%d" % (i, int(random()*40 +20)) for i in range(0,81,10)])
            #Carta.CLIP_POINTS.append[pt]
            clip = svg.clipPath(
                svg.polygon(points=pt), id="clipping%d" % a
                )
            defs <= clip
            return cs
        clip_style = "".join([create_a_clip(clip) for clip in range(10)])
        doc[html.HEAD][0] <= html.STYLE(clip_style)
        tela <= clips

    global SPLASH
    tela = doc["main"]
    tela.style.backgroundColor = "green"
    create_clips(tela)
    #SPLASH = html.DIV("VOADORAS")
    #tela <= SPLASH
    Deque(html, tela)