#include "obfuscate.h"
#include <iostream>
#include <signal.h>
#define FLAG AY_OBFUSCATE("flag{1_lo5T_CtRL_Of_mY_l1f3}")
#define CONGRATULATIONS AY_OBFUSCATE("Congratulations! Here is your flag: ")
#define HIGHER AY_OBFUSCATE("Higher!")
#define LOWER AY_OBFUSCATE("Lower!")

void signalHandler(int signalNumber)
{
    if (signalNumber == 21) {
        std::cout << CONGRATULATIONS << FLAG << std::endl;
    } else if (signalNumber < 21){
        std::cout << HIGHER << std::endl;
    } else {
        std::cout << LOWER << std::endl;
    }
}

int main()
{
    for (int i = 0; i < 32; i++){
        signal(i, signalHandler);
    }
    while(1);
    return 0;
}