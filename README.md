# D3crypt0r

This projects devotes itself to decrypting various text encryptions algorithms, specifically the likes of Rivest-Shamir-Aldeman(RSA encryption algorithm) and ciphers, mainly the Vigenere and Caeser ciphers and many others.(p.s. encryptions can also be done... since knowledge flows both ways)

#### Application

Command-Line-Tool:: **cryptologer.py**

#### Environment

Python 3.5+

## Installation

There are setup files available for installing the project in the **/SETUP** folder. viz., for both latest *Windows* and *Linux* operating systems.

*Linux Install:* download *crypt_linux*, it's a zip file. Unzip and run python script *alias* first then use `cryptologer` in the bash.

*Windows Install:* download *mystic_win* and go through the installation process. Open the registry key *crypt*, restart terminal and use `cryptologer`.
The required files are auto-saved to  **C:\Program Files (x86)\D3crytMe!**

## Bashing Options
``` bash
cryptoloher -h

cryptologer.py [-h] [--decrypt] [--encrypt] [--sourcefile SOURCEFILE] [--cipher CIPHER] [--key KEY] [--caeser] [--vignere] [--affine] [--bacon] [--polybius] [--railfence] [--atbash] [--substitution] [--rsa] [--weiner] [--smalle] [--internal] [--fermat] [--twin] [--chinese]

Decryptor for Caeser, Vigenere, types of RSA and more...

Optional Arguments
-h, --help            show this help message and exit
--decrypt, --dec, -d  Performs Decryption
--encrypt, --enc, -e  Performs Encryption
--sourcefile SOURCEFILE, --sf SOURCEFILE, -f SOURCEFILE
                      Input file with ciphertext
--cipher CIPHER, --cip CIPHER, -c CIPHER
                      Input cipher as text

--key KEY, -k KEY     If the key is known (text for vignere, shift for caeser)
--caeser, -C          If the cipher is caeser cipher
--vignere, -V         If the cipher is vignere cipher
--affine, -A          If the cipher is affine cipher
--bacon, -B           If the cipher is bacon cipher
--polybius, -P        If the cipher is encrypted by a simple 6x6 polybius square
--railfence, -F       If railfence encryption is used
--atbash, -T          If atbash rotation is done on the plaintext
--substitution, -S    If the plaintext in encrypted using simple substitution cipher

--rsa, -R             If the cipher is RSA related
--weiner, -W          Cracking RSA using Weiner attack
--smalle, -E          Cracking RSA provided e is very small
--internal, -I        If an internal attack for RSA is being performed
--fermat, -M          Fermat\'s attack on the RSA encrypted text
--twin, -N            If the RSA public is a product of twin primes, use this
--chinese, -H         Using the Chinese Remainder Theorem for cracking RSA from e packets having the same n
```                      

## Arguments & Usage:: 
`-e` `-d` for specifing encryption or decryption:: **no default value**

`-C` `-V` `-A` `-B` `-P` `-F` `-S` `-R` `-W` `-E` `-I` any one of these for specifying the kind of cipher/rsa attack:: **no default value**

`-f` for specifying the file containing the data 

`c` for providing the cipher manually:: **not applicable for rsa**

`-k` for manually typing the key in case of Caeser/Vigenere:: **optional**

`-l` for specifying max probable key length in case of vigenere cipher:: **default value=10**


### File Format & Content 

**Ciphers**:: raw data in text files

**RSA**:: text files require specifying modulus *n*, public key _e_ and ciphertext _c_ in seperate lines

![Input_Example](https://github.com/Masrt200/WoC2k19/blob/master/Snips/file.PNG)

The keyword should be followed by its respective value. While encrypting using RSA, use *m* instead of the general *c*.

## Examples

***Caeser Cipher Bruteforce***

![caeser](https://github.com/Masrt200/WoC2k19/blob/master/Snips/Caeser.jpg)

***Vignere without key***

*Encrypting*

![Vig_ENC](https://github.com/Masrt200/WoC2k19/blob/master/Snips/Vig_enc.PNG)

*Decrypting*

![Vig_DEC](https://github.com/Masrt200/WoC2k19/blob/master/Snips/Vig_dec.PNG)

***Simple RSA***

![Rivert](https://github.com/Masrt200/WoC2k19/blob/master/Snips/simple_rsa.PNG)

***RSA: Small-E Attack***

![Shamir](https://github.com/Masrt200/WoC2k19/blob/master/Snips/small_e.PNG)

***RSA: Weiner Attack***

![Aldeman](https://github.com/Masrt200/WoC2k19/blob/master/Snips/Weiner_long.PNG)





  
