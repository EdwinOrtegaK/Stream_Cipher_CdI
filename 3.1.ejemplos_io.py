from stream_cipher import encrypt_to_hex
from stream_cipher_decrypt import decrypt_from_hex

def ejemplo(mensaje, seed):
    cipher = encrypt_to_hex(mensaje, seed)
    recovered = decrypt_from_hex(cipher, seed)

    print("Texto plano:     ", mensaje)
    print("Clave utilizada: ", seed)
    print("Texto cifrado:   ", cipher)
    print("Texto descifrado:", recovered)
    print("-" * 50)

def main():
    ejemplo("Hola Mundo", 12345)
    ejemplo("Año Nuevo Lunar", 170226)
    ejemplo("AAAAAAA", 55555)

if __name__ == "__main__":
    main()
