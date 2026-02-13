from __future__ import annotations
import base64
from keystream import keystream_bytes

def xor_bytes(a: bytes, b: bytes) -> bytes:
    if len(a) != len(b):
        raise ValueError("Para XOR, ambos byte-strings deben tener la misma longitud")
    return bytes(x ^ y for x, y in zip(a, b))

def encrypt_to_hex(plaintext: str, seed: int) -> str:
    pt = plaintext.encode("utf-8")
    ks = keystream_bytes(seed, len(pt))
    ct = xor_bytes(pt, ks)
    return ct.hex()

def encrypt_to_base64(plaintext: str, seed: int) -> str:
    pt = plaintext.encode("utf-8")
    ks = keystream_bytes(seed, len(pt))
    ct = xor_bytes(pt, ks)
    return base64.b64encode(ct).decode("ascii")


if __name__ == "__main__":
    mensaje = input("Ingrese el mensaje (plaintext): ")
    seed = int(input("Ingrese la seed (entero): "))

    c_hex = encrypt_to_hex(mensaje, seed)
    c_b64 = encrypt_to_base64(mensaje, seed)

    print("\nCiphertext (HEX): ", c_hex)
    print("Ciphertext (Base64): ", c_b64)
