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
	return 0.0f;
}

float getChosenMid(std::vector<int> ordStatistics){
	return 1;
}


float getDispersion(std::vector<float> ordStatistics){
	return 0.0f;
}

float getDispersion(std::vector<int> ordStatistics){
	return 1;
}


float getMedian(std::vector<float> ordStatistics){
	return 0.0f;
}

float getMedian(std::vector<int> ordStatistics){
	return 1;
}


float getQuantile(std::vector<float> ordStatistics, short int numberOfQuantile){
	return 0.0f;
}

int getQuantile(std::vector<int> ordStatistics, short int numberOfQuantile){
	return 1;
}