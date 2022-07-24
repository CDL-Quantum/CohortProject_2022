![CDL 2022 Cohort Project](../CDL_logo.jpg)
## Project 3: Shor's algorithm

This project will guide you through an exploration of the gate-model implmentation of Shor's algorithm and its scaling.

Open [INSTRUCTIONS.md](./INSTRUCTIONS.md) to begin learning about your project for this week!


**Please edit this markdown file directly with links to your completed tasks and challenges.**

## Tasks include:
* Encrypt and decrypt a message using RSA
* Research and implement the quantum algorithm for order finding
* Use Shor's algorithm to factor increasingly large sequences
* Discuss a new quantum-safe protocol as part of your Business Application

### Task 1: Privacy is key

``` python

message_from_friend = [
    292, 290, 218, 55, 127, 174, 171, 127, 112, 24,
    251, 248, 127, 132, 218, 213, 24, 251, 248, 174, 55,
    53, 127, 233, 24, 268, 24, 251, 248
]

lett = "0123456789abcdefghijklmnopqrstuvwxyz "

decode = {ii:lett[ii] for ii in range(37)}

encode = {lett[ii]:ii for ii in range(37)}

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
    decoded_message = ""

    # YOUR CODE HERE
    for c in message:
        decoded_message += decode[c ** private_d % N]

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
    encoded_message = []

    # YOUR CODE HERE
    for lett in message:
        encoded_message.append(encode[lett]**public_e % N)

    return encoded_message

print(decrypt(message_from_friend, 169, 299))

```
The result of the above code is: `what is your favourite colour`

## Task 2: Everything is in order



After you have completed your tasks, consider the optional Challenges below!

## Further Challenges:
* Try running your implementation of Shor's algorithm on any available quantum hardware
* Explore variational quantum factoring
* Attempt factoring using quantum annealers

## Business Application
For each week, your team is asked to complete a Business Application. Questions you will be asked are:

* Explain to a layperson the technical problem you solved in this exercise.
* Explain or provide examples of the types of real-world problems this method can solve.
* Identify at least one potential customer for this solution - i.e. a business who has this problem and would consider paying to have this problem solved.
* Prepare a 90 second video explaining the value proposition of your innovation to this potential customer in non-technical language.

For more details refer to the [Business Application found here](./Business_Application.md)
