# shark on wire 1

## Description
We found this packet capture. Recover the flag.

## How to
First, download the .pcap file and open it with wireshark. If you don't have it, no problem. It's a free program. Download install done.

After that, you can open the pacap file.

Now it's just a matter of clicking the entries with the right mouse button and 'Follow TCP Stream'. 

This command follows the next 'packets' of data until it reads the whole menssage.

1. Find one that says 
   *picoCTF{N0t_a_fLag}*

2. Right click it and filter all connections from this IP adress
3. Test around and you will find the key.

## Flag
picoCTF{StaT31355_636f6e6e}

