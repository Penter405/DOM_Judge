
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int data_size, interval_size;
    cin >> data_size >> interval_size;

    vector<int> nums(data_size);
    for (int &x : nums) cin >> x;

    vector<vector<int>> d(data_size);
    vector<pair<int, int>> want;

    for (int i = 0; i < interval_size; i++) {
        int a, b;
        cin >> a >> b;
        --a;
        --b;

        d[a].push_back(b);
        want.push_back({a, b});
    }

    // Sort each row in alternating order
    for (int i = 0; i < data_size; i++) {
        if (i % 2 == 0) {
            sort(d[i].begin(), d[i].end());
        } else {
            sort(d[i].begin(), d[i].end(), greater<int>());
        }
    }

    // Coordinate compression
    vector<int> values = nums;
    sort(values.begin(), values.end());
    values.erase(unique(values.begin(), values.end()), values.end());

    vector<int> compressed(data_size);
    for (int i = 0; i < data_size; i++) {
        compressed[i] = lower_bound(
            values.begin(), values.end(), nums[i]
        ) - values.begin();
    }

    vector<int> appear(values.size(), 0);
    unordered_map<long long, int> res;

    int distinct = 0;
    int p1 = 0, p2 = 0;

    appear[compressed[0]]++;
    distinct++;

    for (int a = 0; a < data_size; a++) {

        while (p1 < a) {
            int x = compressed[p1];

            appear[x]--;
            if (appear[x] == 0) {
                distinct--;
            }

            p1++;
        }

        for (int b : d[a]) {

            while (p2 != b) {
                if (p2 < b) {
                    p2++;

                    int x = compressed[p2];
                    appear[x]++;

                    if (appear[x] == 1) {
                        distinct++;
                    }
                } else {
                    int x = compressed[p2];

                    appear[x]--;
                    if (appear[x] == 0) {
                        distinct--;
                    }

                    p2--;
                }
            }

            long long key = 1LL * a * data_size + b;
            res[key] = distinct;
        }
    }

    for (auto [a, b] : want) {
        long long key = 1LL * a * data_size + b;
        cout << res[key] << '\n';
    }

    return 0;
}
