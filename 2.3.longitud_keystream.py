from stream_cipher import encrypt_to_hex

def main():
    mensaje = "A" * 20
    seed = 12345

    print("Mensaje: ", mensaje)
    print("Seed: ", seed)

    # Keystream igual al mensaje
    c_normal = encrypt_to_hex(mensaje, seed)
    print("\n1) Keystream igual al mensaje: ")
    print(c_normal)

    # Keystream más largo que el mensaje
    mensaje_largo = "A" * 50
    c_largo = encrypt_to_hex(mensaje_largo, seed)
    prefijo = c_largo[:len(mensaje) * 2]
    print("\n2) Keystream más largo (prefijo): ")
    print(prefijo)
    print("\n¿Prefijo == normal?", prefijo == c_normal)

    # Keystream corto y repetido
    key_corta = b"ABCDE"
    msg_bytes = mensaje.encode("utf-8")
    key_repetida = (key_corta* (len(msg_bytes) // len(key_corta) + 1))[:len(msg_bytes)]
    c_corto = bytes(x ^ y for x, y in zip(msg_bytes, key_repetida))

    print("\n3) Keystream corto repetido: ")
    print(c_corto.hex())

if __name__ == "__main__":
    main()
