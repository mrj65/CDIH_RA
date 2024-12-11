# NLP

In this exercise, you will implement an NLP-based solution to extract all biological entities related to a chosen disease from text sources from the Mayo Clinic website. Follow these steps:

1. Select a disease: Using the disease provided for the above sections, navigate to the Mayo Clinic website (https://www.mayoclinic.org/) and search for the disease name to retrieve a relevant text description.

2. Entity recognition: Using NLP techniques with spaCy, identify and extract mentions of:

    - The chosen disease name
    - Symptoms associated with the disease
    - Genes, proteins, or other biological elements relevant to the disease
    - Any other biological factors (e.g., treatments)

3. Implementation requirements: Use NLP models that are compatible with spaCy for entity recognition, processing the text to detect and categorize these entities.

4. Output: Provide a list of the detected biological entities along with their categories to summarize the extracted information.

--

SYMPTOM:
  - fatigue
  - loss of appetite
  - joint stiffness
  - fever
TREATMENT:
  - steroids
  - methotrexate
DISEASE:
  - rheumatoid arthritis
GENE_PROTEIN:
  - synovium
  - antibodies
CAUSE:
  - immune system attacks healthy tissue
  - infection with certain viruses and bacteria
  - genetic component
RISK_FACTOR:
  - excess weight
  - family history
  - women
  - middle age
  - smoking
COMPLICATIONS:
  - lymphoma
  - abnormal body composition
  - lung disease
  - carpal tunnel syndrome
  - osteoporosis
  - dry eyes and mouth
  - rheumatoid nodules
  - infections
  - heart problems
