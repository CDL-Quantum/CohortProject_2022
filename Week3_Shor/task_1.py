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
        
    # Decode each integer into its alphabetical integer
    integer_decoded_message = []
    for item in message:
        integer_decoded_message.append(item ** private_d % N)

    
    # Translate into words
    int_to_string = {string.printable[i]: i for i in range(0,36)}
    int_to_string[" "] = 36
    
    decoded_message = ""
    for item in integer_decoded_message:
        decoded_message += int_to_string[item]

    return decoded_message


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
  
  
    # Set dictionary for translation to integers
    string_to_int = {string.printable[i] : i for i in range(0, 36)}
    string_to_int[' '] = 36
    
    # Encode the message
    encoded_message = []
    for item in message:
        encoded_message.append(string_to_int[item] ** public_e % N)

    return encoded_message

   (d,e,N) = (169, 25, 299)
   decoded_message = decrypt(message_from_friend, d, N)
   print(decoded_message)
   
   answer = "I love all colors"
   encoded_message = encrypt(answer, e, N)
   print(encoded_message)
   
