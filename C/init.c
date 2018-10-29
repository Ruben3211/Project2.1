#include <avr/io.h>
#include "init.h"
#define F_CPU 16E6
#include <util/delay.h>
#include  <avr/sfr_defs.h>
#define UBBRVAL 51;

void set_portC(){
	
	
}

void setPortB(){
	DDRB |= _BV(DDB0); // pin 0 van port b als output voor de groene led.
	DDRB |= _BV(DDB1); // pin 1 van port b als outpt voor de gele led.
	DDRB |= _BV(DDB2); // pin 2 van port b als output voor de rode led.
	
}

void setPortD(){
	
	
}

void setSerial(){
	// Set baudrate 19200
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	// disable U2X mode
	UCSR0A = 0;
	// enable transmitter
	UCSR0B = _BV(TXEN0) | _BV(RXEN0);
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}

