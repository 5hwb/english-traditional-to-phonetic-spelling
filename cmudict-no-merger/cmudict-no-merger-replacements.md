# Regex replacements carried out to undo the 'father-bother' vowel merger

I experimented with a couple of regular expressions to try undo the 'father-bother' vowel merger present in the American accent of the Carnegie Mellon Pronouncing Dictionary (CMUdict). This turned out to be relatively easy to find: although the pronunciation was indicated as 'AA' (as in 'far', 'bar'), the vowel in the corresponding word was still spelt as 'o'. So I started off by matching individual syllables one-by-one (e.g. 'po', 'bo', etc) like this:

* `(BOTH)(.+)B AA([012]) DH` -> `$1$2B OA$3 DH` (bother)
* `(BOT)(.+)B AA([012]) T` -> `$1$2B OA$3 T` (bottle, bottom, botany etc)
* `(PO)(.+)P AA([012])` -> `$1$2P OA$3`
* `(BO)(.+)B AA([012])` -> `$1$2B OA$3`
* `(FO)(.+)F AA([012])` -> `$1$2F OA$3`
* `(VO)(.+)V AA([012])` -> `$1$2V OA$3`

etc...

## More advanced and all-encompassing regex

Having to change the consonant in the regex replacement for each possible consonant was getting really tiring. Then I found out [in the Python documentation for their regex library](https://docs.python.org/3.6/library/re.html?highlight=regex) that it was possible to match a group within the regex lookup in the same string, which helped to simplify the process drastically.

`([PBFVMTDNKGSZJRLHWY])O(.+)\1 AA([012])` -> `$1O$2$1 OA$3`

**Explanation**:

* `([PBFVMTDNKGSZJRLHWY])O` (Group 1, `$1`) = match any one of the consonant letters 'P', 'B', 'F', 'V', 'M', 'T', 'D', 'N', 'K', 'G', 'S', 'Z', 'J', 'R', 'L', 'H', 'W' and 'Y' in the original word, provided that it precedes 'O'.
* `(.+)` (Group 2, `$2`) = match all text between the previous match and the next match.
* `\1 AA` = match `\1`, the consonant that was matched in Group 1 (`$1`), provided that it precedes 'AA'.
* `([012])` (Group 3, `$3`) = match either the number 0, 1 or 2.

For example, given the input string 'TECHNO**LOGICAL  T EH2 K N AH0 L AA1** JH IH0 K AH0 L' (the substring matched by regex is in bold):

* Group 1 (`$1`, `\1`) is 'L'
* Group 2 (`$2`) is 'GICAL  T EH2 K N AH0 '
* Group 3 (`$3`) is '1'

Plugging it into the replacement string `$1O$2$1 OA$3`, we get 'L' + 'O' + 'GICAL  T EH2 K N AH0 ' + 'L' + ' OA' + '1', resulting in the replaced string 'TECHNO**LOGICAL  T EH2 K N AH0 L OA1** JH IH0 K AH0 L'.

## Clean-up

Only issue with the previous regex was that it also replaced words that don't need to be changed. Thankfully these issues were minimal overall.

* `([PBFVMTDNKGSZJRLHWY])AR(.+)\1 OA([012]) R` -> `$1AR$2$1 AA$3 R` - find words corresponding to '*ar' but were mistakenly translated as 'OA R'
* `([PBFVMTDNKGSZJRLHWY])A(.+)\1 OA([012])` -> `$1A$2$1 AA$3` - find words corresponding to '*a' but were mistakenly translated as 'OA'. This was done manually on a case-by-case basis
