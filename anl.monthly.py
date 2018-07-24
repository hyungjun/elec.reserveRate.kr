import  os, sys
import  numpy   as np
import  pylab   as pl


class Data( object ):

    def __init__(self, srcpath):
        self.data   = [ l.strip().split('\t') for l in open( srcpath ) if not 'skip' in l ]

    def __getitem__(self, colidx):
        return np.array( zip( *self.data )[ colidx ][1:-10][::-1] ).astype('int')


def drawfig( yrs,mons, data ):

    datalen = len( data )
    tstamps = ['{}/{:02d}'.format( y,m ) for y,m in zip(yrs, mons)]

    fig     = pl.figure( figsize=(12,3) )
    ax      = fig.add_axes( [0.03, 0.16, 0.95, 0.75] )

    ax.plot( data )
    ax.hlines( [10], 0, datalen, color='r', linestyle='--' )

    ax.set_xticks( range(datalen)[::6] )
    ax.set_xticklabels( tstamps[::6], rotation=30 )
    ax.set_title('Reserve Rate (%)')

    return fig, ax


def main( *args ):
    print args

    datapath    = './pwrgenTrend.1993-2018.mon.txt'
    data        = Data( datapath )

    year        = data[0]
    mon         = data[1]
    saveratio   = data[7]

    fig, ax     = drawfig( year, mon, saveratio )
    #fig.savefig = './reserveRate.2003-2018.png'

    pl.show()

    '''
    for y in range(20):
        print y+2003
        print mon[y*12:(y+1)*12]
    '''



if __name__ == '__main__':
    main( *sys.argv )
