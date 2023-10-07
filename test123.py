import secp256k1 as ice
import random
import dask

max_p = 115792089237316195423570985008687907852837564279074904382605163141518161494336


def RandomInteger(minN, maxN):
    return random.randrange(minN, maxN)

@dask.delayed
def Random_Bruteforce(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce1(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce1 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce1 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce1 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce2(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce1 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce2 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce2 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce3(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce3 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce3 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce3 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce4(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce4 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce4 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce4 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce5(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce5 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce5 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce5 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce6(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce6 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce6 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce6 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce7(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce7 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce7 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce7 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce8(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce8 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce8 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce8 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce9(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce9 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce9 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce9 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce10(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce10 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce10 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce10 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
                

@dask.delayed
def Random_Bruteforce11(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce11 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce11 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce11 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')

@dask.delayed
def Random_Bruteforce12(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce12 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce12 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce12 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce13(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce13 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce13 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce13 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')               


@dask.delayed
def Random_Bruteforce14(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce14 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce14 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce14 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n') 


@dask.delayed
def Random_Bruteforce15(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce15 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce15 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce15 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n') 


@dask.delayed
def Random_Bruteforce16(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce16 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce16 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce16 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')  


@dask.delayed
def Random_Bruteforce17(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce17 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce17 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce17 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n') 


@dask.delayed
def Random_Bruteforce18(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce18 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce18 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce18 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n') 


@dask.delayed
def Random_Bruteforce19(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce19 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce19 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce19 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')


@dask.delayed
def Random_Bruteforce20(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address (0, False, dec)
        print(f'Instance: Random_Bruteforce20 Address {caddr} - {uaddr} ', end="\r")
        if address_to_find in caddr or address_to_find in uaddr:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            wifu = ice.btc_pvk_to_wif(HEX, False)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce20 - Found: {caddr} - {uaddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce20 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\nBTC Address Uncompressed: {uaddr} \nWIF Uncompressed: {wifu}\n')   
def main():
    x = dask.delayed(Random_Bruteforce(1157920892373161954235709850, max_p))
    y = dask.delayed(Random_Bruteforce1(115792089237316195423570985008, max_p))
    z = dask.delayed(Random_Bruteforce2(11579208923731619542357098500899, max_p))
    x1 = dask.delayed(Random_Bruteforce3(1157920892373161954235709850089999, max_p))
    y1 = dask.delayed(Random_Bruteforce4(1157920892373161954235709850089999999, max_p))
    z1 = dask.delayed(Random_Bruteforce5(115792089237316195423570985008999999999, max_p))
    x2 = dask.delayed(Random_Bruteforce6(11579208923731619542357098500899999999999, max_p))
    y2 = dask.delayed(Random_Bruteforce7(11579208923731619542357098500899999999999999, max_p))
    z2 = dask.delayed(Random_Bruteforce8(1157920892373161954235709850089999999999999999, max_p))
    x3 = dask.delayed(Random_Bruteforce9(11579208923731619542357098500899999999999999999999, max_p))
    y3 = dask.delayed(Random_Bruteforce10(1157920892373161954235709850089999999999999999999999, max_p))
    z3 = dask.delayed(Random_Bruteforce11(115792089237316195423570985008999999999999999999999999, max_p))
    x4 = dask.delayed(Random_Bruteforce12(11579208923731619542357098500899999999999999999999999999, max_p))
    y4 = dask.delayed(Random_Bruteforce13(115792089237316195423570985008999999999999999999999999999, max_p))
    z4 = dask.delayed(Random_Bruteforce14(1157920892373161954235709850089999999999999999999999999999, max_p))
    x5 = dask.delayed(Random_Bruteforce15(11579208923731619542357098500899999999999999999999999999999, max_p))
    y5 = dask.delayed(Random_Bruteforce16(115792089237316195423570985008999999999999999999999999999999, max_p))
    z5 = dask.delayed(Random_Bruteforce17(1157920892373161954235709850089999999999999999999999999999999, max_p))
    x6 = dask.delayed(Random_Bruteforce18(115792089237316195423570985008999999999999999999999999999999999, max_p))
    y6 = dask.delayed(Random_Bruteforce19(1157920892373161954235709850089999999999999999999999999999999999, max_p))
    z6 = dask.delayed(Random_Bruteforce20(11579208923731619542357098500899999999999999999999999999999999999, max_p))
    dask.compute(x,y,z,x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,x5,y5,z5,x6,y6,z6)
    
    
if __name__ == '__main__':
    address_to_find = input("Adresa ? ")
    main()