from stream_cipher import encrypt_to_hex
from stream_cipher_decrypt import decrypt_from_hex

msg = "Hola"
seed_ok = 12345
seed_bad = 99999

c_hex = encrypt_to_hex(msg, seed_ok)
print("Mensaje:", msg)
print("Seed correcta:", seed_ok)
print("Cipher (HEX):", c_hex)

print("\nDescifrado con seed correcta:", decrypt_from_hex(c_hex, seed_ok))

try:
    print("Descifrado con seed incorrecta:", decrypt_from_hex(c_hex, seed_bad))
except Exception as e:
    print("Descifrado con seed incorrecta fallo (esperado):", type(e).__name__)
