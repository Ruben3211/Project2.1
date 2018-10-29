/*
 * project.c
 *
 * Created: 29-10-2018 09:09:30
 * Author :Ruben,Yaimon,Casper en Kevin
 */ 
#include <avr/io.h>
#define F_CPU 16E6

#include "AVR_TTC_scheduler.h"


// Zet gier alles wat geïnitialiseerd moet worden.
void setup(){
	
	SCH_Init_T1(); // Schedular initialiseren 
}

int main(void)
{
	setup(); // roep de setup functie aan
// Zet hier onder alle taken die van af de start al moeten draaien



	SCH_Start(); // Enable Schedular
	
	
    while (1) 
    {
		SCH_Dispatch_Tasks();
    }
}

