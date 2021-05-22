#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream file("aaa.txt", ios::in | ios::binary);

    if (file.is_open()) {
        char memblock;

        while (!file.eof()) {
            file.read(&memblock, 1);

            if (!file.eof()) {
                cout << int(memblock);
            }
        }

        file.close();
    }

    return 0;
}
