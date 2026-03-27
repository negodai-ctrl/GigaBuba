#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int main() {
    setlocale(LC_ALL, "Russian");
    char a[9];
    char b[9];
    char ae[9];
    char be[9];
    char res[9];
    int temp = 0;
    cout << "Введите биты для массива 1 (8 символов максимум):" << "\n";
    cin >> a;
    while (strlen(a) > 8) {
        cout << "Вы ввели больше 8 символов! Повторите: " << "\n";
        cin >> a;
    }
    cout << "Введите биты для массива 2 (8 символов максимум):" << "\n";
    cin >> b;
    while (strlen(b) > 8) {
        cout << "Вы ввели больше 8 символов! Повторите: " << "\n";
        cin >> b;
    }
    int len1 = strlen(a);
    for (int i = 0; i < (8 - len1); i++) {
        ae[i] = '0';
        temp++;
    }
    for (int i = temp; i < 8; i++) {
        if (a[i - temp] == '0' || a[i - temp] == '1') {
            ae[i] = a[i - temp];
        }
        else {
            cout << "вы ввели недопустимый символ в массиве 1" << "\n";
        }
    }
    cout << "массив 1: ";
    for (int i = 0; i < 8; i++) {
        cout << ae[i];
    }
    cout << "\n";
    int len2 = strlen(b);
    temp = 0;
    for (int i = 0; i < (8 - len2); i++) {
        be[i] = '0';
        temp++;
    }
    for (int i = temp; i < 8; i++) {
        if (b[i - temp] == '0' || b[i - temp] == '1') {
            be[i] = b[i - temp];
        }
        else {
            cout << "вы ввели недопустимый символ в массиве 2" << "\n";
        }
    }
    cout << " массив 2:";
    for (int i = 0; i < 8; i++) {
        cout << be[i];
    }
    cout << "\n";
    for (int i = 0; i < 8; i++) {
        res[i] = (ae[i] & be[i]);
    }
    cout << "результат:";
    for (int i = 0; i < 8; i++) {
        cout << res[i];
    }
    return 0;
}
