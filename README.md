# Tipcc Suite

Designed to work with tip.cc cryptocurrency bot.

Uses the PyAutoGui library.

This project contains 3 different programs: MissingCoins, Phrasedrops, and TipBals.


## **MissingCoins**

### Calculates the missing coins needed to collect all available coins supported by the tip.cc wallet (295 coins supported in this version).

Type `$bals noembed` or `$bals top noembed` to the tip.cc bot.

Copy and paste your portfolio into the check_mine.txt file. 

The format should be like: `Ethereum: :ETH: 0.000295 ETH (≈ $14023.82) for coins` for coins with value or `Cheddar: :CHEDR: 0.0000000068 CHEDR` for coins with no value (no additional change needed).

The currencies that come in check_all.txt might not be up to date when program is used, so update the file by typing `$currencies`.

Copy and paste all the currencies and pasting it into check_all.txt. They should be in the format `:BSV: Bitcoin SV (BSV)` or `:BTC: Bitcoin (BTC)`.

Now, head over to check.py and run the code. 

For the final result, check in the check_missing.txt file.


## **Phrasedrops**

### Helps do confusing and long phrasedrops as tip.cc does not allow copy and paste. Especially useful when the phrasedrops are combinations of | (vertical bar), l (lowercase L), and/or I (capitalcase i).

Run phrasedrop.py.

Enter the phrase. 

Move cursor to Discord message box. 

Watch the program regurgitate the phrase. 

## **TipBals**

### Designed to tip another Discord user a portion or an entire crypto portfolio without having to manually type in the commands one at a time.

Type `$bals noembed` or `$bals top noembed` to the tip.cc bot.

Copy the coins that you wish to tip another account and paste it into tip.txt (check *MissingCoins* for the format).

Go to the tip.py file and replace the discord tag `person#4567` with the tag of the person receiving crypto in the line `person = "@person#4567"`.

Run the program.

Go to the tipcc bot and move the cursor to the Discord message box.
