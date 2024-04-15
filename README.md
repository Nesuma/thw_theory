# THW Theory (Technisches Hilfswerk Theorie Grundausbildung Anki)
TL;DR: Parser for the current Technisches Hilfswerk theory questions (basic training) into Anki flashcards.

As far as I know the up-to-date questions are currently (15.04.2024) provided in Ilias as `Aufgaben_Theorie_2022_3-4.pdf`.
This format is quite useless to learn with. 
A better alternative is the online learning website [Die Theorie](https://www.thw-theorie.de).
This even provides an offline version (which I do not want to install) and the source code (503 Service Unavailable).

Even better in my opinion are tools like [Anki](https://github.com/ankitects/anki).
This scripts creates [multiple choice](https://ankiweb.net/shared/info/1566095810) flashcards for all questions with relatively little manual preparation necessary.

## Usage
Assumes Anki installed with the [multiple choice](https://ankiweb.net/shared/info/1566095810) addon. 

1. Prepare input questions. Desired format: text file with separated values ("," and ";" are used in questions, use e.g tabulator as separator instead). 
   1. Visit each topic (Lernabschnitt) like https://www.thw-theorie.de/loesung/abschnitt-1.html
   2. Replace their tick symbols with "X" via browser developer tools for copy & pasting compatibility
      1. Open developer tools (e.g. Firefox: press F12)
      2. Execute the following command in the console: `document.body.innerHTML = document.body.innerHTML.replaceAll('<img src="img/haken.gif" width="16" height="16" alt="X">', "X")`
      3. Copy the tables (which now use "X" for correct answers) into a spreadsheet tool like Google Sheets.
   3. Once all questions of all topics are pasted into your spreadsheet (**without** any empty rows!) export the file as (my recommendation) tab-separated value file (.tsv)
2. Parse questions into an Anki compatible format by executing the python script `python3 parser.py`
   1. variables at the top of the script allow to customize input and output file names and the separator of the input file
3. Import questions into Anki
4. Enjoy learning efficiently

## Examples

### Spreadsheet format
![image](https://github.com/Nesuma/thw_theory/assets/33174209/4f8884e8-04c4-40c2-b601-466de62123ef)

### A tab-separated input file generated from the spreadsheet:
```
1.2	Wann wurde das THW gegründet?	1949	A	
		1950	B	X
		1956	C
```

### Anki flashcard
![image](https://github.com/Nesuma/thw_theory/assets/33174209/7af3eb68-0c49-4476-87f8-71fd9b458035)

## Disclaimer
I do not upload my spreadsheet, .tsv or Anki files here as they would get outdated sooner or later. 
If the format does not change significantly in future question sets, the tool could stay relevant.
