# EmojiCrypt_pip

EmojiCrypt_pip es un paquete de Python diseñado para ofrecer una forma única y divertida de cifrar y descifrar mensajes utilizando emojis. Este enfoque no solo hace que el proceso de cifrado sea más interesante, sino que también agrega una capa de abstracción al texto original, haciendo que el mensaje cifrado sea menos perceptible a primera vista.

## Instalación

Puedes instalar EmojiCrypt_pip directamente desde PyPI:

```bash
pip install EmojiCrypt_pip
```
Asegúrate de tener Python y pip ya instalados en tu sistema para poder ejecutar este comando sin problemas.

## Uso

EmojiCrypt_pip es extremadamente fácil de usar con solo dos funciones principales: encrypt para cifrar mensajes y decrypt para descifrar mensajes previamente cifrados con este paquete.

### Cifrar un mensaje
Para cifrar un mensaje, simplemente importa la función encrypt y pásale el mensaje que deseas cifrar como argumento.

```python
from EmojiCrypt_pip import encrypt

mensaje_cifrado = encrypt("Tu mensaje aquí")
print(mensaje_cifrado)
```
Esto convertirá tu mensaje en una cadena de emojis que representan el texto cifrado.


### Descifrar un mensaje
Para descifrar un mensaje que fue cifrado con EmojiCrypt_pip, utiliza la función decrypt de manera similar.

```python
from EmojiCrypt_pip import decrypt

mensaje_descifrado = decrypt(mensaje_cifrado)
print(mensaje_descifrado)
```

Asegúrate de reemplazar mensaje_cifrado con la cadena de emojis que recibiste al cifrar tu mensaje original. Esto te devolverá el texto original.

## Contribuir

Si estás interesado en contribuir a este proyecto, ¡tus aportes son bienvenidos! Puedes contribuir con mejoras en el código, sugerencias o reportando bugs. Para ello, por favor, abre un issue o una pull request en el repositorio de GitHub. https://github.com/Nichokas/EmojiCrypt_pip

## Licencia

Este proyecto está licenciado bajo GNU General Public License v3.0, lo que significa que puedes utilizarlo, modificarlo y distribuirlo bajo los términos de esa licencia.