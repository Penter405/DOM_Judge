#include <windows.h>
#include <urlmon.h>
#include <iostream>
#include <string>

#pragma comment(lib, "urlmon.lib")

int main()
{
    std::cout << "=== Auto ZIP Updater (No Git Required) ===" << std::endl;

    // =========================
    // 🔧 設定區（可修改）
    // =========================

    // 📦 GitHub repo ZIP 下載連結（public repo）
    std::string repoURL = "https://github.com/Penter405/DOM_Judge/archive/refs/heads/main.zip";

    // 📁 下載後的 zip 檔案名稱
    std::string zipFileName = "repo.zip";

    // 📂 解壓縮暫存資料夾
    std::string extractFolder = "temp_repo";

    // 📂 最終更新目標資料夾（你的程式資料）
    std::string targetFolder = "data_on_github";

    // 📁 GitHub 解壓後的資料夾名稱（通常是 repo-name + branch）
    std::string githubExtractFolderName = "DOM_Judge-main";

    // =========================
    // 1️⃣ 下載 ZIP
    // =========================
    std::cout << "[1/3] 下載 GitHub ZIP..." << std::endl;

    HRESULT downloadResult = URLDownloadToFileA(
        NULL,
        repoURL.c_str(),
        zipFileName.c_str(),
        0,
        NULL);

    if (downloadResult != S_OK)
    {
        std::cout << "[ERROR] 下載失敗！" << std::endl;
        return 1;
    }

    std::cout << "[OK] 下載完成" << std::endl;

    // =========================
    // 2️⃣ 解壓 ZIP
    // =========================
    std::cout << "[2/3] 解壓 ZIP..." << std::endl;

    std::string extractCommand =
        "powershell -Command \"Expand-Archive -Force " +
        zipFileName + " " + extractFolder + "\"";

    int extractResult = system(extractCommand.c_str());

    if (extractResult != 0)
    {
        std::cout << "[ERROR] 解壓失敗！" << std::endl;
        return 1;
    }

    std::cout << "[OK] 解壓完成" << std::endl;

    // =========================
    // 3️⃣ 複製檔案到目標資料夾
    // =========================
    std::cout << "[3/3] 同步檔案..." << std::endl;

    std::string copyCommand =
        "xcopy /E /Y /I " +
        extractFolder + "\\" + githubExtractFolderName + "\\* " +
        targetFolder;

    int copyResult = system(copyCommand.c_str());

    if (copyResult != 0)
    {
        std::cout << "[ERROR] 複製失敗！" << std::endl;
        return 1;
    }

    std::cout << "[SUCCESS] 更新完成！" << std::endl;

    // =========================
    // 🧹 清理暫存檔案
    // =========================

    system(("del " + zipFileName).c_str());           // 刪除 zip 檔
    system(("rmdir /S /Q " + extractFolder).c_str()); // 刪除解壓資料夾

    return 0;
}