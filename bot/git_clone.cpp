#include <cstdlib>
#include <filesystem>
#include <iostream>
#include <fstream>
#include <string>

namespace fs = std::filesystem;

void trim(std::string& s) {
    size_t start = s.find_first_not_of(" \n\r\t");
    if (start == std::string::npos) {
        s.clear();
        return;
    }
    s.erase(0, start);
    s.erase(s.find_last_not_of(" \n\r\t") + 1);
}

int main() {
    // ─── Read repo URL from my_repo_url.txt ───
    std::string repo_url = "";
    // When exe is next to bot folder → read bot/my_repo_url.txt
    // When exe is inside bot folder  → read my_repo_url.txt
    std::string url_file = fs::exists("bot") ? "bot/my_repo_url.txt" : "my_repo_url.txt";
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
    if (repo_url.back() == '/') {
        repo_url.pop_back();
    }

    // Extract base repo URL: keep only https://github.com/{user}/{repo}
    {
        std::string marker = "github.com/";
        size_t pos = repo_url.find(marker);
        if (pos != std::string::npos) {
            size_t path_start = pos + marker.length();
            size_t first_slash = repo_url.find('/', path_start);
            if (first_slash != std::string::npos) {
                size_t second_slash = repo_url.find('/', first_slash + 1);
                if (second_slash != std::string::npos) {
                    repo_url = repo_url.substr(0, second_slash);
                }
            }
        }
    }

    // Strip .git suffix if present before re-adding
    if (repo_url.length() >= 4 && repo_url.substr(repo_url.length() - 4) == ".git") {
        repo_url = repo_url.substr(0, repo_url.length() - 4);
    }
    repo_url += ".git";

    std::cout << "[INFO] Using repo: " << repo_url << std::endl;

    std::string branch = "main";
    fs::path repoPath = "data_on_github";

    std::cout << "=== Auto Fetch Tool (Git Clone Version) ===" << std::endl;

    // 1. 如果資料夾不存在 → 創建
    if (!fs::exists(repoPath))
        fs::create_directory(repoPath);

    fs::path gitPath = repoPath / ".git";

    // 2. 如果是正常 git repo → fetch + reset + clean
    if (fs::exists(gitPath)) {
        std::cout << "[INFO] Git repo detected. Fetching and resetting main branch..." << std::endl;
        std::string cmd = "git -C \"" + repoPath.string() + "\" fetch origin " + branch +
                          " && git -C \"" + repoPath.string() + "\" reset --hard origin/" + branch +
                          " && git -C \"" + repoPath.string() + "\" clean -fd";
        int result = system(cmd.c_str());
        if (result == 0) {
            std::cout << "[SUCCESS] Folder synced with main branch!" << std::endl;
            return 0;
        } else {
            std::cout << "[WARNING] Repo may be broken. Will force re-init..." << std::endl;
        }
    }

    // 3. 如果 .git 不存在 或 fetch/reset 失敗 → 清空資料夾內容
    std::cout << "[INFO] Force-sync: clearing folder and re-initializing git..." << std::endl;
    for (auto &p : fs::directory_iterator(repoPath))
        fs::remove_all(p);

    // 4. 初始化 git 並直接 fetch/reset 到該資料夾
    std::string cmd_init =
        "cd \"" + repoPath.string() + "\" && "
        "git init && "
        "git remote add origin " + repo_url + " && "
        "git fetch origin " + branch + " && "
        "git reset --hard origin/" + branch + " && "
        "git clean -fd";

    int result = system(cmd_init.c_str());
    if (result == 0)
        std::cout << "[SUCCESS] Folder force-synced with GitHub main branch!" << std::endl;
    else
        std::cout << "[ERROR] Force-sync failed! Exit code: " << result << std::endl;

    return 0;
}