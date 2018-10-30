#include <avr/io.h>
#define F_CPU 16E6
#include <util/delay.h>
int count = 0;
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
		roluik_bezig = 1;
		PORTB &= ~_BV(PB2); // zet de rode led uit
		while(count < 15){
		PORTB |= _BV(PB1);
		_delay_ms(500);
		PORTB &= ~_BV(PB1);
		_delay_ms(500);
		
		count++;
		}
		PORTB |= _BV(PB0); // zet de groene led aan
		roluik_bezig = 0;
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
		roluik_bezig = 1;
		PORTB &= ~_BV(PB0); // zet de groen led uit
		while(count < 15){
			PORTB |= _BV(PB1);
			_delay_ms(500);
			PORTB &= ~_BV(PB1);
			_delay_ms(500);
			
			count++;
		}
		PORTB |= _BV(PB2); // zet de groene rode aan
		roluik_bezig = 0;
	}
	else if(status_roluik == 1){
		// rol luik is al omhoog
	}
	else if(roluik_bezig == 1) {
		// hier moet nog iets komen als het roluik al bezig is
	}
	
}

