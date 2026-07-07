#include <windows.h>
#include <urlmon.h>
#include <iostream>
#include <fstream>
#include <string>

#pragma comment(lib, "urlmon.lib")

void trim(std::string& s) {
    size_t start = s.find_first_not_of(" \n\r\t");
    if (start == std::string::npos) {
        s.clear();
        return;
    }
    s.erase(0, start);
    s.erase(s.find_last_not_of(" \n\r\t") + 1);
}

int main()
{
    std::cout << "=== Auto ZIP Updater (No Git Required) ===" << std::endl;

    // ─── Read repo URL from my_repo_url.txt ───
    std::string repo_url = "";
    // When the exe is next to the bot folder (moved out), look for bot/my_repo_url.txt
    // When running from inside bot folder, look for my_repo_url.txt directly
    std::string url_file;
    {
        WIN32_FIND_DATAA fd;
        HANDLE hFind = FindFirstFileA("bot", &fd);
        if (hFind != INVALID_HANDLE_VALUE && (fd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
            url_file = "bot\\my_repo_url.txt";
            FindClose(hFind);
        } else {
            url_file = "my_repo_url.txt";
            if (hFind != INVALID_HANDLE_VALUE) FindClose(hFind);
        }
    }

    std::ifstream infile(url_file);
    if (infile.is_open()) {
        std::getline(infile, repo_url);
        infile.close();
        trim(repo_url);
    }

    if (repo_url.empty()) {
        std::cout << "Please enter your GitHub repository URL: ";
        std::getline(std::cin, repo_url);
        trim(repo_url);

        std::ofstream outfile(url_file);
        if (outfile.is_open()) {
            outfile << repo_url << std::endl;
            outfile.close();
        } else {
            std::cout << "[WARNING] Could not save URL to " << url_file << std::endl;
        }
    }

    if (repo_url.empty()) {
        std::cout << "[ERROR] No valid URL provided. Exiting..." << std::endl;
        return 1;
    }

    // ─── Normalize URL ───
    // Strip trailing slash
    if (!repo_url.empty() && repo_url.back() == '/') {
        repo_url.pop_back();
    }

    // Extract base repo URL: keep only https://github.com/{user}/{repo}
    std::string user, repo;
    {
        std::string marker = "github.com/";
        size_t pos = repo_url.find(marker);
        if (pos != std::string::npos) {
            size_t path_start = pos + marker.length();
            size_t first_slash = repo_url.find('/', path_start);
            if (first_slash != std::string::npos) {
                user = repo_url.substr(path_start, first_slash - path_start);
                size_t second_slash = repo_url.find('/', first_slash + 1);
                if (second_slash != std::string::npos) {
                    repo = repo_url.substr(first_slash + 1, second_slash - first_slash - 1);
                    repo_url = repo_url.substr(0, second_slash);
                } else {
                    repo = repo_url.substr(first_slash + 1);
                }
            }
        }
    }

    // Strip .git suffix if present
    if (repo.length() >= 4 && repo.substr(repo.length() - 4) == ".git") {
        repo = repo.substr(0, repo.length() - 4);
    }
    if (repo_url.length() >= 4 && repo_url.substr(repo_url.length() - 4) == ".git") {
        repo_url = repo_url.substr(0, repo_url.length() - 4);
    }

    std::string branch = "main";

    // Build the ZIP download URL:
    // https://github.com/{user}/{repo}/archive/refs/heads/main.zip
    std::string zipURL = repo_url + "/archive/refs/heads/" + branch + ".zip";

    // The folder name inside the ZIP that GitHub creates: {repo}-{branch}
    std::string githubExtractFolderName = repo + "-" + branch;

    std::string zipFileName = "repo.zip";
    std::string extractFolder = "temp_repo";
    std::string targetFolder = "data_on_github";

    std::cout << "[INFO] Using repo: " << repo_url << std::endl;
    std::cout << "[INFO] ZIP URL:    " << zipURL << std::endl;

    // =========================
    // 1. Download ZIP
    // =========================
    std::cout << "[1/3] Downloading GitHub ZIP..." << std::endl;

    HRESULT downloadResult = URLDownloadToFileA(
        NULL,
        zipURL.c_str(),
        zipFileName.c_str(),
        0,
        NULL);

    if (downloadResult != S_OK)
    {
        std::cout << "[ERROR] Download failed!" << std::endl;
        return 1;
    }

    std::cout << "[OK] Download complete" << std::endl;

    // =========================
    // 2. Extract ZIP
    // =========================
    std::cout << "[2/3] Extracting ZIP..." << std::endl;

    std::string extractCommand =
        "powershell -Command \"Expand-Archive -Force " +
        zipFileName + " " + extractFolder + "\"";

    int extractResult = system(extractCommand.c_str());

    if (extractResult != 0)
    {
        std::cout << "[ERROR] Extraction failed!" << std::endl;
        return 1;
    }

    std::cout << "[OK] Extraction complete" << std::endl;

    // =========================
    // 3. Copy files to target folder
    // =========================
    std::cout << "[3/3] Syncing files..." << std::endl;

    std::string copyCommand =
        "xcopy /E /Y /I " +
        extractFolder + "\\" + githubExtractFolderName + "\\* " +
        targetFolder;

    int copyResult = system(copyCommand.c_str());

    if (copyResult != 0)
    {
        std::cout << "[ERROR] Copy failed!" << std::endl;
        return 1;
    }

    std::cout << "[SUCCESS] Update complete!" << std::endl;

    // =========================
    // Cleanup temp files
    // =========================

    system(("del " + zipFileName).c_str());
    system(("rmdir /S /Q " + extractFolder).c_str());

    return 0;
}