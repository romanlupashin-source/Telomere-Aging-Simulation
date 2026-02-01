# Telomere Aging Simulation 

This project simulates telomere dynamics during cell division and compares
normal somatic cells with cancer cells exhibiting telomerase activity.

The model demonstrates key biological principles behind cellular aging
and replicative immortality.

---

## Scientific Background

Telomeres are repetitive DNA sequences that shorten with each cell division.
When telomeres reach a critical length (Hayflick limit), the cell enters
senescence or apoptosis.

Cancer cells bypass this limitation by activating **telomerase**, allowing
them to maintain telomere length and divide indefinitely.

---

## Simulation Overview

The simulation models:
- Telomere shortening in normal somatic cells
- Telomere maintenance in cancer cells
- The Hayflick limit as a biological death threshold

---

## Output

The script produces a comparative plot showing:
- Progressive telomere loss in normal cells
- Stable or increasing telomere length in cancer cells
- The Hayflick limit as a reference line

---

## Technologies Used

- Python 3.9+
- Matplotlib
- Random-based stochastic modeling

---

## Usage

Install dependencies:

```bash
pip install -r requirements.txt

