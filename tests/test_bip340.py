#
# The following code is only used to verify the test vectors.
#
import csv
import os
import sys


def test_vectors() -> bool:
    all_passed = True
    with open(os.path.join(sys.path[0], "test-vectors.csv"), newline="") as csvfile:
        reader = csv.reader(csvfile)
        reader.__next__()
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
            print("\nTest vector", ("#" + index).rjust(3, " ") + ":")
            if seckey_hex != "":
                seckey = bytes.fromhex(seckey_hex)
                pubkey_actual = pubkey_gen(seckey)
                if pubkey != pubkey_actual:
                    print(" * Failed key generation.")
                    print("   Expected key:", pubkey.hex().upper())
                    print("     Actual key:", pubkey_actual.hex().upper())
                aux_rand = bytes.fromhex(aux_rand_hex)
                try:
                    sig_actual = schnorr_sign(msg, seckey, aux_rand)
                    if sig == sig_actual:
                        print(" * Passed signing test.")
                    else:
                        print(" * Failed signing test.")
                        print("   Expected signature:", sig.hex().upper())
                        print("     Actual signature:", sig_actual.hex().upper())
                        all_passed = False
                except RuntimeError as e:
                    print(" * Signing test raised exception:", e)
                    all_passed = False
            result_actual = schnorr_verify(msg, pubkey, sig)
            if result == result_actual:
                print(" * Passed verification test.")
            else:
                print(" * Failed verification test.")
                print("   Expected verification result:", result)
                print("     Actual verification result:", result_actual)
                if comment:
                    print("   Comment:", comment)
                all_passed = False
    print()
    if all_passed:
        print("All test vectors passed.")
    else:
        print("Some test vectors failed.")
    return all_passed


#
# The following code is only used for debugging
#
import inspect


def pretty(v: Any) -> Any:
    if isinstance(v, bytes):
        return "0x" + v.hex()
    if isinstance(v, int):
        return pretty(bytes_from_int(v))
    if isinstance(v, tuple):
        return tuple(map(pretty, v))
    return v


def debug_print_vars() -> None:
    if DEBUG:
        current_frame = inspect.currentframe()
        assert current_frame is not None
        frame = current_frame.f_back
        assert frame is not None
        print(
            "   Variables in function ",
            frame.f_code.co_name,
            " at line ",
            frame.f_lineno,
            ":",
            sep="",
        )
        for var_name, var_val in frame.f_locals.items():
            print("   " + var_name.rjust(11, " "), "==", pretty(var_val))


if __name__ == "__main__":
    test_vectors()
