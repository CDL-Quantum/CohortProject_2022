"""
For this task, messages are expressed as a list of integers. Each integer represents
a separate character in the original message string. The mapping between characters 
and `decoded` (plaintext) integers is:
 - 0-9: numbers 0-9
 - 10-35: letters a-z (only lowercase is used)
 - 36: space

Example: "abc def" would be converted to [10, 11, 12, 36, 13, 14, 15].

List of the symbols to follows the previous format
"""
 
decoded_format = [str(i) for i in range(10)]+[chr(i)  for i in range(97,123) ]+[" "]



"""
Below is an *encoded* message from your friend; you will need to decode it character
by character using your RSA private key, and then convert the resulting list of
integers back to a string using the correspondence above.
"""
message_from_friend = [
    292, 290, 218, 55, 127, 174, 171, 127, 112, 24,
    251, 248, 127, 132, 218, 213, 24, 251, 248, 174, 55,
    53, 127, 233, 24, 268, 24, 251, 248
]
    

def phi_n(N):
    
    """Search phi_n to obtain p, q values to find the decode key
 
    Args:
        N (int): A integer value that is  the  base for encode and decode the message
 
    Returns:
        int: phi of n.
    """
    
    # save  two primes numbers p,q that are the coprime to find  N
    prime = []
    
    
    # Prime Factorization from to  N
    for i in range(2,N + 1):
        
        # if is the same value
        if N % i == 0:
            count = 1
            #check is not prime number the first half of i
            for j in range(2,(i//2 + 1)):
                if(i % j == 0):
                    count = 0
                    break
            # if is prime
            if(count == 1):
                prime.append(i)

    return (prime[0]-1)*(prime[1]-1)


def find_private_d(public_e, N):
			 
    """    calculates the modular inverse from public_e and phi
        Args:
        public_e (int): An integer value about the key public or e
        N (int): The N value for the base in the  RSA algoritmh find phi
 
    Returns:
        private_d: An integer value about the key private or d
    """
    phi = phi_n(N)
    
    #init variables
    phi_0 = phi
    
    aux_1 = 0
    private_d = 1
    
    
    # validate in case that phi is equals to 1  that return 0
    if (phi == 1) : 
        return 0
    
    # obtain the private_d value usign the inverse from public_e and phi
    while (public_e > 1) : 

        aux_2 = public_e // phi
        aux_3 = phi 
        
        phi = public_e % phi 
        public_e = aux_3 
        
        aux_3 = aux_1 

        aux_1 = private_d - aux_2 * aux_1 
        private_d = aux_3 
        
    # Make the private_d in a positive value 
    if (private_d < 0) : 
        private_d = private_d + phi_0 
  
    return private_d 



## second method for task 2 
def find_private_d_task2(public_e, N, p, q):
			 
    """    calculates the modular inverse from public_e and phi
        Args:
        public_e (int): An integer value about the key public or e
        N (int): The N value for the base in the  RSA algoritmh find phi
 
    Returns:
        private_d: An integer value about the key private or d
    """
    phi = (p-1)*(q-1)
    
    #init variables
    phi_0 = phi
    
    aux_1 = 0
    private_d = 1
    
    
    # validate in case that phi is equals to 1  that return 0
    if (phi == 1) : 
        return 0
    
    # obtain the private_d value usign the inverse from public_e and phi
    while (public_e > 1) : 

        aux_2 = public_e // phi
        aux_3 = phi 
        
        phi = public_e % phi 
        public_e = aux_3 
        
        aux_3 = aux_1 

        aux_1 = private_d - aux_2 * aux_1 
        private_d = aux_3 
        
    # Make the private_d in a positive value 
    if (private_d < 0) : 
        private_d = private_d + phi_0 
  
    return private_d 


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
    
    # YOUR CODE HERE    
    return ''.join([decoded_format[pow(char,private_d,N)] for char in message])



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
    
    # YOUR CODE HERE    
    return [pow(decoded_format.index(char),public_e,N) for char in  message]
