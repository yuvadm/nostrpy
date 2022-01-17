import csv

from pathlib import Path
from typing import Any

from nostr.bip340 import pubkey_gen, schnorr_sign, schnorr_verify

TEST_VECTORS = Path(__file__).parent / "test-vectors.csv"


def test_vectors():
    with open(TEST_VECTORS, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip column titles

        for row in reader:
            (
                index,
                seckey_hex,
                pubkey_hex,
                aux_rand_hex,
                msg_hex,
                sig_hex,
                result_str,
                comment,
            ) = row

            pubkey = bytes.fromhex(pubkey_hex)
            msg = bytes.fromhex(msg_hex)
            sig = bytes.fromhex(sig_hex)
            result = result_str == "TRUE"

            if seckey_hex != "":
                seckey = bytes.fromhex(seckey_hex)
                pubkey_actual = pubkey_gen(seckey)
                assert pubkey == pubkey_actual
                aux_rand = bytes.fromhex(aux_rand_hex)
                sig_actual = schnorr_sign(msg, seckey, aux_rand)
                assert sig == sig_actual

            result_actual = schnorr_verify(msg, pubkey, sig)
            assert result == result_actual
