#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

const int SIZE = 20;

void intilalize(/*in*/bool[][SIZE]);
void printgrid2(/*in*/bool[][SIZE]);
void readDatafile(/*in*/bool[][SIZE]);
void countneighbors(/*in*/bool[][SIZE], /*in*/bool[][SIZE]);
int livingRowTen(/*in*/bool[][SIZE]);
int livingColumnTen(/*in*/bool[][SIZE]);
int deadcellsRowSixteen(/*in*/bool[][SIZE]);
int deadcellscolumnOne(/*in*/bool[][SIZE]);
int livingEntireBoard(/*in*/bool[][SIZE]);
int deadEntireBoard(/*in*/bool[][SIZE]);

int main()
{
	bool shape[SIZE][SIZE];
	bool nextgen[SIZE][SIZE];

	intilalize(shape); //function call
	intilalize(nextgen);
	readDatafile(shape);//function call
	readDatafile(nextgen);






	for (int gen = 0; gen<5; gen++)
	{
		countneighbors(shape, nextgen);
		for (int i = 0; i < SIZE; ++i)
		{
			for (int j = 0; j < SIZE; ++j)
			{
				shape[i][j] = nextgen[i][j];
			}
		}
	}

	cout << endl << endl;
	printgrid2(shape);

	cout << endl;
	cout << "GAME OF LIFE STATS (5th GENERATION)" << endl;
	cout << "Total alive in row 10 = " << livingRowTen(nextgen) << endl;
	cout << "Total alive in col 10 = " << livingColumnTen(nextgen) << endl;
	cout << "Total dead in row 16 = " << deadcellsRowSixteen(nextgen) << endl;
	cout << "Total dead in col 1 = " << deadcellscolumnOne(nextgen) << endl;
	cout << "Total alive = " << livingEntireBoard(nextgen) << endl;
	cout << "Total dead = " << deadEntireBoard(nextgen) << endl;

	return 0;
}

///this function will intilize the array with data.
void intilalize(bool/*in*/ somearray[][SIZE])
///pre:function is called
///post:the array is intillized
{
	for (int row = 0; row < SIZE; row++)
	{
		for (int col = 0; col < SIZE; col++)
		{
			somearray[row][col] = false;
		}
	}
}

///this function will print the array in a grid format after being intilized.
void printgrid2(/*in*/bool somearray[][SIZE])
///pre:the function is called
///post:the contents of the array are posted in a grid format
{
	cout << "  01234567890123456789" << endl;

	for (int row = 0; row < SIZE; row++)
	{
		cout << setw(2) << row;
		for (int col = 0; col < SIZE; col++)
		{
			if (somearray[row][col])
			{
				cout << "*";
			}
			else
			{
				cout << " ";
			}
		}
		cout << endl;
	}
}
///this function reads in data from a txt file specified by the user.
void readDatafile(/*in*/bool somearray[][SIZE])
///pre:the function is called
///post:the data is filed in with the data from the specified txt file
{
	int row, col;



	ifstream infile("bacteria.txt");

	infile >> row >> col;
	while (infile)
	{
		somearray[row][col] = true;
		infile >> row >> col;
	}
	infile.close();

}
///this function checks whether there is life inside of each grid of the array or not and changes accordingly with the rules
///of the game of life
void countneighbors(/*in*/bool somearray[][SIZE], /*in*/bool nextGen[][SIZE])
///pre:the function is called
///post:the check happens through the grid and the changes are made to the living and dead grids.
{
	int counter = 0;
	for (int row = 0; row<SIZE; row++)
	{
		for (int col = 0; col<SIZE; col++)
		{
			counter = 0;
			if (somearray[row][col] == true)
			{
				if (somearray[row - 1][col] == true)
				{
					if (row - 1 >= 0)
					{
						counter++;
					}
				}
				if (somearray[row + 1][col] == true)
				{
					if (row + 1 <= SIZE - 1)
					{
						counter++;
					}
				}
				if (somearray[row - 1][col - 1] == true)
				{
					if (row - 1 >= 0 && col - 1 >= 0)
					{
						counter++;
					}
				}
				if (somearray[row][col - 1] == true)
				{
					if (col - 1 >= 0)
					{
						counter++;
					}

				}
				if (somearray[row + 1][col - 1] == true)
				{
					if (row + 1 <= SIZE - 1 && col - 1 >= 0)
					{
						counter++;
					}
				}
				if (somearray[row - 1][col + 1] == true)
				{
					if (row - 1 >= 0 && col + 1 <= SIZE - 1)
					{
						counter++;
					}
				}
				if (somearray[row][col + 1] == true)
				{
					if (col + 1 <= SIZE - 1)
					{
						counter++;
					}
				}
				if (somearray[row + 1][col + 1] == true)
				{
					if (row + 1 <= SIZE - 1 && col + 1 <= SIZE - 1)
					{
						counter++;
					}
				}
				if (counter == 0 || counter == 1)
				{
					nextGen[row][col] = false;
				}
				if (counter >= 4)
				{
					nextGen[row][col] = false;
				}
			}
			if (somearray[row][col] == false)
			{
				if (somearray[row - 1][col] == true)
				{
					if (row - 1 >= 0)
					{
						counter++;
					}
				}
				if (somearray[row + 1][col] == true)
				{
					if (row + 1 <= SIZE - 1)
					{
						counter++;
					}
				}
				if (somearray[row - 1][col - 1] == true)
				{
					if (row - 1 >= 0 && col - 1 >= 0)
					{
						counter++;
					}
				}
				if (somearray[row][col - 1] == true)
				{
					if (col - 1 >= 0)
					{
						counter++;
					}
				}
				if (somearray[row + 1][col - 1] == true)
				{
					if (row + 1 <= SIZE - 1 && col - 1 >= 0)
					{
						counter++;
					}
				}
				if (somearray[row - 1][col + 1] == true)
				{
					if (row - 1 >= 0 && col + 1 <= SIZE - 1)
					{
						counter++;
					}
				}
				if (somearray[row][col + 1] == true)
				{
					if (col + 1 <= SIZE - 1)
					{
						counter++;
					}
				}
				if (somearray[row + 1][col + 1] == true)
				{
					if (row + 1 <= SIZE - 1 && col + 1 <= SIZE - 1)
					{
						counter++;
					}
				}
				if (counter == 3)
				{
					nextGen[row][col] = true;
				}
			}
		}
	}


}

///this function counts the amount of living in row 10.
int livingRowTen(/*in*/bool somearray[][SIZE])
///pre:the function is called
///post:the number is returned to the function
{
	int counting = 0;

	for (int counter = 0; counter<SIZE; counter++)
	{

		if (somearray[(9) + 1][counter] == true)
		{
			counting++;
		}

	}

	return counting;
}
///this function counts the amount of living cells in column ten
int livingColumnTen(/*in*/bool somearray[][SIZE])
///pre:the function is called
///post:the number of living cells in column ten is returned to the function call
{
	int counting = 0;

	for (int counter = 0; counter<SIZE; counter++)
	{

		if (somearray[counter][10] == true)
		{
			counting++;
		}

	}

	return counting;
}
///this function counts the dead cells in row sixteen
int deadcellsRowSixteen(/*in*/bool somearray[][SIZE])
///pre:the function is called
///post:the number of dead cells is returned to the function call.
{
	int counting = 0;

	for (int counter = 0; counter<SIZE; counter++)
	{

		if (somearray[16][counter] == false)
		{
			counting++;
		}

	}

	return counting;
}
///this function counts the dead cells in column one
int deadcellscolumnOne(/*in*/bool somearray[][SIZE])
///pre:the function is called
///post:the number of dead cells in column one is returned to the function call
{
	int counting = 0;

	for (int counter = 0; counter<SIZE; counter++)
	{

		if (somearray[counter][1] == false)
		{
			counting++;
		}

	}

	return counting;
}
///this function counts the number of living cells of the entire board
int livingEntireBoard(/*in*/bool somearray[][SIZE])
///pre:the function is called
///post:the value is returned to the function call
{
	int counting = 0;

	for (int row = 0; row<SIZE; row++)
	{
		for (int col = 0; col<SIZE; col++)
		{
			if (somearray[row][col] == true)
			{
				counting++;
			}
		}
	}

	return counting;
}
///this function counts the amount of dead cells for the entire board
int deadEntireBoard(/*in*/bool somearray[][SIZE])
///pre:the function is called
///post:the value is returned to the function call.
{
	int counting = 0;

	for (int row = 0; row<SIZE; row++)
	{
		for (int col = 0; col<SIZE; col++)
		{
			if (somearray[row][col] == false)
			{
				counting++;
			}
		}
	}

	return counting;
}