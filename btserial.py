class BTSerial(object):
    import bluetooth

    def __init__(self):
        self.socket = []
        self.bluetooth_devices = []
        pass
    
    def scan(self):
        self.bluetooth_devices = bluetooth.discover_devices(lookup_names = True)
        print "found %d devices"%len(bluetooth_devices)
        for name, addr in self.bluetooth_devices:
            print " %s - %s"%(addr, name)
    
    def connect(self, device_id=0, channel=1):
        self.socket = bluetooth.BluetoothSocket(RFCOMM)
        self.socket.connect((self.bluetooth_devices[device_id][0], channel))
        self.socket.settimeout(1)
        
    def write(self, string):
        self.socket.send(string)
        
    def read(self):
        try:
            return self.socket.recv(1024)
        except BluetoothError:
            print 'timed out'
            return []
