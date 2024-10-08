#include <iostream>
#include <algorithm>
using namespace std;
int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};
int N,M;
int map[501][501];
bool visited[501][501];
int max1 = -1;

void dfs(int x, int y, int cnt = 0, int s = 0) {
	if (cnt == 4) {
		if (max1 < s) {
			max1 = s;
		}
	}
	else {
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (0 <= nx  && nx < N && 0 <= ny && ny < M) {
				//cout << nx << x << ny << y << endl;
				if (!visited[nx][ny]) {
					visited[nx][ny] = true;
					dfs(nx,ny,cnt+1,s+map[nx][ny]);
					visited[nx][ny] = false;
				}
			}
		}
	}
}

void check(int y, int x) {
	if (x + 2 < M && y + 1 < N) {
		max1 = max(max1, map[y][x] + map[y][x + 1] + map[y][x + 2] + map[y + 1][x + 1]);
	}
	if (y + 2 < N && x + 1 < M) {
		max1 = max(max1, map[y][x] + map[y + 1][x] + map[y + 2][x] + map[y + 1][x + 1]);
	}
	if (y - 1 >= 0 && y + 1 < N && x + 1 < M) {
		max1 = max(max1, map[y][x] + map[y - 1][x + 1] + map[y][x + 1] + map[y + 1][x + 1]);
	}
	if (y - 1 >= 0 && x + 2 < M) {
		max1 = max(max1, map[y][x] + map[y - 1][x + 1] + map[y][x + 1] + map[y][x + 2]);
	}
	return;
}

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
			visited[i][j] = false;
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			visited[i][j] = true;
			dfs(i,j,1,map[i][j]);
			visited[i][j] = false;
			check(i,j);
		}
	}
	cout << max1 << endl;
	return 0;
}