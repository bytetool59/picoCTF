# So Meta

## Description
Find the flag in this picture.

## Solution
Just by looking at the name of the challenge, we can infer that it is about metadata.

Metadata is a form of storing information about the file in within the file, that's why is *meta*.

1. Download the file
2. Get the metadata
In Linux we have a command to check image metadata called *identify*. You invoke it and pass a image file as parameter.

Let's try it!
> identify pico_img.png -verbose

Nothing interesting yet...

3. Extract the strings
One thing about metadata is that they are stored as plain text in the files.

> strings pico_img.png | less

4. Filter just the flag
The previous command returned a lot of information. We just want the flag. No problem, let's use the *grep* command to solve that.

> strings pico_img.png | grep picoCTF

There you have it!

## Flag
picoCTF{s0_m3ta_fec06741}
