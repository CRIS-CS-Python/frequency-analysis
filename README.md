# Frequency Analysis

We will create a program that

* reads a text file from a path given on the command line.
* counts only the **letters and numbers** in the text file.
  Letters should be converted to upper case.
* prints a frequency table (called a **histogram**) in reverse order
  (from most frequent to least) containing `freq<tab>character<tab>percentage`
  where
  - *freq* is the frequency of occurence for a character (count how many times that character occurs in the file).
  - *character* is each unique character
  - *percentage* the percentage of the freq to the total.

The starter code in `count_characters.py` check proper command line usage
and opens the text file, but you will need to implement the code
that counts the frequencies and prints the histogram.

## Brown Corpus

This repository contains a file `brown.txt` which contains the
[Brown Corpus](https://en.wikipedia.org/wiki/Brown_Corpus), a large English
language document that contains text from a well balance set of categories.
It is especially used for the "scientific study of the frequency and
distribution of word categories in everyday language use."

The file was fetched from [here](http://www.sls.hawaii.edu/bley-vroman/brown.txt).

## Usage & Output

You can test it with any text file, but a correct program will analyze
`brown.txt` to produce the following output.

```
$ py count_characters.py brown.txt
592982  E       0.12433649370089686
438979  T       0.09204513740438328
381728  A       0.08004074502675622
360310  O       0.07554981777755505
345777  I       0.07250253765277026
336729  N       0.07060535258643483
310710  S       0.06514968744043777
290953  R       0.061007038749501745
258019  H       0.05410143607767472
196168  L       0.04113251548329888
188251  D       0.03947247855025538
147237  C       0.030872661097704403
128805  U       0.02700783846920146
120667  M       0.025301462245744595
110706  F       0.023212839296389245
95951   P       0.020119010201143973
92531   G       0.019401904439995964
89151   W       0.01869318588073273
81735   Y       0.017138198651296
72822   B       0.015269320391321678
47272   V       0.00991199518742356
31188   K       0.006539501309556734
9439    X       0.0019791699647590745
7640    J       0.0016019555599914533
5217    1       0.001093900805821389
5103    Q       0.0010699972804497889
4516    Z       0.0009469150927907597
4473    0       0.0009378988507646297
2690    2       0.0005640393267509175
2186    5       0.0004583605830027902
2134    9       0.0004474572205525866
1778    3       0.00037281112377811576
1491    4       0.0003126329502548766
1467    6       0.00030760062912401335
1289    8       0.0002702775807367779
1077    7       0.0002258254107474863
Total characters: 4769171
```