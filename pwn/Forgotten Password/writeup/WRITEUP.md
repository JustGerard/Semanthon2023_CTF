### Discovery

* We are given a docker image and information that it expects a password.
* Description also mentions that the password is case-sensitive and contains only letters and numbers.
* If we run this image we output `Invalid arguments!`
* Adding some argument will give us `Invalid password!`.
* Playing around with arguments gets us nowhere.
* We copy executable from the container and decompile it with for example `Ida Free`.
* We can't find the flag as a plaintext in the decompiled code.
* In the beginning of the code there is a call to `_strlen` and comparison with `std::length`, which suggests that length of the password is compared with length of input.
* Later in the code we can see that there is a loop, and inside this loop there is a function called `busy_loop(ulong)` that's executed after `if` statement.
* This all suggests that this code has `timing atttack` vulnerability.

### Exploitation
* First we write a script that will check for the correct length of the password by analyzing execution time for different input lengths.
* After some testing we find out that correct length is `64`.
* Now it's simply a matter of writing a script for timing attack with knowledge that:
    * Length of password is `64`
    * It only contains letters and numbers
    * It's case-sensitive
    * Execution time will be longer with each correct letter found.
