#include <iostream>
#include <fstream>
using namespace std;

void input(unsigned char m[8]) {
    unsigned char temp_bs[8] = { '0', '0', '0', '0', '0', '0', '0', '0' };
    char tmp;
    int kol = 0;
    cout << "Input bs:";
    cin.get(tmp);
    while (tmp != '\n') {
        if ((tmp != '0' && tmp != '1') || (kol >= 8)) {
            cout << "Incorrect";
            exit(0);
        }
        temp_bs[kol] = tmp;
        cin.get(tmp);
        kol++;
    }
    for (int i = 0; i < kol; i++) {
        m[8 - kol + i] = temp_bs[i];
    }
}

void fileinput(string filename, unsigned char m[8]) {
    ifstream file(filename);
    if (!file.is_open()) {
        cout << "File not found" << endl;
        exit(0);
    }

    unsigned char temp_bs[8] = { '0', '0', '0', '0', '0', '0', '0', '0' };
    char tmp;
    int kol = 0;

    while (file.get(tmp)) {
        if ((tmp != '0' && tmp != '1') || (kol >= 8)) {
            cout << "Incorrect";
            exit(0);
        }
        temp_bs[kol] = tmp;
        kol++;
    }

    for (int i = 0; i < kol; i++) {
        m[8 - kol + i] = temp_bs[i];
    }
    file.close();
}

void output(unsigned char m[8]) {
    cout << "Stroka = ";
    for (int i = 0; i < 8; i++) {
        cout << m[i];
    }
    cout << endl;
}

void fileoutput(string filename, unsigned char m[8]) {
    ofstream file(filename);
    file << "Stroka = ";
    for (int i = 0; i < 8; i++) {
        file << m[i];
    }
    file.close();
}

void conjaction(unsigned char s1[8], unsigned char s2[8], unsigned char s3[8]) {
    for (int i = 0; i < 8; i++) {
        if ((s1[i] == '1') && (s2[i] == '1'))
            s3[i] = '1';
        else
            s3[i] = '0';
    }
}

int main() {
    unsigned char bs1[8] = { '0', '0', '0', '0', '0', '0', '0', '1' };
    unsigned char bs2[8] = { '0', '0', '0', '0', '0', '0', '0', '1' };
    unsigned char res[8] = { '0', '0', '0', '0', '0', '0', '0', '1' };

    //input(bs1);
    fileinput("a.txt", bs1);
    input(bs2);

    cout << "BS 1:";
    output(bs1);

    cout << endl;
    cout << "BS 2:";
    output(bs2);
    cout << endl;

    conjaction(bs1, bs2, res);
    output(res);

    system("pause");
    return 0;
}