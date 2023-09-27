#include "Man.h"
Man::Man(int lName){pName=new char[lName+1];}
Man::~Man(){delete []pName;}