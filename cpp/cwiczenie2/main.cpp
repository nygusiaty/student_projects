#include <iostream>

using namespace std;

float kalkulatorPredkosci(float droga,float czas) {
    droga = droga * 1000;
    czas = czas * 60;
    float wynik = droga/czas*3.6;
    return wynik;
}

int main(){
	float czas = 0;
	float odleglosc =0;

	cout<<"podaj odleglosc przejechana przez samochod w kilometrach"<<endl;
	cin>>odleglosc;
 
	cout<<"podaj czas przejazdu samochodu w minutach"<<endl;
	cin>>czas;
	
	float wynik = kalkulatorPredkosci(odleglosc, czas);

	cout<<wynik<<"KM/h"<<endl;
	
	return 0;
}
