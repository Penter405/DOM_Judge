#include <cstdlib>
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    std::string repo_url = "https://github.com/Penter405/DOM_Judge.git"; // 改成你的 repo
    std::string branch = "main";
    fs::path repoPath = "data_on_github";

    std::cout << "=== Auto Fetch Tool (No Nested Folder Version) ===" << std::endl;

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

    // 4. 初始化 git 並直接 fetch/reset 到該資料夾（絕對不要 clone）
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