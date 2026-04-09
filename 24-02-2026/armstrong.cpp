#include <iostream>
using namespace std;
int main(){
    int n, sum=0, temp, r;
    cout<<"Enter the number to check armstrong or not:";
    cin>>n;
    temp=n;
    while(n!=0){
        r=n%10;
        sum=sum+(r*r*r);
        n=n/10;
    
    }
    if(temp==sum){
        cout<<"The number is an armstrong number";
    }

    else{
        cout<<"The number is not an armstrong number";
    }
}