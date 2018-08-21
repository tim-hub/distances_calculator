# Distances Calculator

This is a distance calculator between 2 addressed, it is based on 
*openstreetmap* api.

## Getting start
- install, `pip install distances-calculator`
- uninstall `pip uninstall distances-calculator`

### get distance between 2 addresses
2 parameters, 

- address 1
- address 2

```
distances-calc "125 Queen St, Auckland, 0620" "127 Queen St, Auckland, 0620"
```

### calculate the distance between a table's data
2 parameters,

- address, the center, the original address
- path, the absolute path of your csv file

```
distances_writer "125 Queen St, Auckland, 0620" "/home/Username/test.csv"
```


### example of distance_writer
table test.csv

id | address
------------- | -------------
0  | 1 Fontenoy Street, Mount Albert, Auckland 1025  
1  | 3A Fontenoy Street, Mount Albert, Auckland 1025

after running `distances_writer "125 Queen St, Auckland, 0620" "/home/Username/test.csv"`

new table test.csv will be


id|address|distance_to_139 Carrington Rd, Mount Albert, Auckland 1025
------|-----|----
0  | 1 Fontenoy Street, Mount Albert, Auckland 1025| 0.447789551786935
1  | 3A Fontenoy Street, Mount Albert, Auckland 1025|0.471488332032505




#### P.S.
in your csv table, there should be one column named `address`, and the writer can create a new column named `distance_to_<address>`

## How to calculate distance
### Based on coordinate
Earth is a sphere, so we can use simple triangle function to 
calculate a not accurate distance, but most of time, 
this direct distance is good enough.

### Based on open street map api (in future)
this can be used to calculate route distance.

## APIxcode
- extract_coordinate 
- get_distance
- write_into

## Links About
- [github public repo](https://github.com/tim-hub/distance_calculator)
- [pypi distribution](https://pypi.org/project/distances-calculator/)