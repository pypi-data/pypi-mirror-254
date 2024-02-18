## Introduction

TOPSIS (technique for order performance by similarity to ideal solution) is a useful technique in dealing with multi-attribute or multi-criteria decision making (MADM/MCDM) problems in the real world.

## Installation
Use the package manager pip to install.

```pip install topsis-102103357```

## Usage
Enter csv filename followed by .csv extentsion, then enter the weights vector with vector values separated by commas, followed by the impacts vector with comma separated signs (+,-) and enter the output file name followed by .csv extension.

```topsis-102103357 [InputDataFile as .csv] [Weights as a string] [Impacts as a string] [ResultFileName as .csv]```

## Sample Input

| Fund Name| P1	  | P2	 | P3  | P4	  | P5    |
|----------|------|------|-----|------|-------|
| M1	   | 0.84 |	0.71 | 6.7 | 42.1 |	12.59 |
| M2	   | 0.91 |	0.83 | 7   | 31.7 |	10.11 |
| M3	   | 0.79 |	0.62 | 4.8 | 46.7 |	13.23 |
| M4	   | 0.78 |	0.61 | 6.4 | 42.4 |	12.55 |
| M5	   | 0.94 |	0.88 | 3.6 | 62.2 | 16.91 |
| M6	   | 0.88 | 0.77 | 6.5 | 51.5 | 14.91 |
| M7	   | 0.66 | 0.44 | 5.3 | 48.9 | 13.83 |
| M8	   | 0.93 | 0.86 | 3.4 | 37   | 10.55 |

```topsis-102103357 data.csv "1,1,1,1,1" "+,-,+,-,+" output.csv```

## Sample Output

Results saved to output.csv

| Fund Name| P1	  | P2	 | P3  | P4	  | P5    |     Performance   | Rank |
|----------|------|------|-----|------|-------|-------------------|------|
| M1	   | 0.84 |	0.71 | 6.7 | 42.1 |	12.59 | 0.404268469809145 | 5.0  |
| M2	   | 0.91 |	0.83 | 7   | 31.7 |	10.11 | 0.699297825503612 | 1.0  |
| M3	   | 0.79 |	0.62 | 4.8 | 46.7 |	13.23 | 0.333581741928051 | 8.0  |
| M4	   | 0.78 |	0.61 | 6.4 | 42.4 |	12.55 | 0.364968017290041 | 6.0  |
| M5	   | 0.94 |	0.88 | 3.6 | 62.2 | 16.91 | 0.534831688649816 | 2.0  |
| M6	   | 0.88 | 0.77 | 6.5 | 51.5 | 14.91 | 0.439693012540145 | 4.0  |
| M7	   | 0.66 | 0.44 | 5.3 | 48.9 | 13.83 | 0.526356720373482 | 3.0  |
| M8	   | 0.93 | 0.86 | 3.4 | 37   | 10.55 | 0.341972356097968 | 7.0  |

The best model is M2

## License

This repository is licensed under the MIT license. See LICENSE for details.