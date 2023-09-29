#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 *infinite_while - an infinite while loop
 *Return: nothing
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 *main - entry point
 *Return: nothing
 */
int main(void)
{
	pid_t f;
	int i;

	for (i = 0; i < 5; i++)
	{
		f = fork();

		if (f > 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
		}

		else
			exit(0);
	}

	infinite_while();
	return (0);
}
