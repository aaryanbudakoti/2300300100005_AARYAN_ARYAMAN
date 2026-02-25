#include <iostream>
using namespace std;

int main(){
 int n, rev=0, digit;
 cout<<"ENTER A NUMBER TO CHECK IF PALINDROME OR NOT:";
 cin>>n;
 int original=n;
 while(n!=0){
    digit=n%10;
    rev=rev*10+digit;
    n=n/10;}

    if(original==rev){
        cout<<"THE NUMBER IS A PALINDROME NUMBER";
    }
    else{
            cout<<"NOT A PALINDROME NUMBER";
        }
    }
 