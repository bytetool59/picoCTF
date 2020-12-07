# Cesar 

Decrypt this message.

*Message:* picoCTF{dspttjohuifsvcjdpoabrkttds}


The Cesar Cyper basically shift the letters by some position.
So, to solve this challenge I made a [script](cesar_decode.py) that shifts the letters by a defined amount.

I brute-forced it and searched manually a human-readable combination.
The one that worked was *-1*, this means: **shift all letter position by one**

*Ex:*
- a -> z
- d -> c
- b -> a
And so forth.

## Flag
picoCTF{crossingtherubiconzaqjsscr}
