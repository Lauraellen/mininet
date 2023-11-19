from mininet.topo import Topo

class MyTopo( Topo ):
    "9 host 4 switch host custom topology"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host01 = self.addHost( 'h1' )
        host02 = self.addHost( 'h2' )
        host03 = self.addHost('h3')
        host04 = self.addHost('h4')
        host05 = self.addHost('h5')
        host06 = self.addHost('h6')
        host07 = self.addHost('h7')
        host08 = self.addHost('h8')
        host09 = self.addHost('h9')
        switch01 = self.addSwitch('s1')
        switch02 = self.addSwitch('s2')
        switch03 = self.addSwitch('s3')
        switch04 = self.addSwitch('s4')


        # Add links
        self.addLink( host01, switch01 )
        self.addLink( host02, switch01 )

        self.addLink(host03, switch02)
        self.addLink(host04, switch02)

        self.addLink(host05, switch03)
        self.addLink(host06, switch03)

        self.addLink(host07, switch04)
        self.addLink(host08, switch04)
        self.addLink(host09, switch04)

topos = { 'mytopo': ( lambda: MyTopo() ) }
