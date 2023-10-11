#include <iostream>
#include <cstring>
#include "Man.h"
using namespace std;

Man::Man( int lName ) { 
    cout << "Constructor is working... ";
     pName = new char[lName + 1];
}
Man::~Man() {
    cout << "Destructor is working...";
    delete [] pName;
}
void Man::SetName(const char* fromBuf) {
     strncpy(pName, fromBuf, l_name);
    pName[l_name] = 0;
}
void Man::SetBirthYear(const char* fromBuf) {
     birth_year = atoi(fromBuf + l_name);
}
void Man::SetPay(const char* fromBuf) {
     pay = atof(fromBuf + l_name + l_year);
}
bool Man::CompareName(const char* name) const {
    if ((strstr(pName, name)) && (pName[strlen(name)] == ' ')) return true;
    else return false;
}
void Man::Print() const {
    cout << pName << birth_year << ' ' << pay << endl;
}
