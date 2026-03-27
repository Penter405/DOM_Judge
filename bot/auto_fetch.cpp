#include <cstdlib>
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

int main() {
    std::cout << "=== Auto Fetch Tool ===" << std::endl;

    // Ensure data_on_github folder exists
    fs::path repoPath = "data_on_github";
    if (!fs::exists(repoPath)) {
        std::cout << "[INFO] Folder 'data_on_github' does not exist. Creating..." << std::endl;
        fs::create_directory(repoPath);
    }

    // Check if .git exists inside data_on_github
    fs::path gitPath = repoPath / ".git";
    if (fs::exists(gitPath)) {
        std::cout << "[INFO] Git repo detected. Fetching and resetting main branch..." << std::endl;
        int result = system(
            "cmd /c \"cd data_on_github && git fetch origin main && git reset --hard origin/main && git clean -fd\""
        );
        if (result == 0)
            std::cout << "=== Sync completed successfully ===" << std::endl;
        else
            std::cout << "=== Sync failed ===" << std::endl;
    } else {
        std::cout << "[INFO] No git repo found. Cloning main branch..." << std::endl;
        int result = system(
            "git clone -b main https://github.com/yourusername/yourrepo.git data_on_github"
        );
        if (result == 0)
            std::cout << "=== Clone completed successfully ===" << std::endl;
        else
            std::cout << "=== Clone failed ===" << std::endl;
    }

    return 0;
}