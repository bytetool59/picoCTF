# vault-door-1

## Description
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](VaultDoor1.java).

## Resolution
Analysing the code, the first thing that stands out is the password. 
In this chanllenge, it is stored in an String and the characteres of if are checked randomly.
For those of you who are not familiar with Java, let me explain.

**How it worked?**
In some languages, a string is basically an array of char (eg. Pascal).
Within the code, what they're doing is checking each char of the password randomly, one per line. This way, it is more difficult to find out the password in comparison to plain text.

**Example**
```c
Char[3] password; # A password string with 3 chars

password[3] = 9;  # Assign each position with a char
password[1] = 0;
password[2] = 5;
```

You see? In a complex string you couln't figure out the password just by looking at it. If you arrange them in order, it became pretty easy.

```c
password[1] = 0;
password[2] = 5;
password[3] = 9;
```

The principle there is the same, the only caviat to the story is that they don't store the password in a variable, instead, they check for each char indidually and return them if corrent.
As you might have noticed, the printed flag (shown if the password is correct) is the user input itself.

**How to solve it?**
I'm sure there are a lot of methods to do this, but what I did is to assign instead of check each char and return them in the end.

The thing is, you can't do that so easily in Java. The type string does not support the array notation (string[pos]) as it is.

The solution was to declare them as *char[]* and make the assignments as follows:

```java

    public static String checkPassword() {
        String thePassword;
        char[] password = thePassword.toCharArray();


        password[0]  = 'd';
        password[29] = '3';
        password[4]  = 'r';
        password[2]  = '5';
        password[23] = 'r';
        password[3]  = 'c';
        password[17] = '4';
        password[1]  = '3';
        password[7]  = 'b';
        password[10] = '_';
        password[5]  = '4';
        password[9]  = '3';
        password[11] = 't';
        password[15] = 'c';
        password[8]  = 'l';
        password[12] = 'H';
        password[20] = 'c';
        password[14] = '_';
        password[6]  = 'm';
        password[24] = '5';
        password[18] = 'r';
        password[13] = '3';
        password[19] = '4';
        password[21] = 'T';
        password[16] = 'H';
        password[27] = 'f';
        password[30] = 'b';
        password[25] = '_';
        password[22] = '3';
        password[28] = '6';
        password[26] = 'f';
        password[31] = '0';

        return String.valueOf(password); 
    }
```
And that's it! You can replace the function above and print the return of this function in a *System.out.print()* and you're good to go.

## Flag
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}
