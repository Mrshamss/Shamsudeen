// Sementer Project c++.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	double num1, num2;
	char operation, redo;


	cout << "Welcome to calculator program by Shamsuddeen_Muhammad_Lawal\n" << endl;

	cout << endl;

	do 
	{ 


	cout << "Please enter an opration which you like to calculate \n(+, -, *, /, s)";

	cout << "[s stand for swap]:";

	cin >> operation;
	cout << endl << endl;
	cout << "Please enter two numbers to apply your requested operation( ";
	cout << operation << "):" << endl << "1st num:";
	cin >> num1;
	cout << "2nd num:";
	cin >> num2;
	cout << endl;
	switch (operation)
	{
	case '+':
		cout << "The addition of two numbers (" << num1 << "," << num2 << "):";
		cout << num1 + num2 << endl;
		break;
	case'-':
		cout << "The substracation of two numbers (" << num1 << "," << num2 << "):";
		cout << num1 -
			num2 << endl;
		break;
	case'*':
		cout << "The multiplication of two numbers (" << num1 << "," << num2 << "):";
		cout << num1 * num2 << endl;

		break;
	case'/':
		cout << "The division of two numbers(" << num1 << "," << num2 << "):";
		if (num2 == 0)
		{
			cout << "not valid" << endl;

		}
		cout << (num1 / num2) << endl;
		break;
	case's':
		cout << "The swap of two numbers (" << num1 << "," << num2 << "):";
		swap(num1, num2);
		cout << "1stnumber=" << num1 << " and 2nd number="
			<< num2 << endl << endl;
		break;
	default:
		cout << "unknown command" << endl;
	}
		cout << "enter y or Y to contiue:";
		cin >> redo;
		cout << endl << endl;
		
	
}
	while (redo == 'y' || redo == 'Y');
	
	return 0;
	
}

	

	
	




