import btdht
import binascii
import hashlib
import bencodepy as bc
from time import sleep


def peer_tracker():
    with open("./file.torrent", "rb") as f:
        raw_data = f.read()
        data = bc.decode(raw_data)
        print(data.keys())
    info_hash = hashlib.sha1(bc.bencode(data[b"info"])).hexdigest()
    print(data[b"announce-list"])

    return info_hash


def get_peers(info_hash):

    dht = btdht.DHT()
    dht.start()
    sleep(15)  # wait for the DHT to build
    st = []
    count = 0
    # count for 1 minute
    while count < 1:
        st.append(dht.get_peers(binascii.a2b_hex(info_hash)))
        count += 1
        sleep(1)

    print(st)


if __name__ == "__main__":
    get_peers(peer_tracker())
