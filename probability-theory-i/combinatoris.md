# Kombinatorik

[Stochastik Formeln](http://www.brefeld.homepage.t-online.de/stochastik-formeln.html)

## Aufeinanderfolgende Zahlen bei Lotto

**Gegeben:**
- Ohne Zurücklegen und ohne Reihenfolge
- Ziehe $n$ mal bei einer Anzahl von $N$ Kugeln in der Urne

**Gesucht:** Wie groß ist die Wahrscheinlichkeit, keine aufeinanderfolgende Zahl zu ziehen? 

**Bespiel:** Sei $n=3$ und $N=7$. Dann ist $\{1,3,5\}$ gültig, aber nicht $\{ 1,2,5 \}$.

**Formel:** 

$$
    \frac{\binom{N-n+1}{n}}{\binom{N}{n}}
$$

**Erklärung:** Zieht man $n$ Kugeln, so hat man $N-n$ Kugeln nicht gezogen. Die $n$ gezogenen Kugeln möchte man zwischen den $N-n$ nichtgezogenen Kugeln platzieren; erst diese Platzierung bestimmt die Nummer der gezogenen Kugel. 

```
N = 7, n = 3

... [ ] ... [ ] ... [ ] ... [ ] ...
```

Die eckigen Klammern ```[ ]``` symbolsieren die nichtgezogenen Kugeln und ```...``` die Platzhalter, wo man die gezogene Kugeln platzieren könnte. Hier ein Beispiel für drei vollständige Ziehungen

```
N = 7, n = 3

... [ ] (o) [ ] (o) [ ] ... [ ] (o)
     1   2   3   4   5       6   7
```

Das bedeutet, man hat $\{2,4,7\}$ gezogen. Jede dieser Konfigurationen ist günstig für unser Experiment! Da man $N-n$ nichtgezogene Kugeln hat und dementsprechend $N-n+1$ Plätze zwischen diesen Kugeln, gibt es insgesamt $\binom{N-n+1}{n}$ Möglichkeiten, $n$ Kugeln auf diese Plätze zu verteilen-

