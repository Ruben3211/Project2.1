/*
 * project.c
 *
 * Created: 29-10-2018 09:09:30
 * Author :Ruben,Yaimon,Casper en Kevin
 */ 
#include <avr/io.h>
#define F_CPU 16E6
#include <util/delay.h>

#include "commando.c"
#include "AVR_TTC_scheduler.c"
#include "init.c"
#include "roluik.c"

// Zet hier alles wat geïnitialiseerd moet worden.
void setup(){	
	
	setPortB();
	setSerial();
	setRoluikStatus();
	
	SCH_Init_T1(); // Schedular initialiseren 
}

int main(void)
{
	setup(); // roep de setup functie aan
	
// Zet hier onder alle taken die van af de start al moeten draaien

	SCH_Add_Task(cont_commando, 0, 10);

	SCH_Start(); // Enable Schedular
	
	
    while (1) 
    {
		// zorg er voor dat hij de taken ook gaat dischpatchen 
		SCH_Dispatch_Tasks();
    }
}

