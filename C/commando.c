#include <avr/io.h>

#include "main.h"
#include "roluik.h"
#include "AVR_TTC_scheduler.h"

#define F_CPU 16E6
#include <util/delay.h>

uint8_t command;



void cont_commando(){
	command = ontvang();
	
	switch(command)
	{
		// open het luik
		case 0x01:
		open_roluik();

		// sluit luik
		case 0x02:
		sluit_roluik();
		
	}
}