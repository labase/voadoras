__author__ = 'cetoli'
from __random import shuffle, choice, random

CARDS = 'ace 2 3 4 5 6 7 8 9 10 jack2 queen2 king2'.split()
CH = CV = 80
FACE = "/lib/cards/%s_of_%s.svg"
NAIPES = "clubs hearts spades diamonds".split()
PA = 16
SPLASH = None


class Carta:
    CLIP = []
    def __init__(self, html, xy, deque, face=FACE % ('ace', 'clubs')):
        self.deque = deque
        ct = self.e_carta = html.IMG(src=face, width=CH, heigth=CV, Class=choice(Carta.CLIP))
        self.position(xy)
        ct.style.position = "absolute"
        ct.style.left, ct.style.top = xy
        deque <= ct
        ct.onclick = self.voa
        ct.ontransitionend = self.bota

    def position(self, xy):
        x, y = self.pos = xy
        x /= 32
        d = 0.2
        self.e_carta.style.transition = \
            "left %fs linear %fs, top %fs linear %fs" % (d, x, d, x)

    def voa(self, evento):
        self.deque.voa()

    def voar(self, delta):
        dx, dy = delta
        x, y = self.pos
        xy = self.pos = x + dx, y + dy
        ct = self.e_carta
        ct.style.left, ct.style.top = xy

    def bota(self, ev=0):
        SPLASH.html = "onde: %s, foi %s" % (self.pos, self.was)
        self.deque <= self.e_carta

    def voaraqui(self, xy):
        self.was = self.pos
        self.position(xy)
        ct = self.e_carta
        ct.style.left, ct.style.top = xy


class Deque:
    def __init__(self, html, tela):
        self.tela = tela
        self.deque = [
            Carta(html, ((n*13+x)*PA, 50), self, FACE % (CARDS[x], naipe))
            for n, naipe in enumerate(NAIPES) for x in range(13)]

    def novoa(self):
        [carta.voar((100, 100)) for carta in self.deque[::-1]]

    def voa(self):
        deque = self.deque[::-1]
        shuffle(deque)
        [carta.voaraqui((10+i*PA, 250)) for i, carta in enumerate(deque)]

    def __le__(self, other):
        self.tela <= other

def main(html, doc, svg):

    def create_clips(tela):
        clip_style = ""
        clips = svg.svg()
        defs = svg.defs()
        clips <= defs

        def create_a_clip(a):
            Carta.CLIP += ["clip%d" % a]
            #doc[html.HEAD][0] <= html.STYLE(".clip%d {clip-path: url(#clipping%d);}" % (a, a))
            cs = ".clip%d {clip-path: url(#clipping%d);}\n" % (a, a)
            pt = "80,0 0,0"
            pt = "80,0 0,0" + "".join([" %d,%d" % (i, int(random()*40 +20)) for i in range(0,81,10)])
            clip = svg.clipPath(
                #svg.polygon(points="0,0 80,0 80,80 60,40 40,50 20,45 0,40"), id="clipping"
                svg.polygon(points=pt), id="clipping%d" % a
                )
            defs <= clip
            return cs
        #for clip in range(10):
        clip_style = "".join([    create_a_clip(clip) for clip in range(10)])
        doc[html.HEAD][0] <= html.STYLE(clip_style)
        tela <= clips

    global SPLASH
    tela = doc["main"]
    tela.style.backgroundColor = "green"
    create_clips(tela)
    #tela <= clip
    #html = gui.html
    SPLASH = html.DIV("VOADORAS")
    tela <= SPLASH
    Deque(html, tela)