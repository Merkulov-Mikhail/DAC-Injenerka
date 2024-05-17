import RPi.GPIO as GP
import time


def adc():
    for it in range(256):
        dac_val = decToBin(it)
        GP.output(dac, dac_val)
        comp_val = GP.input(comp)
        time.sleep(0.05)
        if comp_val:
            return it
    return 255


def decToBin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]


dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GP.setmode(GP.BCM)
GP.setup(dac, GP.OUT)
GP.setup(troyka, GP.OUT, initial=GP.HIGH)
GP.setup(comp, GP.IN)


try:
    while True:
        i = adc()
        print(f"i({i}): volt({i * 3.3 / 256})")
finally:
    GP.output(dac, 0)
    GP.cleanup()
    