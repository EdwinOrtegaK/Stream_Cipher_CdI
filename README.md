# Stream Cipher - Cifrados de Información

## Descripción del proyecto

Este proyecto implementa un cifrado de flujo (Stream Cipher) básico
utilizando la operación XOR y un generador pseudoaleatorio (PRNG) para
la creación del keystream.

El objetivo del laboratorio es comprender:

-   El concepto de keystream y su rol en los cifrados de flujo.
-   Cómo funciona el cifrado y descifrado mediante XOR.
-   Las vulnerabilidades asociadas con la reutilización del keystream.
-   El impacto de la clave (seed) en la seguridad del sistema.

La implementación está desarrollada en Python y permite cifrar y
descifrar mensajes utilizando una clave numérica como semilla del
generador pseudoaleatorio.

## Estructura del proyecto

Stream_Cipher_CdI/
    ├── keystream.py
    ├── stream_cipher.py 
    ├── stream_cipher_decrypt.py 
    ├── variacion_seed.py 
    ├── README.md

-   keystream.py: Generación determinística del keystream.
-   stream_cipher.py: Funciones de cifrado.
-   stream_cipher_decrypt.py: Funciones de descifrado.
-   variacion_seed.py: Demostración del impacto de cambiar la seed.

## Instrucciones de instalación y uso

### Requisitos

-   Python 3.10 o superior.
-   No se requieren librerías externas.

### Ejecutar el cifrado

Desde la raíz del proyecto:

    python stream_cipher.py

O dependiendo de lo que quieras correr, solo es necesario
correr ese unico archivo para que funcione.

### Ejecutar la demostración de variación de seed (Parte 2.1)

    python 2.1.variacion_seed.py

## Ejemplos de ejecución

### Ejemplo 1 -- Cifrado y descifrado correcto

Mensaje: Hola
Seed correcta: 12345
Cipher (HEX): 36b04094

Salida:

Descifrado con seed correcta: Hola

### Ejemplo 2 -- Descifrado con seed incorrecta

Seed incorrecta: 99999

Salida:

Descifrado con seed incorrecta fallo (esperado): UnicodeDecodeError

Esto demuestra que una seed distinta genera un keystream diferente y no
permite recuperar el mensaje original.

## Respuestas a las preguntas de análisis

### 2.1 Variación de la Clave

Cuando se cambia la seed utilizada para generar el keystream, la
secuencia de bytes generada por el PRNG cambia completamente.

Como el cifrado se realiza mediante la operación:

Cipher = Mensaje XOR Keystream

si el keystream cambia, el ciphertext también cambia. Intentar descifrar
un mensaje con una seed distinta produce un resultado incorrecto o
ilegible.

Esto demuestra que la seguridad del sistema depende totalmente de la
confidencialidad y exactitud de la seed.

### 2.2 Reutilización del Keystream

Si se utiliza la misma seed para cifrar dos mensajes distintos, el mismo
keystream será generado.

Si C1 = M1 XOR Keystream y C2 = M2 XOR Keystream
y el atacante calcula C1 XOR C2 obtiene M1 XOR M2

El keystream se cancela, permitiendo obtener la relación entre los dos
mensajes originales.

Esto representa una vulnerabilidad grave, ya que reutilizar el mismo
keystream compromete la confidencialidad del sistema. Siendo que si 
el atacante conoce uno de los mensajes, puede lelgar a conocer el otro.

### 2.3 Longitud del Keystream

Si el keystream es más corto que el mensaje y se repite, la seguridad se
ve comprometida porque aparecen patrones repetitivos.

Si el keystream tiene la misma longitud que el mensaje, el cifrado
funciona correctamente.

Si es más largo, no afecta negativamente, siempre que no se reutilice
para otros mensajes.

### 2.4 Consideraciones Prácticas

La implementación desarrollada es adecuada con fines educativos, pero no 
es segura para uso en producción. Ya que en un entorno real de producción
presenta limitaciones importantes de seguridad.

En primer lugar, utiliza un PRNG básico (LCG), el cual no es criptográficamente 
seguro y puede ser predecible. En entornos reales deben emplearse generadores 
criptográficamente seguros y algoritmos modernos como ChaCha20 o AES-CTR.

En segundo lugar, la reutilización de la misma seed implica reutilización 
del keystream, lo que rompe la confidencialidad, como se demostró en la 
sección 2.2. En la práctica se utilizan nonces o IV únicos por mensaje 
para evitar este problema.

Finalmente, el sistema no incluye autenticación, por lo que es vulnerable 
a modificaciones del ciphertext. En sistemas reales se emplean esquemas de 
cifrado autenticado (AEAD) para garantizar tanto confidencialidad como 
integridad.

En conclusión, el modelo implementado es correcto a nivel conceptual, 
pero requiere mejoras significativas para ser seguro en un entorno real.

## Validación y Pruebas

### 3.1 Ejemplos de Entrada/Salida

Ejemplo 1:

- Texto plano: Hola Mundo  
- Clave utilizada: 12345  
- Texto cifrado (HEX): 36b04094aab66d1f32b8  
- Texto descifrado: Hola Mundo  

Ejemplo 2:

- Texto plano: Año Nuevo Lunar  
- Clave utilizada: 1702  
- Texto cifrado (HEX): a6578c5da34e4c1ba943d5c68e761024  
- Texto descifrado: Año Nuevo Lunar  

Ejemplo 3:

- Texto plano: AAAAAAA  
- Clave utilizada: 55555  
- Texto cifrado (HEX): c1f8bf1eed344b  
- Texto descifrado: AAAAAAA  

## Reflexión Técnica

### 4.1 Limitaciones de PRNG Simples (LCG / random.Random)

Los PRNG simples (por ejemplo, LCG o generadores no criptográficos) no son 
adecuados para criptografía porque su salida puede presentar debilidades 
explotables:

- Predictibilidad: si un atacante observa suficiente salida (keystream o 
partes del ciphertext) puede inferir el estado interno o predecir valores 
futuros. En criptografía se requiere un CSPRNG (Cryptographically Secure 
PRNG), diseñado para resistir predicción incluso con conocimiento parcial 
de la salida.

- Periodicidad: los PRNG simples tienen un período finito; eventualmente 
la secuencia se repite. Si el keystream se repite, reaparecen patrones y 
se facilita el criptoanálisis. Por eso en stream ciphers, la repetición es 
especialmente peligrosa.

- Calidad estadística del keystream: aunque un PRNG simple “parezca aleatorio”, 
puede tener sesgos o correlaciones internas. En cifrado, esas pequeñas 
desviaciones pueden convertirse en fugas de información, sobre todo cuando 
se cifran muchos mensajes o estructuras repetitivas.

Por eso un PRNG simple puede ser suficiente para simulaciones, pero no para 
generar keystreams en aplicaciones criptográficas reales.

### Comparación con Stream Ciphers Modernos (ChaCha20 y AES-CTR)

#### ¿Cómo generan keystreams?

ChaCha20 es un stream cipher moderno que genera el keystream a partir de una 
clave de 256 bits, un nonce (típicamente 96 bits) y un contador de bloque. 
Su estado interno se transforma con rondas diseñadas para producir salida con 
alta difusión y resistencia criptanalítica.

AES-CTR no es “un stream cipher” puro, sino un modo de operación de un cifrador 
por bloques (AES). Convierte AES en un generador de keystream cifrando valores 
de contador: keystream = AES_K(counter), y luego se hace XOR con el mensaje.

#### ¿Qué mejoras de seguridad ofrecen?

Usan primitivas con diseño y análisis criptográfico moderno (no linealidad 
fuerte, difusión, resistencia a ataques conocidos)

Se apoyan en claves de alta entropía y estructuras internas mucho más robustas que 
un PRNG simple.

En implementaciones reales suelen usarse con autenticación (AEAD), por ejemplo 
ChaCha20-Poly1305 o AES-GCM, para proteger también integridad y autenticidad, no 
solo confidencialidad.

#### ¿Qué técnicas usan para evitar vulnerabilidades de PRNG básicos?

Nonce/IV único por mensaje: evita reutilización del keystream (así como la parte
2.2 y el ataque realizado). ChaCha20 define explícitamente nonce y un contador, 
CTR define contador/IV inicial para generar bloques distintos.

El contador garantiza que, dentro de un mismo mensaje, cada bloque use un valor 
diferente, evitando repetición interna del keystream.

#### ¿Cómo manejan inicialización y estado interno?

ChaCha20: estado interno incluye constantes, clave, contador y nonce; se actualiza 
por bloque incrementando el contador.

AES-CTR: el “estado” práctico es el contador y su incremento. Cada bloque cifra 
un contador distinto con AES para producir keystream independiente.

#### Conclusión comparativa

Mi implementación del laboratorio es útil para entender el concepto “keystream XOR mensaje”, 
pero en producción un PRNG simple no ofrece garantías criptográficas. ChaCha20 y AES-CTR 
bien implementados con nonces/IV únicos y, preferiblemente, con autenticación AEAD, evitan 
predictibilidad y reutilización del keystream mediante diseños y estándares robustos.

## Referencias

Nir, Y., & Langley, A. (2018). ChaCha20 and Poly1305 for IETF protocols (RFC 8439). Internet Engineering Task Force (IETF). https://datatracker.ietf.org/doc/rfc8439/

Dworkin, M. (2007). Recommendation for block cipher modes of operation: Methods and techniques. National Institute of Standards and Technology (NIST). https://doi.org/10.6028/NIST.SP.800-38A

VPN Unlimited. (2025, 20 de septiembre). ¿Qué es ChaCha20? Términos y definiciones de ciberseguridad. 
https://www.vpnunlimited.com/es/help/cybersecurity/chacha20

Nordic Semiconductor. (2025, 12 de agosto). Crypto: AES CTR - Documentación técnica. 
https://docs.nordicsemi.com/bundle/ncs-3.1.0/page/nrf/samples/crypto/aes_ctr/README.html

