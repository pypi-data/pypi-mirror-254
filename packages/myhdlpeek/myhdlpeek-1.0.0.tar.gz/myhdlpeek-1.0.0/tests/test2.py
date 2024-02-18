
from random import randrange
from myhdl import Signal, Simulation, delay, always_comb, intbv, now, block, instance
from myhdlpeek import Peeker, PeekerGroup, show_text_table

@block
def Mux(z, a, b, sel):
    """ Multiplexer.

    z -- mux output
    a, b -- data inputs
    sel -- control input: select a if asserted, otherwise b

    """

    @always_comb
    def muxLogic():
        if sel == 1:
            z.next = a
        else:
            z.next = b

    grp = PeekerGroup(r=z, a=a, b=b, sel=sel)

    return (muxLogic, grp)


@block
def tb():
    # Once we've created some signals...
    z, a, b, z2 = [Signal(intbv(0, min=0, max=8)) for i in range(4)]
    sel = Signal(bool(0))

    PeekerGroup.clear()

    # ...it can be instantiated as follows
    mux_1 = Mux(z, a, b, sel)
    mux_2 = Mux(z2, b, a, sel)

    @instance
    def test():
        for i in range(8):
            a.next, b.next, sel.next = randrange(8), randrange(8), randrange(2)
            yield delay(2)

    return (test, mux_1, mux_2)


tb().run_sim()
# for p in Peeker.peekers():
# print(p.trace)
#print(Peeker.to_json('sel[0]', 'a[0]', 'b[0]', 'z[0]', start_time=3, stop_time=7))
peeker_groups = PeekerGroup.groups()
for grp in peeker_groups:
    grp.to_text_table()
print(Peeker.to_wavejson())
print(len(peeker_groups))
print(peeker_groups[0].r, peeker_groups[1].a, peeker_groups[0].b, peeker_groups[1].sel)
print(peeker_groups[0]['r'], peeker_groups[1]['a'], peeker_groups[0]['b'], peeker_groups[1]['sel'])
