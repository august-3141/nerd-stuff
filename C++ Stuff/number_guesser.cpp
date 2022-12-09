#include <iostream>
#include <cstdlib>

using namespace std;

int main() {

    int MAX = 10;
    int guess;
    int trueNum;

    cout << "*** Number Guesser ***" << endl;
    cout << "----------------------" << endl;

    cout << "Enter your guess (1-10): " << endl;
    cin >> guess;

    srand(time(0));

    trueNum = rand()%MAX;

    cout << "The number was " << trueNum << "." << endl;

    if (trueNum == guess) {

        cout << "You got the number right, good job!";

    } else {

        int amountOff = guess - trueNum;
        amountOff = abs(amountOff);

        cout << "Nice try, you were only " << amountOff << " off!";

    }

    return 0;

}