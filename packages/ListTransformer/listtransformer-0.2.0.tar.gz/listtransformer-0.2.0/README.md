# ListTransformer
## Installation
``pip install ListTransformer``

## Examples

````py
import ListTransformer

liste = ListTransformer.lister("123 123 123")
print(liste)
print(ListTransformer.str_list(liste))
````

### lister
Converts strings to lists.

- (required) str_list: ```str``` the text to convert to list
- (optional) typ: ``lister.Typ`` the method for example comma or space, default is that it is selected automatically  
  - Attributes ```ListTransformer.Typ.auto, ListTransformer.Typ.comma, ListTransformer.Typ.space``` the input format

#### Example

````py
import ListTransformer

print(ListTransformer.lister("123 123 123"))
print(ListTransformer.lister("123, 123, 123"))
````
#### Outputs:
``['123', '123', '123']`` as ``list``  
``['123', '123', '123']`` as ``list``

### str_list
Convert lists to strings.

- (required) list: ``list`` The list to be converted into a string
- (optional) split: ``lister.Splits`` The way in which the string should separate the entries  
  - Attributes ```ListTransformer.Splits.space, ListTransformer.Splits.comma``` the output format

#### Example

````py
import ListTransformer

liste = ["test1", "test2", "test3"]

print(ListTransformer.str_list(liste))
print(ListTransformer.str_list(liste, ListTransformer.Splits.space))
````
#### Outputs:
``test1, test2, test3`` as ``string``  
``test1 test2 test3`` as ``string``

### difference
Shows the differences between two lists.
- (required) list1: ``list`` The first list.
- (required) list2: ``list`` The secend list.
  - Attributes ```ListTransformer.Tools.same, ListTransformer.Typ.no_same``` The type whether entries should occur twice.

#### Example

````py
import ListTransformer

print(ListTransformer.difference([1, 2, 3], [1, 2, 3, 4, 5, 5]))
print(ListTransformer.difference([1, 2, 3], [1, 2, 3, 4, 5, 5], ListTransformer.Tools.no_same))
````
#### Outputs:
``[4, 5, 5]`` as ``list``
``[4, 5]`` as ``list``

### intersection
Shows the entries that are the same.

- (required) list1: ``list`` The first list.
- (required) list2: ``list`` The secend list.
  - Attributes ```ListTransformer.Tools.same, ListTransformer.Typ.no_same``` The type whether entries should occur twice.

#### Example

````py
import ListTransformer

print(ListTransformer.intersection([1, 2, 3, 3], [1, 2, 3, 3, 4, 5]))
print(ListTransformer.intersection([1, 2, 3, 3], [1, 2, 3, 3, 4, 5], ListTransformer.Tools.no_same))
````
#### Outputs:
``[1, 2, 3, 3]`` as ``list``  
``[1, 2, 3]`` as ``list``

### combine
returns the two lists combined into one.

- (required) list1: ``list`` The first list.
- (required) list2: ``list`` The secend list.
  - Attributes ```ListTransformer.Tools.same, ListTransformer.Typ.no_same``` The type whether entries should occur twice.

#### Example

````py
import ListTransformer

print(ListTransformer.combine([1, 2, 3], [4, 5, 6, 6]))

print(ListTransformer.combine([1, 2, 3], [4, 5, 6, 6], ListTransformer.Tools.no_same))
````
#### Outputs:
``[1, 2, 3, 4, 5, 6, 6]`` as ``list``  
``[1, 2, 3, 4, 5, 6]`` as ``list``