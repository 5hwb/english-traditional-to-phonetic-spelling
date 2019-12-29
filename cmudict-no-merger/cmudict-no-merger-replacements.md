# Regex replacements carried out to undo the father-bother merger

* `(BOT)(.+)B AA([012]) DH` -> `$1$2B OA$3 DH` (bother)
* `(BOT)(.+)B AA([012]) T` -> `$1$2B OA$3 T` (bottle, bottom, botany etc)
* `(PO)(.+)P AA([012])` -> `$1$2P OA$3`
* `(BO)(.+)B AA([012])` -> `$1$2B OA$3`
* `(FO)(.+)F AA([012])` -> `$1$2F OA$3`
* `(VO)(.+)V AA([012])` -> `$1$2V OA$3`
