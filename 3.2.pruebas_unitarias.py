from stream_cipher import encrypt_to_hex
from stream_cipher_decrypt import decrypt_from_hex

def test_descifrado_recupera_mensaje():
    msg = "Feliz Año Nuevo Chino"
    seed = 17022026
    c = encrypt_to_hex(msg, seed)
    recovered = decrypt_from_hex(c, seed)
    assert recovered == msg, "El descifrado no recuperó exactamente el mensaje original"
    print("Test descifrado y si recupera el mensaje")


def test_claves_diferentes_producen_cipher_diferente():
    msg = "Mensaje fijo"
    c1 = encrypt_to_hex(msg, 11111)
    c2 = encrypt_to_hex(msg, 22222)
    assert c1 != c2, "Dos claves diferentes produjeron el mismo ciphertext"
    print("\nTest de claves diferentes producen un cipher diferente")


def test_determinismo_misma_clave_mismo_cipher():
    msg = "Determinismo"
    seed = 99999
    c1 = encrypt_to_hex(msg, seed)
    c2 = encrypt_to_hex(msg, seed)
    assert c1 == c2, "La misma clave no produjo el mismo ciphertext"
    print("\nTest determinismo con misma clave y mismo cipher")


def test_mensajes_diferentes_longitudes():
    seed = 54321
    mensajes = [
        "",
        "A",
        "ABCDE",
        "A" * 100,
        "Año Nuevo Lunar",
    ]

    for msg in mensajes:
        c = encrypt_to_hex(msg, seed)
        recovered = decrypt_from_hex(c, seed)
        assert recovered == msg, f"Fallo con longitud {len(msg)}"
    print("\nTest de mensajes con diferentes longitudes")


def main():
    test_descifrado_recupera_mensaje()
    test_claves_diferentes_producen_cipher_diferente()
    test_determinismo_misma_clave_mismo_cipher()
    test_mensajes_diferentes_longitudes()
    print("\nTodas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    main()
