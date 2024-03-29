/*
 * project.c
 *
 * Created: 29-10-2018 09:09:30
 * Author :Ruben,Yaimon,Casper en Kevin
 */ 
#include <avr/io.h>
#include <util/delay.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#define F_CPU 16E6
#define FOSC 16000000 // Clock Speed
#define BAUD 9600
#define MYUBRR FOSC/16/BAUD-1
#include "AVR_TTC_scheduler.c"
int modes = 0;
double waarde = 0;
uint8_t sensor_type = 0;
uint8_t meet_freq;
uint8_t grens_waarde;
uint8_t deel_freq;
char buffer[5];
int command;
//int count = 0;
int status_roluik;
int roluik_bezig;

//settings
void verander_mode(){
	if (modes == 0){
		modes = '1';
	}
	else if(modes == 1){
		modes = '0';
	}
}

void cont_commando(){
	if(USART_Receive() != 0xFF){
		return;
	}
	command = USART_Receive();
	switch(command)
	{
		// Open het luik
		case 0x01:
		open_rolluik();
		return;
		// Sluit luik
		case 0x02:
		sluit_rolluik();
		return;
		// Verander de mode van automatisch naar handmatig en andersom
		case 0x03:
		verander_mode();
		return;
		// Ontvangt het sensor type
		case 0x04:
		sensor_type = USART_Receive();
		return;
		// Ontvangt de meet frequentie
		case 0x05:
		meet_freq = USART_Receive();
		return;
		// Ontvangt de grens waarde
		case 0x06:
		grens_waarde = USART_Receive();
		return;
		// Ontvangt de deel freq
		case 0x07:
		deel_freq = USART_Receive();
		return;
		case 0x08:
		itoa(waarde, buffer, 10);
		USART_sendstring(buffer);
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

		analoge_waarde = (((((double)ADCW /1024) * 5) - 0.5 )* 100);
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
void USART_Transmit( unsigned int data )
{
	/* Wait for empty transmit buffer */
	while ( !( UCSR0A & (1<<UDRE0)) )
	;
	/* Put data into buffer, sends the data */
	UDR0 = data;
}

void USART_sendstring(char* stringptr){
	while(*stringptr != 0x00){
		USART_Transmit(*stringptr);
		stringptr++;
	}
}

int USART_Receive()
{
	/* Wait for data to be received */
	while ( !(UCSR0A & (1<<RXC0)) );
	/* Get and return received data from buffer */
	return UDR0;
}

// rolluik.c
//int count = 0;

void setRoluikStatus(){
	roluik_bezig = 0; // als de roluik niet bezig is moet deze nul zijn anders 1
	status_roluik = 1; // nul is niet bezig
	PORTB |= _BV(PB2); // zet de groene led aan.
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
			_delay_ms(5000);
			PORTB &= ~_BV(PB1);
			_delay_ms(5000);
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
			_delay_ms(5000);
			PORTB &= ~_BV(PB1);
			_delay_ms(5000);
			
			//count++;
		}
		PORTB |= _BV(PB2); // zet de rode aan
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

void USART_Init( unsigned int ubrr)
{
	/*Set baud rate */
	UBRR0H = (unsigned char)(ubrr>>8);
	UBRR0L = (unsigned char)ubrr;
	/* Enable receiver and transmitter */
	UCSR0B = (1<<RXEN0)|(1<<TXEN0);
	/* Set frame format: 8data, 2stop bit */
	UCSR0C = (1<<USBS0)|(3<<UCSZ00);
}

// timer
void timer()
{
	TCCR1B |= _BV(CS10);
}

// lampjes
uint8_t tussen;
void lees_waarde(){
	if (sensor_type == 0){
		tussen = sensor_lees(0);	
		if (tussen != waarde){
			waarde = tussen;
		}
	}
	else if( sensor_type == 1){
	
		tussen = sensor_lees(1);
		if(tussen != waarde){
			waarde = tussen;
		}
		}
}


// Zet hier alles wat geïnitialiseerd moet worden.
void setup(){	
	
	set_PortB();
	set_portC();
	set_PortD();
	USART_Init(MYUBRR);
	setRoluikStatus();
	timer();
	SCH_Init_T1(); // Schedular initialiseren 

}

int main(void)
{
	setup(); // roep de setup functie aan
	
// Zet hier onder alle taken die van af de start al moeten draaien

	SCH_Add_Task(lees_waarde, 0, 3);
	SCH_Add_Task(cont_commando, 0 ,20);
	SCH_Start(); // Enable Schedular
	
    while (1) 
    {
		// zorg er voor dat hij de taken ook gaat dischpatchen 
		
		SCH_Dispatch_Tasks();
		
    }
}

