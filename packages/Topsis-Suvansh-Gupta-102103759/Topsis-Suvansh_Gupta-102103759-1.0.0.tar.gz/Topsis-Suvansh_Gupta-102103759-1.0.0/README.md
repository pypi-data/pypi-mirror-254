## Project description

# Topsis

for: *Project-1 (UCS633)* submitted by: *Suvansh Gupta* Roll no: 102103759 Group: *3COE27*

Topsis-Suvansh-Gupta-102103759 is a Python library for dealing with Multiple Criteria Decision Making(MCDM) problems by using Technique for Order of Preference by Similarity to Ideal Solution(TOPSIS).

## Installation

Use the package manager pip to install topsis.

```pip install Topsis-Suvansh_Gupta-102103759```

## Usage
Enter csv filename followed by .csv extentsion, then enter the weights vector with vector values separated by commas, followed by the impacts vector with comma separated signs (+,-)

```topsis sample.csv "1,1,1,1" "+,-,+,+"```
or vectors can be entered without " "

```topsis sample.csv 1,1,1,1 +,-,+,+```

But the second representation does not provide for inadvertent spaces between vector values. So, if the input string contains spaces, make sure to enclose it between double quotes (" ").

To view usage help, use

```topsis /h```

## Example

### sample.csv

A csv file showing data for different mobile handsets having varying features.

| Model | Storage (in gb)  | Camera (in MP)  | Price (in $) | Looks (out of 5) |
|-------|------------------|-----------------|--------------|------------------|
| M1    | 16               | 12              | 250          | 5                |
| M2    | 16               | 8               | 200          | 3                |
| M3    | 32               | 16              | 300          | 4                |
| M4    | 32               | 8               | 275          | 4                |
| M5    | 16               | 16              | 225          | 2                |



weights vector = [ 0.25 , 0.25 , 0.25 , 0.25 ]

impacts vector = [ + , + , - , + ]

### input:

```topsis sample.csv "0.25,0.25,0.25,0.25" "+,+,-,+"```

### output:

```
      TOPSIS RESULTS
-----------------------------

    P-Score  Rank
1  0.534277     3
2  0.308368     5
3  0.691632     1
4  0.534737     2
5  0.401046     4

```
## Other notes

The first column and first row are removed by the library before processing, in attempt to remove indices and headers. So make sure the csv follows the format as shown in sample.csv.
Make sure the csv does not contain categorical values

## License


[MIT](https://choosealicense.com/licenses/mit/)