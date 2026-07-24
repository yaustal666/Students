#include <string>
#include <fstream>
#include <iostream>
#include <filesystem>

class ImageDecoder {
private:
    std::string imagePath;
    std::string key;
    int messageSizeLimit = 2000;
    int messageStart = -1;
public:
    ImageDecoder(std::string& path, std::string& key, int limit) {
        imagePath = path;
        this->key = key;
        messageSizeLimit = limit;
    }

    bool findMessage() {
        std::ifstream imageFile(imagePath);
        int fileSize = std::filesystem::file_size(imagePath);
        int scanBytes = messageSizeLimit + key.size() + 100;
        if (fileSize >= scanBytes) {
            imageFile.seekg(-scanBytes, std::ios::end);
        } else {
            imageFile.seekg(0, std::ios::beg);
        }

        char a;
        while (imageFile.get(a)) {
            if (a == char(key[0])) {
                int count = 1;
                for (size_t i = 1; i < key.size(); i++) {
                    if (imageFile.get(a)) {
                        if (a == key[i]) {
                            count++;
                        } else {
                            break;
                        }
                    } else {
                        break;
                    }
                }

                if (count == key.size()) {
                    messageStart = static_cast<int>(imageFile.tellg());
                    imageFile.close();
                    return true;
                }
            }
        }

        imageFile.close();
        return false;
    }
};