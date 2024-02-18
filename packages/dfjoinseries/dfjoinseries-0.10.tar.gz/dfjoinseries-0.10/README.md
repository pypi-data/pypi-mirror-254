# Like numpy.char.join for DataFrames
 
## Tested against Windows / Python 3.11 / Anaconda

## pip install dfjoinseries

```
import pandas as pd
from dfjoinseries import pd_add_str_tools
pd_add_str_tools()
df = pd.read_csv(
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
)

df2 = df.d_to_str()
df3 = df.d_to_repr()
df4 = df2.d_join(sep=" --- ")
df5 = df3.d_join()
print(df)
print(df2)
print(df3)
print(df4)
print(df5)

#      PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
# 0              1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
# 1              2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
# 2              3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
# 3              4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
# 4              5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
# ..           ...       ...     ...                                                ...     ...   ...    ...    ...               ...      ...   ...      ...
# 886          887         0       2                              Montvila, Rev. Juozas    male  27.0      0      0            211536  13.0000   NaN        S
# 887          888         1       1                       Graham, Miss. Margaret Edith  female  19.0      0      0            112053  30.0000   B42        S
# 888          889         0       3           Johnston, Miss. Catherine Helen "Carrie"  female   NaN      1      2        W./C. 6607  23.4500   NaN        S
# 889          890         1       1                              Behr, Mr. Karl Howell    male  26.0      0      0            111369  30.0000  C148        C
# 890          891         0       3                                Dooley, Mr. Patrick    male  32.0      0      0            370376   7.7500   NaN        Q

# [891 rows x 12 columns]
#     PassengerId Survived Pclass                                               Name     Sex   Age SibSp Parch            Ticket     Fare Cabin Embarked
# 0             1        0      3                            Braund, Mr. Owen Harris    male  22.0     1     0         A/5 21171     7.25   nan        S
# 1             2        1      1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0     1     0          PC 17599  71.2833   C85        C
# 2             3        1      3                             Heikkinen, Miss. Laina  female  26.0     0     0  STON/O2. 3101282    7.925   nan        S
# 3             4        1      1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0     1     0            113803     53.1  C123        S
# 4             5        0      3                           Allen, Mr. William Henry    male  35.0     0     0            373450     8.05   nan        S
# ..          ...      ...    ...                                                ...     ...   ...   ...   ...               ...      ...   ...      ...
# 886         887        0      2                              Montvila, Rev. Juozas    male  27.0     0     0            211536     13.0   nan        S
# 887         888        1      1                       Graham, Miss. Margaret Edith  female  19.0     0     0            112053     30.0   B42        S
# 888         889        0      3           Johnston, Miss. Catherine Helen "Carrie"  female   nan     1     2        W./C. 6607    23.45   nan        S
# 889         890        1      1                              Behr, Mr. Karl Howell    male  26.0     0     0            111369     30.0  C148        C
# 890         891        0      3                                Dooley, Mr. Patrick    male  32.0     0     0            370376     7.75   nan        Q

# [891 rows x 12 columns]
#     PassengerId Survived Pclass                                               Name       Sex   Age SibSp Parch              Ticket     Fare   Cabin Embarked
# 0             1        0      3                          'Braund, Mr. Owen Harris'    'male'  22.0     1     0         'A/5 21171'     7.25     nan      'S'
# 1             2        1      1  'Cumings, Mrs. John Bradley (Florence Briggs T...  'female'  38.0     1     0          'PC 17599'  71.2833   'C85'      'C'
# 2             3        1      3                           'Heikkinen, Miss. Laina'  'female'  26.0     0     0  'STON/O2. 3101282'    7.925     nan      'S'
# 3             4        1      1     'Futrelle, Mrs. Jacques Heath (Lily May Peel)'  'female'  35.0     1     0            '113803'     53.1  'C123'      'S'
# 4             5        0      3                         'Allen, Mr. William Henry'    'male'  35.0     0     0            '373450'     8.05     nan      'S'
# ..          ...      ...    ...                                                ...       ...   ...   ...   ...                 ...      ...     ...      ...
# 886         887        0      2                            'Montvila, Rev. Juozas'    'male'  27.0     0     0            '211536'     13.0     nan      'S'
# 887         888        1      1                     'Graham, Miss. Margaret Edith'  'female'  19.0     0     0            '112053'     30.0   'B42'      'S'
# 888         889        0      3         'Johnston, Miss. Catherine Helen "Carrie"'  'female'   nan     1     2        'W./C. 6607'    23.45     nan      'S'
# 889         890        1      1                            'Behr, Mr. Karl Howell'    'male'  26.0     0     0            '111369'     30.0  'C148'      'C'
# 890         891        0      3                              'Dooley, Mr. Patrick'    'male'  32.0     0     0            '370376'     7.75     nan      'Q'

# [891 rows x 12 columns]
# 0      1 --- 0 --- 3 --- Braund, Mr. Owen Harris --- ...
# 1      2 --- 1 --- 1 --- Cumings, Mrs. John Bradley (...
# 2      3 --- 1 --- 3 --- Heikkinen, Miss. Laina --- f...
# 3      4 --- 1 --- 1 --- Futrelle, Mrs. Jacques Heath...
# 4      5 --- 0 --- 3 --- Allen, Mr. William Henry ---...
#                              ...
# 886    887 --- 0 --- 2 --- Montvila, Rev. Juozas --- ...
# 887    888 --- 1 --- 1 --- Graham, Miss. Margaret Edi...
# 888    889 --- 0 --- 3 --- Johnston, Miss. Catherine ...
# 889    890 --- 1 --- 1 --- Behr, Mr. Karl Howell --- ...
# 890    891 --- 0 --- 3 --- Dooley, Mr. Patrick --- ma...
# Length: 891, dtype: object
# 0      103'Braund, Mr. Owen Harris''male'22.010'A/5 2...
# 1      211'Cumings, Mrs. John Bradley (Florence Brigg...
# 2      313'Heikkinen, Miss. Laina''female'26.000'STON...
# 3      411'Futrelle, Mrs. Jacques Heath (Lily May Pee...
# 4      503'Allen, Mr. William Henry''male'35.000'3734...
#                              ...
# 886    88702'Montvila, Rev. Juozas''male'27.000'21153...
# 887    88811'Graham, Miss. Margaret Edith''female'19....
# 888    88903'Johnston, Miss. Catherine Helen "Carrie"...
# 889    89011'Behr, Mr. Karl Howell''male'26.000'11136...
# 890    89103'Dooley, Mr. Patrick''male'32.000'370376'...
# Length: 891, dtype: object


```
