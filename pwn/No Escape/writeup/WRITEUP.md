### Discovery

* We are given a docker image.
* If we run this image we don't get any output and our terminal becomes blocked.
* Trying to escape the program with `CTRL + C` prints output: `Higher!`
* Knowing that `CTRL + C` simply sends a signal to the program we can assume that the program suggests we send a signal with higher number.

### Exploitation

* To send the signal we need to know PID of the process.
* Checking inside the image or container we can find that process name is `a.out`
* `ps -aux | grep -w "a\.out"` will give us PID of this process.
* We can try sending different signal numbers with `kill -<number> <PID>`
* Trying different numbers we find that sending `kill -21 <PID>` gives us the flag.