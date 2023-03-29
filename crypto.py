'''
This module contains functions to encrypt or decrypt a message based on the given key
'''
from functools import *
# Create a target list of str in ascending order based on the values from ord() between 32 and 126
target_characters = list(map(lambda i: chr(i), range(32,127)))

def ch_to_num(char):
    '''
    Take a character and return the corresponding non-negatvie integer value based on a specific encoding method 

    Parameters
    ----------
    char : str
        a character from the target set of characters

    Returns
    -------
    int
        the corresponding non-negative integer value based on the encoding method

    '''
    return target_characters.index(char)

def num_to_ch(num):
    '''
    Take a non-negative integer and return the corresponding character based on a specific encoding method

    Parameters
    ----------
    num : int
        an non-negative integer in the range [0,94]

    Returns
    -------
    str
        the corresponding character based on the encoding method

    '''
    return target_characters[num%95]
   
        
def encode(message,key):
    '''
    Encrypt a given message into the ciphertext using the key

    Parameters
    ----------
    message : str
        the plain text to be encoded
    key: str
        the key used to encrypt the message

    Returns
    -------
    cipher_text : str
        the cipher text encoded based on the given key
    '''
    key_1 = key * (len(message)//len(key)) + key[:(len(message) % len(key))] # make the length of the key match the length of the message
    def _encode(message,key):
        resulting_num = ch_to_num(key) + ch_to_num(message)
        return num_to_ch(resulting_num)
    return reduce(lambda a,b: a+b, map(_encode,message,key_1))

def decode(message,key):
    '''
    Decrypt a given ciphertext using the key.

    Parameters
    ----------
    message : str
        the cipher text to be decoded
    key: str
        the key used to decrypt the message

    Returns
    -------
    plain_text : str
        the plain text decoded based on the given key

    '''
    key_1 = key * (len(message)//len(key)) + key[:(len(message) % len(key))]
    def _decode(message,key):
        resulting_num = ch_to_num(message) - ch_to_num(key)
        return num_to_ch(resulting_num)
    return reduce(lambda a,b: a+b, map(_decode,message,key_1))