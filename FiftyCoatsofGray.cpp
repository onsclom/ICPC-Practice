#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;


int main()
{
    int num1, num2, num3;
    int index = 0;
    int totalSum = 0;
    string line, line2;
    
    while(getline(cin, line)){
        stringstream S(line);
        S >> num1 >> num2 >> num3;
        float sumForLines = 0;
        float sumForRooms = 0;
        for(int i = 0; i < num3; i++){
            getline(cin, line2);
            stringstream S2(line2);
            // cout << line2 << endl;
            float h, w, l;
            S2 >> h >> w >> l; 
            // cout << "h " << h << " w " << w << " l " << l << endl;
            sumForLines = (2 * h * w) + (w * l) + (2 * l * h);
            S2 >> index;
            // cout << "Index: " << index << endl;
            float sumofWins = 0;
            for (int j = 0; j < index; j++)
            {
             	float win1, win2;
                S2 >> win1 >> win2;
                // cout << "Win1: " << win1 << "    Win2: " << win2 << endl;
                sumofWins += (win2 * win1);
            }
            // cout << "Sum of wins : " << sumofWins << endl;
            sumForRooms += (sumForLines - sumofWins);
            // cout << sumForRooms << endl;
        }

	sumForRooms *= num1;
        float one = sumForRooms;
        float two = num2;
        float floatSum = one / two;
        sumForRooms = ceil(floatSum);
        // cout << sumForRooms << endl;

        cout << sumForRooms << endl;

    }
    



    return 0;
}
