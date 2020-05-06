# Wahrscheinlichkeitstheorie I

## Woche 01

## Woche 02

### 2.1 Bedingte Wahrscheinlichkeiten und Unabhängigkeit

Für das gesamte Kapitel sei $(\Omega, p)$ ein diskreter Wahrscheinlichkeitaraum.

**Definition (Bedingte Wahrscheinlichkeit):** 
Wahrscheinlichkeit, dass $A$ eintrifft, wenn $B$ gegeben ist: $P(A|B) = \frac{P(A \cap B)}{P(B)}$

### 2.2 Unabhängigkeiten von Ereignissen

**Definition (Unabhängigkeit):**

* Zwei Ereignisse $A$ und $B$ heißen unabhängig, wenn $P(A \cap B) = P(A) P(B)$.
* Eine Familie von Ereignissen $(A_i)_{i \in I}$ (wobei $I$ eine beliebige Indexmenge ist) heißt unabhängig, falls für ___jede endliche___ Teilmenge $J \subset I$ gilt, dass $P(\bigcap_{i \in J}A_i) = \prod_{i \in J}P(A_i)$.