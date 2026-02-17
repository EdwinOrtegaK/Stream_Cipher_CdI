from stream_cipher import encrypt_to_hex

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def main():
    m1 = "Pokemon Rojo Fuego"
    m2 = "Pokemon Verde Hoja"
    seed = 12345

    c1_hex = encrypt_to_hex(m1, seed)
    c2_hex = encrypt_to_hex(m2, seed)

    c1 = bytes.fromhex(c1_hex)
    c2 = bytes.fromhex(c2_hex)

    print("=== Mensajes originales ===")
    print("M1:", m1)
    print("M2:", m2)
    print("Seed reutilizada:", seed)

    print("\n=== Cifrados (HEX) ===")
    print("C1:", c1_hex)
    print("C2:", c2_hex)

    x = xor_bytes(c1, c2)

    print("\n=== Ataque: C1 XOR C2 ===")
    print("C1 XOR C2 (hex):", x.hex())

    m1b = m1.encode("utf-8")
    m2b = m2.encode("utf-8")
    mx = xor_bytes(m1b, m2b)

    print("\n=== Verificación ===")
    print("M1 XOR M2 (hex):", mx.hex())
    print("\n¿C1 XOR C2 == M1 XOR M2?", x == mx)

    recovered_m2 = xor_bytes(x, m1b).decode("utf-8", errors="replace")

    print("\n=== Si el atacante conoce M1, recupera M2 ===")
    print("M2 recuperado:", recovered_m2)


if __name__ == "__main__":
    main()
