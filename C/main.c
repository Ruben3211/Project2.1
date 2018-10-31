/*
 * project.c
 *
 * Created: 29-10-2018 09:09:30
 * Author :Ruben,Yaimon,Casper en Kevin
 */ 
#include <avr/io.h>
#define F_CPU 16E6
#include <util/delay.h>
#include  <avr/sfr_defs.h>
#define UBBRVAL 51;
#include "AVR_TTC_scheduler.c"
uint8_t mode;
//Commando.c
uint8_t command;



void cont_commando(){
	command = ontvang();
	
	switch(command)
	{
		// open het luik
		case '1':
		open_rolluik();
		return;
		// sluit luik
		case '2':
		sluit_rolluik();
		return;
	}
}

// sensor.c
float analoge_waarde;

// Deze switch case is er om voor de juiste sensor te kiezen
// zo kan je op alle embedded systems het zelfde zetten zonder iets aan te passen

float sensor_lees(int sensor){
	
	switch(sensor)
	{
		
		case 0: // tempratuur sensor
		ADMUX &= ~_BV(MUX0); // Set channel point to port 0
		ADCSRA |= _BV(ADSC); // Start adc measurement
		loop_until_bit_is_clear(ADCSRA, ADSC); // proceed when done

		analoge_waarde = (((float)ADCW * 5000 / 1024) - 500) / 10;
		return analoge_waarde;
		break;	
		
		case 1: // lichtsensor
		ADMUX |= _BV(MUX0);
		ADCSRA |= _BV(ADSC);
		loop_until_bit_is_clear(ADCSRA, ADSC);
		
		// Return lightvalue between 0 - 100
		analoge_waarde = (float)ADCW / 1024 * 100;
		return analoge_waarde;
		break;
		
		// afstand sensor
		case 2:
			PORTD |= _BV(PD3);
			_delay_us(10);
			PORTD &= ~_BV(PD3);

			loop_until_bit_is_set(PIND, PD4);
			TCNT1 = 0;
			//PORTB |= _BV(PB3);
			loop_until_bit_is_clear(PIND, PD4);
			//PORTB &= ~_BV(PB3);
			uint16_t count = TCNT1;
			//transmit(count);
			float distance = ((float)count / 4);

			return distance;
			break;
	}
}


// serial.c
void stuur(uint8_t data){
	loop_until_bit_is_set(UCSR0A, UDRE0);
	UDR0 = data;
	
}

void ontvang(){
	loop_until_bit_is_set(UCSR0A, RXC0);
	return UDR0;
}

// rolluik.c
//int count = 0;
int status_roluik;
int roluik_bezig;

void setRoluikStatus(){
	roluik_bezig = 0; // als de roluik niet bezig is moet deze nul zijn anders 1
	status_roluik = 0; // nul is niet bezig
	PORTB |= _BV(PB0); // zet de groene led aan.
}

// open rolluik
void open_rolluik(){
	if(status_roluik == 1 & roluik_bezig == 0){
		//count = 0;
		roluik_bezig = 1;
		PORTB &= ~_BV(PB2); // zet de rode led uit
	//	while(count < 3)
		while(sensor_lees(2) < 20)
	{
			PORTB |= _BV(PB1);
			_delay_ms(500);
			PORTB &= ~_BV(PB1);
			_delay_ms(500);
			//count++;
		}
		PORTB |= _BV(PB0); // zet de groene led aan
		roluik_bezig = 0;
		status_roluik = 0;
	}
	else if(status_roluik == 1){
		// rol luik is al omhoog
	}
	else if(roluik_bezig == 1) {
		// hier moet nog iets komen als het roluik al bezig is
	}
	
}

// sluit rolluik
void sluit_rolluik(){
	if(status_roluik == 0 & roluik_bezig == 0){
		//count = 0;
		roluik_bezig = 1;
		PORTB &= ~_BV(PB0); // zet de groen led uit
		//while(count < 3)
		while(sensor_lees(2) > 20)
		{
			PORTB |= _BV(PB1);
			_delay_ms(500);
			PORTB &= ~_BV(PB1);
			_delay_ms(500);
			
			//count++;
		}
		PORTB |= _BV(PB2); // zet de groene rode aan
		roluik_bezig = 0;
		status_roluik = 1;
	}
	else if(status_roluik == 1){
		// rol luik is al omhoog
	}
	else if(roluik_bezig == 1) {
		// hier moet nog iets komen als het roluik al bezig is
	}
	
}



// init.c
void set_portC(){
	
	ADCSRA |= _BV(ADPS2) | _BV(ADPS1) | _BV(ADPS0); // 128 prescaler
	ADMUX |= _BV(REFS0);
	ADMUX &= ~_BV(REFS1); // 5v mode
	ADCSRA |= _BV(ADEN); // Turn on
	
}

void set_PortB(){
	DDRB |= _BV(DDB0); // pin 0 van port b als output voor de groene led.
	DDRB |= _BV(DDB1); // pin 1 van port b als outpt voor de gele led.
	DDRB |= _BV(DDB2); // pin 2 van port b als output voor de rode led.
	
}

void set_PortD(){
	
	DDRD |= _BV(PD3); // Pin 3 Trigger Output
	DDRD &= ~_BV(PD4); // Pin 4 Echo Input
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

void lamp()
{
	if(sensor_lees(1) < 30)
	{
		sluit_rolluik();
	} else if(sensor_lees(1) > 29){
		open_rolluik();
	}
}


// Zet hier alles wat geïnitialiseerd moet worden.
void setup(){	
	
	set_PortB();
	set_portC();
	set_PortD();
	setSerial();
	setRoluikStatus();
	
	SCH_Init_T1(); // Schedular initialiseren 
}

int main(void)
{
	setup(); // roep de setup functie aan
	
// Zet hier onder alle taken die van af de start al moeten draaien

	SCH_Add_Task(lamp,0,10);
	//SCH_Add_Task(cont_commando, 0, 10); // maak een task aan voor het wachten op een commando
	SCH_Start(); // Enable Schedular
	
    while (1) 
    {
	
		// zorg er voor dat hij de taken ook gaat dischpatchen 
		SCH_Dispatch_Tasks();
    }
}

