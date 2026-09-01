#include <stdio.h>

double add(double a, double b){
    return a+b;
}
double subtract(double a, double b){
    return a-b;
}
double multiply(double a, double b){
    return a*b;
}
double divide(double a, double b){
    return a/b;
}

int main()
{
    int choice;
    double num1, num2, result;
    char userName[50];

    printf("Enter your first name (no space): ");
    scanf("%s",userName); // Reads until the first space

    do
    {
        printf("\n===== Calculator Menu =====\n");
        printf("1. Add\n");
        printf("2. Subtract\n");
        printf("3. Multiply\n");
        printf("4. Divide\n");
        printf("5. Exit\n");

        printf("Enter choice: ");
        scanf("%d", &choice);

        if(choice >= 1 && choice <= 4)
        {
            printf("Enter first number: ");
            scanf("%lf", &num1);

            printf("Enter second number: ");
            scanf("%lf", &num2);

            switch(choice)
            {
                case 1:
                    result = add(num1,num2);
                    break;
                case 2:
                    result = subtract(num1,num2);
                    break;
                case 3:
                    result = multiply(num1,num2);
                    break;
                case 4:
                    if(num2 == 0)
                    {
                        printf("Cannot divide by zero.\n");
                        continue;
                    }
                    result = divide(num1,num2);
                    break;
            }

            printf("Result = %lf\n", result);
        }

    } while(choice != 5);

    return 0;
}