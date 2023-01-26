# Boolsche Operatoren
*Tipp: In folgenden Theorieteilen sehen Sie im mittleren Teil viel Pythoncode. Führen Sie diesen aus, um die Ausgabe im Terminal zu interpretieren. Durch mehrzeilige Kommentare ('''code''') können Abschnitte ignoriert werden.*

In den vorhergehenden Kapiteln bestand der betrachtete Pythoncode aus einer
linearen Aneinanderreihung von Codezeilen. Mit Hilfe der booleschen Operatoren
besteht die Möglichkeit, den Pythoncode in Abhängigkeit von Fragestellungen
gezielt zu steuern.  

Das Resultat einer booleschen Operation erfolgt stehts in einer binären Form als
`True` oder `False`.

## Vergleichsoperatoren
Die Vergleichsoperatoren dienen der Umwandlung von Abfragetermen mit
einem grossen Werteraum in die zwei Zustände `True` oder `False`.
Die nachfolgende Liste beschreibt die wichtigsten Vergleichsoperatoren welche
in Python zur Verfügung stehen:

<table>
  <tr>
    <th>Vergleichsoperator</th>
    <th>Beispiel</th>
    <th>Bedeutung</th>
  </tr>
  <tr>
    <td><</td>
    <td>a < b</td>
    <td>a ist kleiner als b</td>
  </tr>
    <td>></td>
    <td>a > b</td>
    <td>a ist grösser als b</td>
  </tr>
    <td><=</td>
    <td>a <= b</td>
    <td>a ist kleiner gleich b</td>
  </tr>
    <td>!=</td>
    <td>a != b</td>
    <td>a ist ungleich b</td>
  </tr>
    <td>==</td>
    <td>a == b</td>
    <td>a ist gleich b</td>
  </tr>
</table>

**Hinweis**:  
Ein häufiger Programmierfehler besteht darin, dass bei einem Vergleich auf
Gleichheit nur ein einzelnes Gleichheitszeichen `=` eingesetzt wird. Im Gegensatz
zur mathematischen Gleichheit sind bei einem logischen Vergleich in Python zwei 
Gleichheitszeichen `==` zu verwenden.

## Logische Operatoren
Für die logische Verknüpfung von booleschen Datentypen können die logischen Operatoren
eingesetzt werden. Die drei wichtigsten lauten:
- and
- or
- not

Die dazugehörigen Wertetabellen lauten:  

---
**and** (Maximalfunktion)  
**x = a and b**
<table>
  <tr>
    <th>a</th>
    <th>b</th>
    <th>x</th>
  </tr>
  <tr>
    <td>False</td>
    <td>False</td>
    <td>False</td>
  </tr>
  <tr>
    <td>False</td>
    <td>True</td>
    <td>False</td>
  </tr>
  <tr>
    <td>True</td>
    <td>False</td>
    <td>False</td>
  </tr>
  <tr>
    <td>True</td>
    <td>True</td>
    <td>True</td>
  </tr>
</table>

---
**or** (Minimalfunktion)  
**x = a or b**
<table>
  <tr>
    <th>a</th>
    <th>b</th>
    <th>x</th>
  </tr>
  <tr>
    <td>False</td>
    <td>False</td>
    <td>False</td>
  </tr>
  <tr>
    <td>False</td>
    <td>True</td>
    <td>True</td>
  </tr>
  <tr>
    <td>True</td>
    <td>False</td>
    <td>True</td>
  </tr>
  <tr>
    <td>True</td>
    <td>True</td>
    <td>True</td>
  </tr>
</table>

---
**not** (Invertierung)  
**x = not a**
<table>
  <tr>
    <th>a</th>
    <th>x</th>
  </tr>
  <tr>
    <td>False</td>
    <td>True</td>
  </tr>
  <tr>
    <td>True</td>
    <td>False</td>
  </tr>
</table>

---