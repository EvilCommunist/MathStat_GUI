#include <iostream>
#include <fstream>
#include "../../selectionBasis.h"

bool readData1Dim(std::string filepath, std::vector<float>& toFill) {
    std::ifstream testInput;
    testInput.open(filepath, testInput.in);
    if (!testInput.is_open()) { // Проверка на открытие файла
        std::cout << "Cannot open current file!";
        return false;
    }

    float temp{};
    while (testInput >> temp) {
        toFill.push_back(temp);
    }
    return true;
}
bool readData1Dim(std::string filepath, std::vector<int>& toFill) {
    std::ifstream testInput;
    testInput.open(filepath, testInput.in);
    if (!testInput.is_open()) { // Проверка на открытие файла
        std::cout << "Cannot open current file!";
        return false;
    }

    int temp{};
    while (testInput >> temp) {
        toFill.push_back(temp);
    }
    return true;
}

void writeVector(std::vector<float> toWrite) {
    for (int i = 0; i < toWrite.size(); i++) {
        std::cout << toWrite[i] << " ";
    }
}
void writeVector(std::vector<int> toWrite) {
    for (int i = 0; i < toWrite.size(); i++) {
        std::cout << toWrite[i] << " ";
    }
}

int main(){
    std::string filepath = "../../../RStudio_test/r_test_data/test_data_for_1dimension.txt";
    std::vector<float> test;
    if (!readData1Dim(filepath, test))
        return 1;

    auto sortedTest = getOrdStatistics(test);
    writeVector(sortedTest);
    std::cout << std::endl << getChosenMid(sortedTest);
    std::cout << std::endl << getDispersion(sortedTest);
    std::cout << std::endl << getMedian(sortedTest);
    std::cout << std::endl << getQuartile(sortedTest, 1);
    std::cout << std::endl << getQuartile(sortedTest, 3);
    std::cout << "\nTest successfully completed!";
}

