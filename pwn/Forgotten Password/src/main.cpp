#include "obfuscate.h"
#include <iostream>
#include <signal.h>
#include <cstring>
#define FLAG AY_OBFUSCATE("flag{Ch4n9E2_k0mE_7iMe_m0ve2_0N}")
#define INVALID_PASSWORD AY_OBFUSCATE("Invalid password!")
#define INVALID_ARGUMENTS AY_OBFUSCATE("Invalid arguments!")
#define CORRECT_PASSWORD AY_OBFUSCATE("Correct password! Here is your flag:")
#define PASSWORD AY_OBFUSCATE("vfrJdU9v8NLPYagGHCbWu62U334cWK2FaGSBPXQhZaBF3JRkZcCV5C2BRZn3XSfA")

void busy_loop(uint64_t iters) {
    volatile int sink;
    do {
        sink = 0;
    } while (--iters > 0);
    (void)sink;
}

int main(int argc, char **argv)
{
    if (argc != 2){
        std::cout << INVALID_ARGUMENTS << std::endl;
        return 1;
    }
    std::string str = argv[1];
    if (str.length() != strlen(PASSWORD)){
        std::cout << INVALID_PASSWORD << std::endl;
        return 1;
    }
    for (int i = 0; i < str.length(); i++){
        if (str[i] != PASSWORD[i]) {
            std::cout << INVALID_PASSWORD << std::endl;
            return 1;
        }
        busy_loop(10000000);
    }
    std::cout << CORRECT_PASSWORD << std::endl << FLAG << std::endl;
    return 0;
}