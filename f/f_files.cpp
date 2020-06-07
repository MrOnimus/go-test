#include <iostream>
#include <fstream>
#include <vector>

int 	recursive_search(int target, std::vector<int> num_arr, int index_1,
		int index_2)
{
	if (num_arr[index_1] + num_arr[index_2] == target)
		return (1);
	else if (index_2 < num_arr.size() - 1)
		return recursive_search(target, num_arr, index_1, index_2 + 1);
	else if (index_1 < num_arr.size() - 1 && index_2 == num_arr.size() - 1)
		return recursive_search(target, num_arr, index_1 + 1, (index_2 = index_1 + 2));
	else
		return (0);
}

int		main() {
	std::vector<int> num_arr;
	int target;
	int num;

	std::ifstream infile("input.txt");
	std::ofstream outfile("output.txt");
	infile >> target;
	while(infile >> num)
		num_arr.push_back(num);
	outfile << std::to_string(recursive_search(target, num_arr, 0, 1)) << std::endl;
	return (0);
}
