#include <iostream>
using namespace std;
#include "calculator.h"

int main()
{
    double value1, value2, result;
    int choice;
    string name;
    
    cout << "Enter your first name (no space):\n";
    cin >> name;
    cout << "Thank you.";

    while(choice != 5)
    {
        cout << "\n\n ===== Calculator Menu ===== \n\n";
        cout << "1. Add \n";
        cout << "2. Subtract \n";
        cout << "3. Multiply \n";
        cout << "4. Divide \n";
        cout << "5. Exit \n\n";
        cout << "Enter choice. \n\n";

        cin >> choice;
        

        if(choice >= 1 && choice <= 4)
        {
            cout << "Enter first number. \n";
            cin >> value1;
            cout << "Enter second number. \n";
            cin >> value2;

            switch(choice)
            {
                case 1:
                    result = add(value1,value2);
                    cout << name << ": " << value1 << " + " << value2 << " = " << result << endl;
                    break;
                case 2:
                    result = subtract(value1,value2);
                    cout << name << ": " << value1 <<" - " << value2 << " = " << result << endl;  
                    break;
                case 3:
                    result = multiply(value1, value2);
                    cout << name << ": " << value1 <<" * " << value2 << " = " << result << endl;
                    break;
                case 4:
                    if(value2 == 0)
                    {
                        cout << "Cannot divide by 0." << endl;
                        break;
                    }
                    else
                    {
                        result = divide(value1, value2);
                        cout << name << ": " << value1 << " / " << value2 << " = " << result << endl;
                        break;
                    }
            }
        }
        else if(choice == 5)
        {
            cout << "Thank you, " << name << ". Goodbye." << endl;
        }
        else
        {
            cout << "Error. Try again." << endl;
        }
    }
    return 0;
}