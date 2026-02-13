def lcg_siguiente(x: int) -> int:
    a = 1103515245
    c = 12345
    m = 2**31
    return (a * x + c) % m

def keystream_bytes(seed: int, n_bytes: int) -> bytes:
    if n_bytes < 0:
        raise ValueError("n_bytes debe ser >= 0")

    x = seed
    out = bytearray()

    for _ in range(n_bytes):
        x = lcg_siguiente(x)
        out.append(x & 0xFF)

    return bytes(out)


if __name__ == "__main__":
    seed = 12345
    ks1 = keystream_bytes(seed, 16)
    ks2 = keystream_bytes(seed, 16)
    ks3 = keystream_bytes(seed + 1, 16)

    print("Keystream 1:", ks1.hex())
    print("Keystream 2:", ks2.hex())
    print("Determinístico (igual seed):", ks1 == ks2)
    print("Cambia con otra seed:", ks1 != ks3)
