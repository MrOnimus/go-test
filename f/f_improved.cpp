#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>
using namespace std;

int		hashSearch(vector<int>num_arr, int target)
{
	unordered_map<int, size_t>	dict;
	int							num;

	for(size_t i = 0; i < num_arr.size(); i++)
	{
		num = num_arr[i];
		if(dict.count(target - num))
			return (1);
		else
			dict.insert({ num, i });
	}
	return (0);
}

int		main() {
	int target;
	int num;
	vector<int> num_arr;
	ifstream infile("input.txt");
	ofstream outfile("output.txt");

	infile >> target;
	while(infile >> num)
		if (num < target)
			num_arr.push_back(num);

	if (num_arr.size() < 2)
		outfile << to_string(0) << endl;
	else
		outfile << to_string(hashSearch(num_arr, target)) << endl;
	return (0);
}
