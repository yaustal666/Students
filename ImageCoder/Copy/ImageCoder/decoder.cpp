#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>

int main() {
    
    std::filesystem::path filepath = "./testImages/bmpImage.bmp";

    std::uint64_t filesize = std::filesystem::file_size(filepath);
    std::cout << "File size: " << filesize << " bytes" << std::endl;
    std::ifstream imageFile("./testImages/bmpImage.bmp", std::ios::binary);

    std::size_t bytesToRead = (filesize < 500) ? filesize : 500;
    imageFile.seekg(-bytesToRead, std::ios::end);

    // std::ofstream output("./ouptutBmp.txt");

    std::vector<char> buffer;
    buffer.reserve(500);

    char a;
    while(imageFile.get(a)) {
        buffer.push_back(a);
    }

    for (auto i : buffer) {
        std::cout << i;
    }
}