#pragma once
#include <vector>

std::vector<float> getOrdStatistics(std::vector<float> unsortedData);
std::vector<int> getOrdStatistics(std::vector<int> unsortedData);

float getChosenMid(std::vector<float> ordStatistics);
float getChosenMid(std::vector<int> ordStatistics);

float getDispersion(std::vector<float> ordStatistics);
float getDispersion(std::vector<int> ordStatistics);

float getMedian(std::vector<float> ordStatistics);
float getMedian(std::vector<int> ordStatistics);

float getQuartile(std::vector<float> ordStatistics, short int numberOfQuantile = 1); // ѕозвол€ет получить квантиль по указанному номеру (1-4)
int getQuartile(std::vector<int> ordStatistics, short int numberOfQuantile = 1);