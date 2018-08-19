#include <iostream>

long long greatestCommonDivisor(int a, int b)
{
  if (a == 0)
  {
    return b;
  }

  if (b == 0)
  {
    return a;
  };

  long long remains = a % b;

  return (long long)greatestCommonDivisor(b, remains);
}

long long leastCommonDivisor(int a, int b)
{
  double result = a / greatestCommonDivisor(a, b) * b;

  return result;
}

int main()
{
  int a, b;
  std::cin >> a >> b;
  std::cout << greatestCommonDivisor(a, b) << std::endl;
  return 0;
}
