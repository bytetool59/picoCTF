# Easy1

## Description
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help **UFJKXQZQUNB** with the key of **SOLVECRYPTO**. Can you use this table to solve it?.

## Solution
As the name implies this is a lookup table. This means we need to find a corresponding combination to get to the key.

The table provided matches to the [Vigenère Cipher](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html). Let me show you how it works:

1. The table has all the letters in the English Alphabet in both axis (x and y)
2. You need a *key* and a *message* to be encripted.
3. Both of them need to be the same size.
> Wait, what? How can I transmit the key for a really long message? It is unpractical! Don't worry, we'll see that in a bit.
3. The encripted message is the intersection of the two corresponding columns. At the Y pos you use the encripted key and a the X the message you want to encript.

### Let's go pratical
**Message:** UFJKXQZQUNB (X axis)
**Key:**     SOLVECRYPTO (Y axis)

> Remember when I said they needed to have equal lengths? That's where it will come handy.

### Step by step
To decript the next, you need to have the encripted message and the key.
Let's take the letter *U* from the enc_message, for example.
1. The corresponding letter in the key (put them one bellow the other; repeat if it is shorter than the message) is S.
2. Find the letter un in the line S
3. The column you are in is the decripted letter, in our case, *C*. Easy right?

Let's do this process letter by letter.

UFJKXQZQUNB -> encripted message
SOLVECRYPTO -> key
CRYPTOISFUN -> decripted message

## Flag
picoCTF{CRYPTOISFUN}

