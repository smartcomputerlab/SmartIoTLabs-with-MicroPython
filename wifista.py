from machine import Pin

def scan():
    import network
    station = network.WLAN(network.STA_IF)
    station.active(True)

    for (ssid, bssid, channel, RSSI, authmode, hidden) in station.scan():
        print("* {:s}".format(ssid))
        print(" - Channel: {}".format(channel))
        print(" - RSSI: {}".format(RSSI))
        print(" - BSSID: {:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*bssid))
        print()


def connect():
    import network
    ssid      = "SmartIoTLab"
    password  =  ""
    
    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("Already connected")
        return station
 
    station.active(True)
    station.connect(ssid,password)
    
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())
    return station

def disconnect():
    import network
    station = network.WLAN(network.STA_IF)
    station.disconnect()
    station.active(False)
    

scan()
disconnect()
connect()
 