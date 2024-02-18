# TOPSIS PACKAGE - Assignment 1
I have developed a command line python program to implement the TOPSIS.
TOPSIS (technique for order performance by similarity to ideal solution) is a useful technique in dealing with multi-attribute or multi-criteria decision making (MADM/MCDM) problems in the real world
## Installation
```pip install topsis-Dev-102117160```

## Usage
Please provide the filename for the CSV, including the .csv extension. After that, enter the weights vector with values separated by commas. Following the weights vector, input the impacts vector, where each element is denoted by a plus (+) or minus (-) sign. Lastly, specify the output file name along with the .csv extension.

```py -m topsis.__main__ [input_file_name.csv] [weight as string] [impact as string] [result_file_name.csv]```

## Example Usage
The below example is for the data have 5 columns.
```py -m topsis.__main__ "C:\User\...." "1,1,2,0.5,0.75" "+,+,-,-,-" "C:\User\....."```

## Example Dataset

Fund Name | P1 | P2 | P3 | P4 | P5
------------ | ------------- | ------------ | ------------- | ------------ | ------------
M1 | 0.78 | 0.61 | 5.5 | 34.7 | 10.4
M2 | 0.88 | 0.77 | 5 | 58.4 | 16.26
M3 | 0.61 | 0.37 | 5.9 | 39.9 | 11.7
M4 | 0.76 | 0.58 | 4.2 | 57.7 | 15.81
M5 | 0.84 | 0.71 | 3.2 | 48 | 13.19
M6 | 0.76 | 0.58 | 4 | 68.8 | 18.54
M7 | 0.81 | 0.66 | 6.5 | 38.2 | 11.54
M8 | 0.81 | 0.66 | 3.2 | 32.8 | 9.37

## Output Dataset
Fund Name | P1 | P2 | P3 | P4 | P5 | TOPSIS Score | Rank
------------ | ------------- | ------------ | ------------- | ------------ | ------------ | ------------ | ------------
M1 | 0.78 | 0.61 | 5.5 | 34.7 | 10.4 | 0.5303740545041122 | 4
M2 | 0.88 | 0.77 | 5 | 58.4 | 16.26 | 0.5372510220778413 | 3
M3 | 0.61 | 0.37 | 5.9 | 39.9 | 11.7 | 0.4715707210914604 | 8
M4 | 0.76 | 0.58 | 4.2 | 57.7 | 15.81 | 0.5099483054760279 | 6
M5 | 0.84 | 0.71 | 3.2 | 48 | 13.19 | 0.57723478293325 | 1
M6 | 0.76 | 0.58 | 4 | 68.8 | 18.54 | 0.49447887833737925 | 7
M7 | 0.81 | 0.66 | 6.5 | 38.2 | 11.54 | 0.5244107252631429 | 5
M8 | 0.81 | 0.66 | 3.2 | 32.8 | 9.37 | 0.5576533672285703 | 2 

<br>

## Important Points
1) There should be only numeric columns except the first column i.e. Fund Name.
2) Input file must contain atleast three columns.

<br>

