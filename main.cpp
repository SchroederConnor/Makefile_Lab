#include <iostream>
using namespace std;
#include "calculator.h"

int main()
{
    double value1, value2, result;
    string name;
    cin >> value1 >> value2;
    cout << value1 << " & " << value2 << endl;

    result = add(value1,value2);
    cout << name << value1 <<" + " << value2 << " = " << result << endl;

    result = subtract(value1,value2);
    cout << name << value1 <<" - " << value2 << " = " << result << endl;

    result = multiply(value1, value2);
    cout << name << value1 <<" * " << value2 << " = " << result << endl;

    result = divide(value1, value2);
    cout << name << value1 << " / " << value2 << " = " << result << endl;

    return 0;
}