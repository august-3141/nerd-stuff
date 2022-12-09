// normal enough distribution

#include <iostream>
#include <random>

using namespace std;

int main() {

    cout << "*** Psuedo-random Number Counter ***" << endl;
    cout << "------------------------------------" << endl;

   std::default_random_engine pseudo_random_generator;
   std::uniform_int_distribution<int> int_distribution(0, 9);
   
   int actual_distribution[10] = {0,0,0,0,0,0,0,0,0,0};
   
   for(int i = 0; i < 10000; i++) {
       int result = int_distribution(pseudo_random_generator);
       actual_distribution[result]++;
   }

   for(int i = 0; i <= 9; i++) {
       std::cout << actual_distribution[i] << " ";
   }
}