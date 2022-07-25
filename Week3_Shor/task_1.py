"""
For this task, messages are expressed as a list of integers. Each integer represents
a separate character in the original message string. The mapping between characters 
and `decoded` (plaintext) integers is:
 - 0-9: numbers 0-9
 - 10-35: letters a-z (only lowercase is used)
 - 36: space

Example: "abc def" would be converted to [10, 11, 12, 36, 13, 14, 15].

Below is an *encoded* message from your friend; you will need to decode it character
by character using your RSA private key, and then convert the resulting list of
integers back to a string using the correspondence above.
"""
message_from_friend = [
    292, 290, 218, 55, 127, 174, 171, 127, 112, 24,
    251, 248, 127, 132, 218, 213, 24, 251, 248, 174, 55,
    53, 127, 233, 24, 268, 24, 251, 248
]


def char_to_number(letter: str)->int:
    """
    Function that converts characters to numbers via the mapping:
    - Numbers 0-9: 0-9
    - Letters a-z: 10-35
    - Space: 36

    Using unicode ord() function, we get numeric representation 
    of the character and then map to the appropriate ranges.
    """
    letter_unicode = ord(letter)

    if ord("0") <= letter_unicode <= ord("9"):
        letter_decoded = (letter_unicode - ord("0"))
    
    elif ord("a") <= letter_unicode <= ord("z"):
        letter_decoded = (letter_unicode - ord("a")) + 10
    
    elif letter == " ":
        letter_decoded = 36
    
    return letter_decoded


def number_to_char(number: int)->str:
    """
    Function that converts characters to numbers via the mapping:
    - 0-9: numbers 0-9
    - 10-35: letters a-z (only lowercase is used)
    - 36: space

    Using unicode chr() function, we get numeric representation 
    of the character and then map to the appropriate ranges.
    """

    if 0 <= number <= 9:
        unicode = number + ord("0")
    
    elif 10 <= number <= 35:
        unicode = number + ord("a") - 10

    elif number == 36:
        unicode = ord(" ")

    return chr(unicode)



def decrypt(message, private_d, N):
    """Decrypt an encoded message. 
 
    Args:
        message (list[int]): A list of integers representing the secret message.
            Each integer in the list represents a different character in the message.
        private_d (int): Your (private) portion of the RSA key.
        N (int): The modulus of the RSA key.
 
    Returns:
        str: The decoded message.
    """
    # Implement RSA decoding cᵈ mod N
    decoded_message = [(c**private_d) % N for c in message]
    
    # Map from decoded characters to string
    decoded_letters = [number_to_char(char) for char in decoded_message]
    return "".join(decoded_letters)


def encrypt(message, public_e, N):
    """Encrypt a message 

    Args:
        message (str): A string representation of the message to send. It should
            contain only the characters a-z (lowercase), numbers 0-9, and spaces.
        public_e (int): The public portion of the RSA key (e, N) used for encoding.
        N (int): The modulus of the RSA key.
 
    Returns:
        list[int]: The message, encoded using the public key as a list of integers.
    """
    numeric_message = [char_to_number(letter) for letter in list(message)]
    
    # Implement RSA encoding c = mᵉ mod N
    encoded_message = [(m**public_e) % N for m in numeric_message]
    return encoded_message
