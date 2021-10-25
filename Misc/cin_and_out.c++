// Figuring how to includepath for windows.h, will do later.
#include <iostream>
#include <fstream>
#include <string>   

using namespace std;

// Reads input and redirects it into a file.
void f() {
    string line;
    while (getline(cin, line)) {
        cout << line << "\n";
    }
}

int main() {
    ifstream in("input.txt"); // Input file stream takes in an input from in.txt
    streambuf *cinbuf = cin.rdbuf(); // Save the old buffer
    cin.rdbuf(in.rdbuf()); // Redirect std::cin to in.txt

    ofstream out("output.txt"); // Output file stream outputs the input
    streambuf *coutbuf = cout.rdbuf(); // Saves the old buffer
    cout.rdbuf(out.rdbuf()); // Redirects cout to out.txt

    string word;
    cin >> word; // Input from file input.txt
    cout << word << " "; // Output to file output.txt

    f();

    cin.rdbuf(cinbuf); // Reset to Standard input again
    cout.rdbuf(coutbuf); // Reset to Standard output again

    cin >> word; // input from the standard input
    cout << word; // output to the standard input
}





