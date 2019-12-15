![walk](pix/walk.png)
### Split 
**N**ombre *五* seems a bit weird, it looks like one of the pioneers in computing,
Markov stuff, zo I've dodged it for a while and picked nombre *六*. It has a super
short description, but I couldn't find equally super simple solution: We are given
a nombre ***a***, and are asked to express integer powers of it with minimum multiplications,
[clck](https://ioinformatics.org/files/ioi1990round1.pdf). The text example for *n = 13*
can be represented as a *binary tree* as follows:
```
                        d 
        5 ==============*============== 8
1 ======*====== 4               4 ======*====== 4
            2 ==*== 2       2 ==*== 2       2 ==*== 2
          1 * 1   1 * 1   1 * 1   1 * 1   1 * 1   1 * 1
```
### (bo  o                  m                                                      )
**V**hich gives us a clue how to look for a solution, the problem is how to generate all
trees for a given *root* nombre?! In this case it seems more simple to build tree forest
the other way around from leafs to roots:
```
mysql> SHOW forest;
+---+-------+-----------+----------------+----------------------+---------------------------------+-----+
| 1 |   2   |    3      |     4          |      5               |         6                       | etc |
+---+ 1 * 1 | 1 =*= 2   | 1 ==*== 3      | 1 ===*=== 4          | 1 ======*====== 5               +-----+
    +-------+     1 * 1 |      1 =*= 2   |       1 ==*== 3      |            1 ===*=== 4          |
            +-----------+          1 * 1 |            1 =*= 2   |                  1 ==*== 3      |
                        +----------------+                1 * 1 |                       1 =*= 2   |
                        |      4         +----------------------+                           1 * 1 |
                        |   2 =*= 2      |      5               +---------------------------------+
                        | 1 * 1 1 * 1    | 1 ===*=== 4          |         6                       |
                        +----------------+        2 =*= 2       | 1 ======*====== 5               |
                                         |      1 * 1 1 * 1     |           1 ====*==== 4         |
                                         +----------------------+                    2 =*= 2      |
                                         |        5             |                  1 * 1 1 * 1    |
                                         |   2 ===*=== 3        +---------------------------------+
                                         | 1 * 1    1 =*= 2     |         6                       |
                                         |              1 * 1   | 1 ======*====== 5               |
                                         +----------------------+            2 ===*=== 3          |
                                                                |          1 * 1    1 =*= 2       | 
                                                                |                       1 * 1     |
                                                                +---------------------------------+
                                                                |        6                        |
                                                                |   2 ===*=== 4                   |
                                                                | 1 * 1   1 ==*== 3               |
                                                                |              1 =*= 2            |
                                                                |                  1 * 1          |
                                                                +---------------------------------+
                                                                |        6                        |
                                                                |   2 ===*=== 4                   |
                                                                | 1 * 1    2 =*= 2                |
                                                                |        1 * 1 1 * 1              |
                                                                +---------------------------------+
                                                                |         6                       |
                                                                |    3 ===*=== 3                  |
                                                                | 1 =*= 2   1 =*= 2               |
                                                                |     1 * 1     1 * 1             |
                                                                +---------------------------------+     
(fig 35.) He ce 4eTe
``` 
### 
**N**ow we have to figure for example why ze last *(3,3)-split* has less multiplications than the first
*(1,5)-split* for the *6-rooted* forest *(fig 35.)**?*** For every tree we have a corresponding set of
nodes: In the above example the corresponding sets are *{ 1,2,3,6 }* and *{ 1,2,3,4,5,6 }* respectively.
So the *(3,3)-split* has less multiplications because the corresponding set has the lesser cardinality.
One of the problems of this approach is that the following ***Python*** code:
```Python
def split(n): 
    for j in range(n >> 1, 0, -1): 
    	split(j) 
	split(n - j) 
```
will start running forever after *n* around *23*. One possible workaround is to realize that for
even nombres, we don't need to ck all splits but only the last symmetric *(n/2,n/2)* split which
will roughly double nombres' range.

https://youtu.be/BEM-9mPe120