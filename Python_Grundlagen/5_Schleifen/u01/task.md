# for Schleife

`for` Schleifen werden verwendet, um über eine bestimmte Sequenz zu iterieren.  
Bei jeder Iteration wird die im `for` Loop definierte Variable dem nächsten Wert in der Liste zugeordnet.
  
Mit dem Schlüsselwort `range(start, stopp, schrittweite)` wird eine Iterationsliste erzeugt. Zu beachten 
gilt es, dass die Iteration mit `stopp - 1` endet.   
z. B. `range(0, 5, 1)` führt zu den Iterationsdurchgängen => `0, 1, 2, 3, 4` ohne die 5.

Bei der Iteration über eine Liste bietet Python das Schlüsselwort `in`. Dies vereinfacht die
Zuweisung der Iterationschritte auf ein Minimum.

Übung: Geben Sie jede Primzahl aus der `primzahlen` Liste mit einem `for` Loop aus.

<div class='hint'>
    len(primzahlen) ergibt die aktuelle Länge der Liste.
    <br>Oder "for element in list" iteriert über alle Elemente der Liste (temporäre Variable "element" mit dem aktuellen Listenelement, welche im Schleifenrumpf genutzt werden kann).
</div>

