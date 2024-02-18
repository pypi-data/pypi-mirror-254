from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='EmojiCrypt_pip',                                      # Nombre del paquete
    packages=['EmojiCrypt_pip'],                                # Folder del paquete
    version='1',                                              # Version de la libreria
    license='GNU v3',                                           # Licencia
    description='encrypt text in emojis',                       # Breve descripcion de la libreria
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Nichokas',
    author_email='nicolas.rodalv@educa.jcyl.es',
    url='https://github.com/Nichokas',                          # Url del sitio web o de Github
    download_url='https://github.com/Nichokas/EmojiCrypt_pip',  # Link del repositorio de la libreria
    keywords=[],                                                # Keywords para definir el paquete/libreria
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',          # Estados del paquete "3 - Alpha", "4 - Beta", "5 - Production/Stable"
        'Intended Audience :: Developers',                      # Definir cual es el publico al que va dirigido el paquete
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',            # Licencia
        'Programming Language :: Python :: 3',                  # Especificar las versiones de python que soportan el paquete
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
