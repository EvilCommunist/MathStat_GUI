#include "selectionBasis.h"

std::vector<float> getOrdStatistics(std::vector<float> unsortedData){
	for (int i = 0; i < unsortedData.size(); i++) {
		for (int j = i; j < unsortedData.size(); j++) {
			if (unsortedData[j] < unsortedData[i]) {
				float temp = unsortedData[j];
				unsortedData[j] = unsortedData[i];
				unsortedData[i] = temp;
			}
		}
	}
	return unsortedData;
}

std::vector<int> getOrdStatistics(std::vector<int> unsortedData){
	for (int i = 0; i < unsortedData.size(); i++) {
		for (int j = i; j < unsortedData.size() - 1; j++) {
			if (unsortedData[j] < unsortedData[i]) {
				int temp = unsortedData[j];
				unsortedData[j] = unsortedData[i];
				unsortedData[i] = temp;
			}
		}
	}
	return unsortedData;
}


float getChosenMid(std::vector<float> ordStatistics){
	float sum{}, mid{};
	for (int i = 0; i < ordStatistics.size(); i++) {
		sum += ordStatistics[i];
	}
	mid = sum / ordStatistics.size();
	return mid;
}

float getChosenMid(std::vector<int> ordStatistics){
	float sum{}, mid{};
	for (int i = 0; i < ordStatistics.size(); i++) {
		sum += ordStatistics[i];
	}
	mid = sum / ordStatistics.size();
	return mid;
}


float getDispersion(std::vector<float> ordStatistics){
	auto ch_mid = getChosenMid(ordStatistics);
	float sum{};
	for (int i = 0; i < ordStatistics.size(); i++) {
		sum += pow(ordStatistics[i] - ch_mid,2);
	}
	auto disp = sum / ordStatistics.size();
	return disp;
}

float getDispersion(std::vector<int> ordStatistics){
	auto ch_mid = getChosenMid(ordStatistics);
	float sum{};
	for (int i = 0; i < ordStatistics.size(); i++) {
		sum += pow(ordStatistics[i] - ch_mid, 2);
	}
	auto disp = sum / ordStatistics.size();
	return disp;
}


float getMedian(std::vector<float> ordStatistics){
	auto size = ordStatistics.size();
	auto firstElem = ordStatistics[size / 2-1];
	auto secondElem = ordStatistics[size / 2];
	return (firstElem + secondElem) / 2;
}

float getMedian(std::vector<int> ordStatistics){
	auto size = ordStatistics.size();
	float firstElem = ordStatistics[size / 2-1];
	float secondElem = ordStatistics[size / 2];
	return (firstElem + secondElem) / 2;
}


float getQuartile(std::vector<float> ordStatistics, short int numberOfQuantile){
	return ordStatistics[ordStatistics.size()*0.25*numberOfQuantile];
}

int getQuartile(std::vector<int> ordStatistics, short int numberOfQuantile){
	return ordStatistics[ordStatistics.size() * 0.25 * numberOfQuantile];
}