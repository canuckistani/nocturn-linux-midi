from NocturnHardware import *

#    Knobs Data:         64  ->  71
#    X Fader:            72
#    X Fader Touch:      83
#    Speed Dial:         74
#    Speed Dial Touch:   82
#    Knobs Touch:        96  ->  103
#    Top Button Row:     112 ->  119
#    Bottom Button Row:  120 ->  127

def initializeNocturn(connection):
    try:
        connection.setLEDRingMode(8, 0)
    except e:
        print(e)



if __name__ == "__main__":
    nh = NocturnHardware()
    nh.clearAll()
    try:
        while True:
            value = nh.processedRead()
            if value != None:
                print(value)
    except KeyboardInterrupt as e:
        sys.exit(e)
