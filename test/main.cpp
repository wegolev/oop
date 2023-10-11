#include <iostream>
  
int main()
{
    int a {10};
    int *pa {&a};
    std::cout << "pa: address=" << pa << "\tvalue=" << *pa << std::endl;
    int b {*pa++};      // инкремент адреса указателя
          
    std::cout << "b: value=" << b << std::endl;
    std::cout << "pa: address=" << pa << "\tvalue=" << *pa << std::endl;
}