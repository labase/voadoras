__author__ = 'cetoli'
from __random import shuffle, choice, random
from browser.ajax import ajax

CARDS = 'ace 2 3 4 5 6 7 8 9 10 jack2 queen2 king2'.split()
CH = CV = 80
FACE = "/lib/cards/%s_of_%s.svg"
NAIPES = "clubs hearts spades diamonds".split()
PA = 16
PB = 75
SPLASH = None
SHUFFLESPEED = 0.1
SHUFFLEFACTOR = 128


class Carta:
    CLIP = []
    CLIP_POINTS = []
    def __init__(self, html, xy, deque, face=('ace', 'clubs')):
        self.deque = deque
        self.face = face
        self.clip = choice(Carta.CLIP)
        ct = self.e_carta = html.IMG(src=FACE % face, width=CH, heigth=CV, Class=self.clip)
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
        self.deque.voa(evento, self)

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
        def set_id(gid):
            self.gid = gid
            print(gid)
        self.tela = tela
        self.count = 0
        self._voa = self.voar
        self._cartear = self.cartear
        self.deque = [
            Carta(html, ((n*13+x)*PA, 50), self, (CARDS[x], naipe))
            for n, naipe in enumerate(NAIPES) for x in range(13)]
        self.send('getid', {}, set_id, "GET")

    def send(self, operation, data, action=lambda t: None, method="POST"):
        def on_complete(req):
            if req.status==200 or req.status==0:
                print( req.text)
                action(req.text)
            else:
                print( "error "+req.text)
        req = ajax()
        req.on_complete = on_complete
        url = "/record/"+ operation
        req.open(method,url,True)
        req.set_header("Content-Type","application/json; charset=utf-8")
        req.send(data)

    def voa(self, evento, carta):
        self._voa(evento, carta)

    def pontua(self, evento, carta, ponto, valor):
        carta = '_'.join(carta.face)
        casa = '_'.join([str(evento.x), str(evento.y)])
        data = dict(doc_id=self.gid, carta=carta, casa=casa, move="ok", ponto=ponto, valor=valor)
        self.send('store',data )

    def cartear(self, evento, cartaid):
        deque = self.deque[::-1]
        self.count = 0
        self._cartear = lambda : None
        shuffle(deque)
        [carta.voaraqui((10+(i%13)*PB, 10+(i//13)*PB*2)) for i, carta in enumerate(deque)]
        self.pontua(evento, cartaid, 1, 'ct')

    def voar(self, evento, carta):
        deque = self.deque[::-1]
        self.count = 0
        self._voa = lambda : None
        shuffle(deque)
        [carta.voaraqui((10+i*PA, 550)) for i, carta in enumerate(deque)]
        self.pontua(evento, carta, 2, 'em')

    def __le__(self, other):
        self.tela <= other
        #if self.count >= 51:
        #    [carta.centra() for carta in enumerate(self.deque)]

    def centra(self):
        print("centra")

    def conta(self):
        self.count += 1
        if self.count >= 51:
            self._voa = self._cartear


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