#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <assert.h>

void sleep(seconds)
{
        for (int i =0 ;i < seconds* 1000; i ++)
        {
                continue;
        }
}
int main (int argc, char *argv[])
        {
        if (argc == 1) {
                fprintf( stderr, "Usage: cpu <string> \n" );
                fprintf( stderr, "Example: cpu \"University\" \n" );
                exit(1);
        }
        char *str = argv[1];
        printf(argv, "   here i am");
        int sleep_seconds = 2;
        while (1) {
                sleep( sleep_seconds );
                printf("%s\n", str);
        }
        return 0;
}