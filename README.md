# WoC2k19
My Winter of Code 2019 Project

This projects devotes itself to decrypting various text encryptions algorithms, specifically the likes of Rivest-Shamir-Aldeman(RSA encryption algorithm) and ciphers, mainly the Vigenere and Caeser ciphers and many others.(p.s. encryptions can also be done... since knowledge flows both ways)

Description: command-line-tool:: cryptologer.exe


usage: cryptologer.py [-h] [--decrypt] [--encrypt] [--sourcefile SOURCEFILE]
                      [--cipher CIPHER] [--key KEY] [--caeser] [--vignere]
                      [--affine] [--bacon] [--polybius] [--railfence] [--atbash]
                      [--substitution] [--rsa] [--weiner] [--smalle] [--internal]
                      [--fermat] [--twin] [--chinese]

Decryptor for Caeser, Vigenere, types of RSA and more...

optional arguments:
  -h, --help            show this help message and exit
  --decrypt, --dec, -d  Performs Decryption
  --encrypt, --enc, -e  Performs Encryption
  --sourcefile SOURCEFILE, --sf SOURCEFILE, -f SOURCEFILE
                        Input file with ciphertext
  --cipher CIPHER, --cip CIPHER, -c CIPHER
                        Input cipher as test
  --key KEY, -k KEY     If the key is known (text for vignere, shift for caeser)
  --caeser, -C          If the cipher is caeser cipher
  --vignere, -V         If the cipher is vignere cipher
  --affine, -A          If the cipher is affine cipher
  --bacon, -B           If the cipher is bacon cipher
  --polybius, -P        If the cipher is encrypted by a simple 6x6 polybius square
  --railfence, -F       If railfence encryption is used
  --atbash, -T          If atbash rotation is done on the plaintext
  --substitution, -S    If the plaintext in encrypted using simple substitution
                        cipher
  --rsa, -R             If the cipher is RSA related
  --weiner, -W          Cracking RSA using Weiner attack
  --smalle, -E          Cracking RSA provided e is very small
  --internal, -I        If an internal attack for RSA is being performed
  --fermat, -M          Fermat's attack on the RSA encrypted text
  --twin, -N            If the RSA public is a product of twin prime, use this
  --chinese, -H         Using the Chinese Remainder Theorem for cracking RSA from e
                        packets having the same n

Compulsary Arguments for correct usage:: 
[-e/d] for specifing encryption or decryption... no default value

[-C/V/A/B/P/F/S/R/W/E/I] any one of these for specifying the kind of cipher/rsa attack... no default value

[-f/-c] for specifying the file containing the text or typing the text manually (not applicable for rsa)

[-k] for manually typing the key in case of Caeser/Vigenere... (optional)

[-l] for specifying max probable key length in case of vigenere cipher... (default value=10)


Format of text in file specified:: For ciphers texts must be as it to be encrypted

For RSA, the file must be the format;;
"""
n:<modulus>
e:<public_key>
c/m:<cipher_text>/<message>
"""
It should be the keyword followed by its respective value. During encrypting it reads 'm' instead of the general 'c'
  