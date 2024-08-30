import pandas as pd
from IPython.display import display

# Simpel DataFrame hvor fx "0", "Yes" er lig med 50, og "0", "No" er lig med 131.
display(pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))

dict_bob_and_sue = {'Bob': ['I liked it', 'It was awful'], 'Sue': ['Pretty good', 'Bland']}
# Vi bruger pd til at generere DataFrame objects.
# Syntaksen for at lave en Dataframe, er et dictionary hvor keys er columns,
# Og values er lister af entries
display(pd.DataFrame(dict_bob_and_sue))

# Constructor'en tildeler automatisk row labels fra index 0 og op.
# Det kan dog ændres ved at bruge "index" argumentet efter dictionary'en, som i følgende eksempel:
display(pd.DataFrame(dict_bob_and_sue, index=['Product A', 'Product B']))