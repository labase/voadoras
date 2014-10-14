__author__ = 'cetoli'
from __random import shuffle, choice, random
from browser.ajax import ajax

CARDS = 'ace 2 3 4 5 6 7 8 9 10 jack2 queen2 king2'.split()
CH = CV = 60
FACE = "/lib/cards/%s_of_%s.svg"
NAIPES = "clubs hearts spades diamonds".split()
PA = 16
BB = 60
PB = 61
SPLASH = None
SHUFFLESPEED = 0.02
SHUFFLEFACTOR = 128


class Carta:
    CLIP = []
    CLIP_POINTS = []
    CARDS = {}
    def __init__(self, html, xy, deque, face=('ace', 'clubs'), version=("0", ), sp=True):
        self.html = html
        self.xy = xy
        self.deque = deque
        self.face = face + version
        self.clip = choice(Carta.CLIP)
        name = "".join(self.face)
        Carta.CARDS[name]=self
        ct = self.e_carta = html.IMG(Id=name, src=FACE % face, width=CH, heigth=CV, Class=self.clip)
        if sp:
            self.position(xy)
        ct.style.position = "absolute"
        ct.style.left, ct.style.top = xy
        deque <= ct
        ct.onclick = self.clicou
        ct.ontransitionend = self.bota
        ct.ondragstart = self.drag_start
        #self._clicou = self.voa

    def fix(self, x, y):
        ct = self.e_carta
        face = tuple(self.face[:-1])
        newversion = (str(int(self.face[-1]) +1 ), )
        xy = int(ct.style.left[:-2]), int(ct.style.top[:-2])
        print (face, newversion)
        Carta(self.html, xy, self.deque, face, newversion, False)
        print('fix',self.face,x, y)
        ct.style.transition = ""
        ct.style.left, ct.style.top = x, y
        ct.style.cursor = "auto"
        ct.draggable = False

    def position(self, xy):
        x, y = self.pos = xy
        x /= SHUFFLEFACTOR
        d = SHUFFLESPEED
        self.e_carta.style.transition = \
            "left %fs linear %fs, top %fs linear %fs" % (d, x, d, x)

    def clicou(self, evento):
        self.deque.acao(evento, self)

    def centra(self):
        self._clicou = self._centra

    def arrastavel(self):
        self.e_carta.draggable = True
        #self.e_carta.style.cursor = "move"

    def drag_start(self, ev):
        print('drag_start',ev.target.id)
        ev.data['text']=ev.target.id
        ev.data.effectAllowed = 'move'

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
    def __init__(self, html, tela, doc):
        self.doc = doc
        def set_id(gid):
            self.gid = gid
            print(gid)
        self.tela = tela
        self.discard = d = html.DIV(Id = "discard")
        s = d.style
        s.left, s.top, s.width, s.height, s.background= 900, 200, 200, 200, "blue"
        s.position = "absolute"
        self.tela <= self.discard
        d.ondrop = self.drop
        d.ondragover = self.drag_over
        self.count = 0
        self._voa = self.voar
        self._cartear = self.cartear
        self.next_state = self.cartear
        self.next_action = lambda: None
        self.deque = [
            Carta(html, ((n*13+x)*PA, 50), self, (CARDS[x], naipe))
            for n, naipe in enumerate(NAIPES) for x in range(13)]
        self.send('getid', {}, set_id, "GET")

    def drag_over(self, ev):
        print('drop',ev.target.id)

        ev.data.dropEffect = 'move'
        ev.preventDefault()

    def drop(self, ev):
        src_id = ev.data['text']
        elt = self.doc[src_id]
        ev.preventDefault()
        Carta.CARDS[src_id].fix(ev.x, ev.y)
        return
        if ev.target.id=="discard":
            print('drop',ev.target.id, src_id, ev.x, ev.y)
            elt.style.left = ev.x-elt.clientWidth/2
            elt.style.top = ev.y-elt.clientHeight/2
            elt.draggable = False # don't drag any more
            elt.style.cursor = "auto"
            print('drop',ev.target.id, src_id, ev.x, ev.y)


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

    def acao(self, evento, carta):
        self._voa(evento, carta)

    def pontua(self, evento, carta, ponto, valor):
        carta = '_'.join(carta.face)
        casa = '_'.join([str(evento.x), str(evento.y)])
        data = dict(doc_id=self.gid, carta=carta, casa=casa, move="ok", ponto=ponto, valor=valor)
        self.send('store',data )

    def cartear(self, evento, cartaid):
        deque = self.deque[::-1]
        self.count = 0
        self._cartear = lambda x, y=0: None
        shuffle(deque)
        [carta.voaraqui((BB+(i%13)*PB, BB+(i//13)*PB*2)) for i, carta in enumerate(deque)]
        self.pontua(evento, cartaid, 1, 'ct')
        self.next_state = lambda e,c : None
        self.next_action = self.arrastar

    def arrastar(self):
        print('arrastar')
        for umacarta in self.deque:
            umacarta.arrastavel()

    def voar(self, evento, carta):
        deque = self.deque[::-1]
        self.count = 0
        self._voa = lambda x, y=0: None
        shuffle(deque)
        [acarta.voaraqui((10+i*PA, 550)) for i, acarta in enumerate(deque)]
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
            self._voa = self.next_state
            self.next_action()


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
    Deque(html, tela, doc)