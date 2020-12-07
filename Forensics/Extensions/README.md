# Extensions

## Description
This is a really weird text file TXT? Can you find the flag?


## Solution

1. First, let's try to open the file
> xxd flag.txt | less
```hex
00000000:  .PNG........IHDR
00000010:  .......`.......^
00000020:  .....sRGB.......
00000030:  ..gAMA......a...
```
In most of files, the first bytes are telling information abou the file. In our case, it is a PNG file, an image.

2. Let's rename it and see what does it have
> cp flag.txt flag.png

3. Opening up the file it reveals the flag itself.

## Flag
picoCTF{now_you_know_about_extensions}
