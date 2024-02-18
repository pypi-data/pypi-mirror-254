![tucan](https://images.unsplash.com/photo-1611788542170-38cf842212f4?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

TUCAN (Tool to Unformat, Clean, ands Analyse) is a code parser for scientific codebases. It tager languages are:
- Very old FORTRAN
- Recent FORTRAN
- Python (Under development)
- C/C++ (Eazrly development)

## What is does?


### Remove Coding archaisms

First is it a code cleaner. For example, this loop in `tranfit.f' a piece of CHEMKIN package  good'old FORTRAN:

```fortran
(547)      DO 2000 K = 1, KK-1
(548)         DO 2000 J = K+1, KK
(549)            DO 2000 N = 1, NO
(550)               COFD(N,J,K) = COFD(N,K,J)
(551) 2000 CONTINUE
```

Is translated  with the command `tucan clean tranfit.f` as : 
```fortran
(547-547)        do 2000 k  =  1,kk-1
(548-548)           do 2000 j  =  k+1,kk
(549-549)              do 2000 n  =  1,no
(550-550)                 cofd(n,j,k)  =  cofd(n,k,j)
(551-551)              end do ! 2000
(551-551)           end do ! 2000
(551-551)        end do ! 2000
```



The cleaned version simplify the code for further analysis passes, like computing cyclomatic complexity, extracting structures, etc...


### Extracting code structure

On the same file `tucan struct tranfit.f` provides a nested dictionary of the code structure. Here is an exemple from a code in very recent fortran:

```yaml
type htable.h_tuple_t :
    At path ['htable', 'h_tuple_t'], name h_tuple_t, lines 47 -> 52
    6 statements over 6 lines
    Complexity 1
    Refers to 1 callables:
       - class
    Contains no inner structures
    Contains no annotations

type_public_abstract htable.htable_t :
    At path ['htable', 'htable_t'], name htable_t, lines 55 -> 64
    10 statements over 10 lines
    Complexity 1
    Refers to 2 callables:
       - pass
       - t
    Contains no inner structures
    Contains no annotations

function_pure htable.interface_abstract66.htable_hash :
    At path ['htable', 'interface_abstract66', 'htable_hash'], name htable_hash, lines 67 -> 72
    6 statements over 6 lines
    Complexity 1
    Refers to 2 callables:
       - class
       - htable_hash
    Contains no inner structures
    Contains no annotations

interface_abstract htable.interface_abstract66 :
    At path ['htable', 'interface_abstract66'], name interface_abstract66, lines 66 -> 73
    8 statements over 8 lines
    Complexity 1
    Contains no callables
    Contains 1 elements:
    - htable.interface_abstract66.htable_hash
    Contains no annotations
```

This information allows the creation and manipulation of graphs to extract the structure of the code


### Interpreting IFDEFS 

An other nasty example is the use of ìfdefs in C or FORTRAN:

```
#ifdef FRONT
        WRITE(*,*) " FRONT is enabled " ! partial front subroutine
        SUBROUTINE dummy_front(a,b,c)
        WRITE(*,*) " FRONT 1"     ! partial front subroutine
#else                
        SUBROUTINE dummy_front(a,d,e)
        WRITE(*,*) " FRONT 2"       ! partial front subroutine
#endif
        END SUBROUTINE

        SUBROUTINE dummy_back(a,b,c)
#ifdef BACK
        WRITE(*,*) " FRONT is enabled " ! partial front subroutine
        WRITE(*,*) " BACK 1"    ! partial back subroutine
        END SUBROUTINE  
#else
        WRITE(*,*) " BACK 2"    ! partial back subroutine
        END SUBROUTINE  
#endif
```

Depending on the pre-definition of variables FRONT and BACK, this code snippet can be read in four ways possible.
Here are usages:

`tucan ifdef-clean templates_ifdef.f` yields:

```fortran
        SUBROUTINE dummy_front(a,d,e)
        WRITE(*,*) " FRONT 2"       ! partial front subroutine
        END SUBROUTINE

        SUBROUTINE dummy_back(a,b,c)


        WRITE(*,*) " BACK 2"    ! partial back subroutine
        END SUBROUTINE
```


`tucan ifdef-clean templates_ifdef.f -v FRONT` yields:

```fortran
        WRITE(*,*) " FRONT is enabled " ! partial front subroutine
        SUBROUTINE dummy_front(a,b,c)
        WRITE(*,*) " FRONT 1"     ! partial front subroutine


        END SUBROUTINE

        SUBROUTINE dummy_back(a,b,c)


        WRITE(*,*) " BACK 2"    ! partial back subroutine
        END SUBROUTINE
```

`tucan ifdef-clean templates_ifdef.f -v FRONT,BACK` yields:

```fortran
         WRITE(*,*) " FRONT is enabled " ! partial front subroutine
        SUBROUTINE dummy_front(a,b,c)
        WRITE(*,*) " FRONT 1"     ! partial front subroutine


        END SUBROUTINE

        SUBROUTINE dummy_back(a,b,c)
        WRITE(*,*) " BACK is enabled " ! partial front subroutine
        WRITE(*,*) " BACK 1"    ! partial back subroutine
        END SUBROUTINE
```

## More about tucan

`Tucan` is used by  `anubis`, our open-source  tool to explore the git repository of a code, and `marauder's map`  our open-source tool to show codes structures by in-depth vizualisation of callgraphs and code circular-packing .

