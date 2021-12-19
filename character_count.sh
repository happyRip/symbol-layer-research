#!/bin/bash

# sources:
# - https://askubuntu.com/questions/593383/how-to-count-occurrences-of-each-character

cat $1 |
shuf -n 10000 |
sed 's/\(.\)/\1\n/g' |
sort |
uniq -ic |
sort -rnk 1 |
grep -vP '[\t ]$' |
awk '{$1=$1};1'
