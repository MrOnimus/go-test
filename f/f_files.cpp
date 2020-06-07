#include <iostream>
#include <fstream>
#include <vector>

int		not_recursive_search(int target, std::vector<int> num_arr)
{
	for (int i1 = 0; i1 < num_arr.size() - 1; i1++)
		for (int i2 = i1 + 1; i2 < num_arr.size(); i2++)
			if (num_arr[i1] + num_arr[i2] == target)
				return (1);
	return (0);
}

int		main() {
	int target;
	int num;
	std::vector<int> num_arr;
	std::ifstream infile("input.txt");
	std::ofstream outfile("output.txt");

	infile >> target;
	while(infile >> num)
		if (num < target)
			num_arr.push_back(num);

	if (num_arr.size() < 2)
		outfile << 0 << std::endl;
	else
		outfile << std::to_string(not_recursive_search(target, num_arr)) << std::endl;
	return (0);
}