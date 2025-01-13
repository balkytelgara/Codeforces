#include <iostream>

using namespace std;

int ldfd(int a, int b) {
    int last_digit = 1;

    for (int i = b; i > a; --i) {
        if (i % 10 == 0) {
            continue;
        }

        last_digit = (last_digit * (i % 10)) % 10;

        if (last_digit == 0) {
            return 0;
        }
    }

    return last_digit;
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << ldfd(a, b) << endl;

    return 0;
}