#include "selectionBasis.h"

std::vector<float> getOrdStatistics(std::vector<float> unsortedData)
{
	return std::vector<float>();
}

std::vector<int> getOrdStatistics(std::vector<int> unsortedData)
{
	return std::vector<int>();
}


float getChosenMid(std::vector<float> ordStatistics)
{
	return 0.0f;
}

float getChosenMid(std::vector<int> ordStatistics)
{
	return 1;
}


float getDispersion(std::vector<float> ordStatistics)
{
	return 0.0f;
}

float getDispersion(std::vector<int> ordStatistics)
{
	return 1;
}


float getMedian(std::vector<float> ordStatistics)
{
	return 0.0f;
}

float getMedian(std::vector<int> ordStatistics)
{
	return 1;
}


float getQuantile(std::vector<float> ordStatistics, short int numberOfQuantile)
{
	return 0.0f;
}

int getQuantile(std::vector<int> ordStatistics, short int numberOfQuantile)
{
	return 1;
}