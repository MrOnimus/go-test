#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int				get_digit(char c)
{
	return (c - '0');
}

char			get_char(int i)
{
	return (i + '0');
}

class BigNumber {
	std::string num;

	public:

	BigNumber()
	{
		num = "";
	}

	void		sum(char digit_in_char, int index)
	{
		int		relative_index = num.size() - 1 - index;

		if (relative_index < 0)
			return push_front(digit_in_char);
		if ((get_digit(num[relative_index]) + get_digit(digit_in_char)) >= 10)
		{
			num[relative_index] = get_char((get_digit(num[relative_index]) + get_digit(digit_in_char)) % 10);
			if (relative_index == 0)
				return push_front('1');
			while (relative_index >= 0 && get_digit(num[--relative_index]) + 1 >= 10)
			{
				if (relative_index < 0)
					return push_front('1');
				num[relative_index] = get_char(get_digit((num[relative_index]) + 1) % 10);
			}
			if (relative_index < 0)
				return push_front('1');
			num[relative_index] = get_char(get_digit((num[relative_index]) + 1));
		}
		else
		{
			num[relative_index] = get_char(get_digit(num[relative_index]) + get_digit(digit_in_char));
		}
	}

	void		push_front(char c)
	{
		num = c + num;
	}

	void		set(std::string new_num)
	{
		num = new_num;
	}

	std::string	get()
	{
		return (num);
	}

	void		print()
	{
		std::cout << num << std::endl;
	}
};

int		main() {
	std::string num1;
	std::string num2;
	BigNumber result;

	std::cin >> num1;
	std::cin >> num2;
	result.set(num1);
	for (int i = num2.size() - 1; i >= 0; i--)
	{
		result.sum(num2[i], num2.size() - i - 1);
	}
	result.print();
	return (0);
}
