# Network medicine.

1. **Disease module.** From the disease genes, localize the disease module in the interactome. What is the size of the disease module? How is this module significant when compared to a random module? Provide a visualization of the disease module significance. Plot the subgraph formed by the disease module following the needed steps to obtain a clean image with Gephi software.

2. **Disease separation.** Work on the molecular overlap of the disease you are studying with other diseases. Chose two particular diseases: one that apparently might overlap with your disease and one that apparently might be very distant to your disease. Compute the separation in the interactome of the two disease modules. Discuss the possible implications of the separation between the two diseases.

3. **Disease - drug proximity.** Apart from the drugs that are specifically indicated for the disease you are studying, can you provide some new repurposing opportunities? Look at some of the drugs whose targets are specifically in the module of your disease and use the proximity metric to describe how near the disease and the drug are.

---

## Protein-Protein Interactions

```
Disease:  rheumatoid arthritis
Number of disease genes:  174
Number of disease genes in the PPI:  173
Number of disease genes in the LCC:  91
```

```
Full randomization
Mean:  13.293
Std:  9.861498415555316
z-score:  7.879836990839713
p-value:  3.3306690738754696e-15

Degree preserving randomization
Mean:  42.608
Std:  7.632583835111148
z-score:  6.340185846028811
p-value:  2.2948820621593313e-10
```

## Disease Separation

```
Top 3 Highest Separations:
                       Disease  Separation
917     carcinoid, goblet cell    3.010870
918  bronchial hyperreactivity    3.065217
919                   paranoia    3.673913

Top 3 Lowest Separations:
                   Disease  Separation
0     rheumatoid arthritis    0.000000
1       reperfusion injury    1.058442
2  glioblastoma multiforme    1.134503
```

## Disease - Drug Proximity

```
Drug: Alvocidib
Targets:  ['CDK2' 'CDK5' 'CDK9' 'CDK1' 'CDK6' 'EGFR' 'CDK4' 'CDK8' 'CDK7' 'PYGM'
 'PYGB' 'UGT1A1' 'ABCG2']
Proximity observed:  1.8131868131868132

Mean:  1.7808461538461542
Std:  0.03841402245431527
z-score:  0.8418972363313642
p-value:  0.3998454774250775
```

```
Drug: Diclofenac
Targets:  ['PTGS2' 'PTGS1' 'CYP2C9' 'CYP2C19' 'CYP1A2' 'CYP2C8' 'UGT2B7' 'CYP3A4'
 'CYP2B6' 'CYP2C18' 'CYP2E1' 'UGT1A3' 'UGT1A9' 'UGT2B4' 'ALOX5' 'PLA2G2A'
 'SLC22A6' 'ABCC4' 'ABCC1' 'SLC22A8' 'SLC22A11' 'SLCO1C1' 'SLCO1B1'
 'ABCB11' 'SCN4A' 'ASIC1' 'KCNQ2' 'KCNQ3' 'ABCB1' 'TTR' 'ALB']
Proximity observed:  2.0

Mean:  2.0027582417582415
Std:  0.0321285287872565
z-score:  -0.08585023536264433
p-value:  0.9315854718093619
```

```
Drug: Ibuprofen
Targets:  ['PTGS2' 'PTGS1' 'BCL2' 'THBD' 'FABP2' 'PPARG' 'CFTR' 'PPARA' 'GP1BA'
 'S100A7' 'CYP2C9' 'CYP2C8' 'CYP2C19' 'UGT1A3' 'UGT1A9' 'UGT2B4' 'UGT2B7'
 'AMACR' 'CYP3A4' 'SLCO2B1' 'ABCB1' 'ABCC4' 'ABCC1' 'SLCO1A2' 'SLC22A6'
 'SLC22A8' 'SLC22A11' 'ALB']
Proximity observed:  1.956043956043956

Mean:  1.9221868131868132
Std:  0.03027156202935583
z-score:  1.1184471691388065
p-value:  0.2633760582688518
```
