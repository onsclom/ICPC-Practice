#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>

using namespace std;

int main()
{
    string curLine;
    while (getline(cin, curLine))
    {
        stringstream sStream(curLine);

        string stringNum;
        int runningMax = 0;
        int count = 0;
        bool firstRead = true;
        int previous;
        while (sStream >> stringNum)
        {
            int curNum = stoi(stringNum);
            count++;
            int curDifference = 0;

            //find curMax
            if (!firstRead)
            {
                curDifference = abs(previous-curNum);
            }
            else 
            {
                firstRead = false;
            }


            //this code sets max if needed
            if (curDifference > runningMax)
            {
                runningMax = curDifference;
            }

            previous = curNum;
        }

        if (runningMax >= 1 && runningMax <= count-1)
        {
            cout << "Jolly" << endl;
        }
        else
        {
            cout << "Not Jolly" << endl;
        }
    }
}