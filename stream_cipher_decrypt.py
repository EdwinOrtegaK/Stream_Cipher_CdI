from keystream import keystream_bytes
from stream_cipher import xor_bytes
import base64

def decrypt_from_hex(ciphertext: str, seed: int) -> str:
    ciphertext_bytes = bytes.fromhex(ciphertext)
    ks = keystream_bytes(seed, len(ciphertext_bytes))
    pt_bytes = xor_bytes(ciphertext_bytes, ks)
    return (pt_bytes.decode("utf-8"))

def decrypt_from_base64(ciphertext: str, seed: int) -> str:
    ciphertext_bytes = base64.b64decode(ciphertext)
    ks = keystream_bytes(seed, len(ciphertext_bytes))
    pt_bytes = xor_bytes(ciphertext_bytes, ks)
    return (pt_bytes.decode("utf-8"))


if __name__ == "__main__":
    print("1. HEX 2. BASE64")
    while True: 
        op = input("¿Que desea decifrar? (1/2): ").strip()
        if op == "1":
            cifrado = input("\nIngrese el menaje a decifrar en HEX: ").strip()
            seed = int(input("Ingrese la seed (entero): "))
            try:
                decifrado = decrypt_from_hex(cifrado, seed)
                print("\nMensaje descifrado: ", decifrado)
                break
            except ValueError:
                print("\nHEX inválido o seed incorrecta\n")
                continue
        elif op == "2":
            cifrado = input("\nIngrese el menaje a decifrar en BASE64: ").strip()
            seed = int(input("Ingrese la seed (entero): "))
            try: 
                decifrado = decrypt_from_base64(cifrado, seed)
                print("\nMensaje descifrado: ", decifrado)
                break
            except ValueError:
                print("\nBASE64 inválido o seed incorrecta\n")
                continue
        else:
            print("\nIngrese una opción valida\n")
