import RPi.GPIO as GP
import time


dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GP.setmode(GP.BCM)
GP.setup(dac, GP.OUT)
GP.setup(troyka, GP.OUT, initial=GP.HIGH)
GP.setup(comp, GP.IN)


def decToBin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]


def adc():
    ans = 0
    for it in range(7, -1, -1):
        ans |= (1 << it)

        dac_val = decToBin(ans)
        GP.output(dac, dac_val)
        time.sleep(0.1)
        comp_val = GP.input(comp)
        if comp_val:
            ans ^= (1 << it)
    return ans


try:
    while True:
        time.sleep(2.5)
        i = adc()
        print(f"i({i}): volt({i * 3.3 / 256})")
finally:
    GP.output(dac, 0)
    GP.cleanup()
    