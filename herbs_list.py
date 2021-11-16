import pandas as pd
  
# creating dataframe
df = pd.DataFrame({'Name' : ['Basil', 'Chives', 'Cilantro', 'Dill',
                                'Mint', 'Oregano', 'Parsley', 'Rosemary', 'Sage', 'Thyme'],
                   'Latin Name' : ['Ocimum basilicum', 'Allium schoenoprasum', 'Coriandrum sativum', 'Anethum graveolens',
                                 'Mentha', 'Origanum vulgare', 'Petroselinum crispum', 'Salvia rosmarinus' 'Salvia officinalis', 'Thymus vulgaris'],
                   'Min Germination Days' : [7, 14, 7, 10, 10, 10, 14, 14, 7, 10],
                   'Max Germination Days' : [10, 21, 10, 14, 16, 15, 30, 30, 21, 14]})
df
