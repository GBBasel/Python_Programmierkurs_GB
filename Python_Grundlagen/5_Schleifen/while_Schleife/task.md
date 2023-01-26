# Schleifen

Computer sind entwickelt worden, um die immer gleichen Sachen in hoher Geschwindigkeit stetig zu wiederholen.
Wiederholende Prozesse werden im Rahmen einer technischen Umsetzung als Schleifenoperationen betrachtet.
Aus der Sicht von Python gibt es zwei unterschiedliche Möglichkeiten:
- Die `for` Schleife für eine zu Schleifenbeginn bekannte und definierte Anzahl von Durchläufen.
- Die `while` Schleife für Konstrukte bei denen in jedem Durchgang eine Weiterführung geprüft wird. 

# Die while Schleife
Eine `while` Schleife wiederholt einen Codeblock solange die Weiterführungsbedingung `True` ist.
Die `while` Schleife besteht aus den zwei folgenden Strukturelementen:

1. Das `while` Schlüsselwort gefolgt von einer booleschen Testbedingung, welches am Ende mit einem 
Doppelpunkt `:` abgeschlossen wird.
2. Dem Schleifenkörper, in welchem der ausführbare Code hinterlegt wird (Einrückung nicht vergessen).

Bei der Ausführung einer `while` Schleife wird bei jeder Durchführung die boolesche Testbedingung geprüft.
Bei einer positiven Antwort erfolgt die Abarbeitung des Schleifenkörpers, bei einer negativen Antwort wird 
die Schleife verlassen und der Code nach dem Schleifenkörper ausgeführt.


