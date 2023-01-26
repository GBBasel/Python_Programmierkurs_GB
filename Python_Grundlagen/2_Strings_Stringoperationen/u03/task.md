# Strings teilen

Das Teilen wird verwendet, um mehrere Zeichen (einen Unterstring) aus einem String zu erhalten.
Seine Syntax ähnelt der Indexierung, aber anstelle von nur einem Index werden zwei Indizes (Zahlen) eingesetzt
und durch einen Doppelpunkt getrennt, z. B. `str[ind1:ind2]`.

## Beispiel

```python
str[start:ende]  # Einträge von start bis ende -1
str[start:]      # Einträge von start und der ganze Rest
str[:ende]       # Einträge von start bis ende -1
str[:]           # eine Kopie des gesamten Strings
````

Übung: Verwenden Sie das Teilen, um `'Python'` von der monty_python-Variable zu erhalten.

<div class='hint'>Sie können einen der beiden Indizes leer lassen.</div>

