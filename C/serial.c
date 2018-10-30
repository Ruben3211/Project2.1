#include <avr/io.h>
#include "serial.h"
#include  <avr/sfr_defs.h>

void stuur(uint8_t data){
	loop_until_bit_is_set(UCSR0A, UDRE0);
	UDR0 = data;
	
}

void ontvang(){
	loop_until_bit_is_set(UCSR0A, RXC0);
	return UDR0
}