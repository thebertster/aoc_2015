import hashlib

secret = "ckczppom"

coin = 1

while True:
    bitCoin = secret + str(coin)

    m = hashlib.md5()
    m.update(bytes(bitCoin,"ascii"))
    bitCoinHash = m.hexdigest()

    if bitCoinHash.startswith("000000"):
        print(coin)
        break;

    coin += 1