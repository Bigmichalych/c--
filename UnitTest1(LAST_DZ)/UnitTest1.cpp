#define _USE_MATH_DEFINES
#include "pch.h"
#include "CppUnitTest.h"
#include "../samouchka/FileName.cpp"


using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest1)
	{
	public:

		float x = 0;
		float y = 5;
		float r = cos(x / y);
		float s = pow(2, -3 * x) + pow(M_PI * y, 1 / 3);

        TEST_METHOD(TestPositiveNumbers)
        {
            Assert::AreEqual(TwoFunk(1.0f, 3.0f), 0.78565f);
            
        }
        TEST_METHOD(TestPositiveNumbers)
        {
            Assert::AreEqual(TwoFunk(1.0f, 3.0f), 0.78565f);

        }
        TEST_METHOD(TestNegativeNumb)
        {
            Assert::AreEqual(TwoFunk(-3.0f, -4.0f), 0.447636f);
            
        }
        TEST_METHOD(TestInf)
        {
            auto function = [] { TwoFunk(1.0f, 0.0f); };
            Assert::ExpectException<std::invalid_argument>(function);

        }
        
        TEST_METHOD(isSmax)
        {
            Assert::IsTrue(TwoFunk(x, y) > r);
        }
        
    };
}
