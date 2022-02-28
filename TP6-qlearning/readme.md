# Trace Epsilon-Greedy
```
[[ 0.  2.  2.]
 [10.  0.  2.]
 [ 2.  0.  0.]]
tresor position: (array([1]), array([0]))
starting position :  (2, 1)

neighbors : [(2, 0), (2, 2), (1, 1), (3, 1)]
sorted neighbors : [(2, 0), (2, 2), (1, 1)]
random_value : 1
move to : (2, 2)

neighbors : [(2, 1), (2, 3), (1, 2), (3, 2)]
sorted neighbors : [(2, 1), (1, 2)]
random_value : 1
move to : (1, 2)

neighbors : [(1, 1), (1, 3), (0, 2), (2, 2)]
sorted neighbors : [(1, 1), (0, 2), (2, 2)]
random_value : 2
move to : (2, 2)

neighbors : [(2, 1), (2, 3), (1, 2), (3, 2)]
sorted neighbors : [(2, 1), (1, 2)]
random_value : 1
move to : (1, 2)

neighbors : [(1, 1), (1, 3), (0, 2), (2, 2)]
sorted neighbors : [(1, 1), (0, 2), (2, 2)]
random_value : 2
move to : (2, 2)

neighbors : [(2, 1), (2, 3), (1, 2), (3, 2)]
sorted neighbors : [(2, 1), (1, 2)]
random_value : 1
move to : (1, 2)

neighbors : [(1, 1), (1, 3), (0, 2), (2, 2)]
sorted neighbors : [(1, 1), (0, 2), (2, 2)]
random_value : 1
move to : (0, 2)

neighbors : [(0, 1), (0, 3), (-1, 2), (1, 2)]
sorted neighbors : [(0, 1), (1, 2)]
random_value : 1
move to : (1, 2)

neighbors : [(1, 1), (1, 3), (0, 2), (2, 2)]
sorted neighbors : [(1, 1), (0, 2), (2, 2)]
random_value : 0
move to : (1, 1)

neighbors : [(1, 0), (1, 2), (0, 1), (2, 1)]
sorted neighbors : [(1, 0), (1, 2), (0, 1), (2, 1)]
random_value : 1
move to : (1, 2)

neighbors : [(1, 1), (1, 3), (0, 2), (2, 2)]
sorted neighbors : [(1, 1), (0, 2), (2, 2)]
random_value : 2
move to : (2, 2)

neighbors : [(2, 1), (2, 3), (1, 2), (3, 2)]
sorted neighbors : [(2, 1), (1, 2)]
random_value : 1
move to : (1, 2)

neighbors : [(1, 1), (1, 3), (0, 2), (2, 2)]
sorted neighbors : [(1, 1), (0, 2), (2, 2)]
random_value : 1
move to : (0, 2)

neighbors : [(0, 1), (0, 3), (-1, 2), (1, 2)]
sorted neighbors : [(0, 1), (1, 2)]
random_value : 1
move to : (1, 2)

neighbors : [(1, 1), (1, 3), (0, 2), (2, 2)]
sorted neighbors : [(1, 1), (0, 2), (2, 2)]
random_value : 0
move to : (1, 1)

neighbors : [(1, 0), (1, 2), (0, 1), (2, 1)]
sorted neighbors : [(1, 0), (1, 2), (0, 1), (2, 1)]
random_value : 3
move to : (2, 1)

neighbors : [(2, 0), (2, 2), (1, 1), (3, 1)]
sorted neighbors : [(2, 0), (2, 2), (1, 1)]
random_value : 0
move to : (2, 0)

neighbors : [(2, -1), (2, 1), (1, 0), (3, 0)]
sorted neighbors : [(2, 1), (1, 0)]
random_value : 1
move to : (1, 0)

tresor found !!!
```

# Trace Q learning

```
[[ 0.  0.  0.]
 [10.  0.  2.]
 [ 2.  0.  0.]]
tresor position: (array([1]), array([0]))
Epsiode n° 0
initial state :  (1, 0)
initial action :  3
Epsiode n° 1
initial state :  (1, 0)
initial action :  2
Epsiode n° 2
initial state :  (1, 0)
initial action :  1
Epsiode n° 3
initial state :  (1, 0)
initial action :  3
Epsiode n° 4
initial state :  (1, 0)
initial action :  0
Epsiode n° 5
initial state :  (1, 0)
initial action :  0
Epsiode n° 6
initial state :  (1, 0)
initial action :  3
Epsiode n° 7
initial state :  (1, 0)
initial action :  2
Epsiode n° 8
initial state :  (1, 0)
initial action :  3
Epsiode n° 9
initial state :  (1, 0)
initial action :  0
Epsiode n° 10
initial state :  (1, 0)
initial action :  1
Epsiode n° 11
initial state :  (1, 0)
initial action :  3
Epsiode n° 12
initial state :  (1, 0)
initial action :  2
Epsiode n° 13
initial state :  (1, 0)
initial action :  2
Epsiode n° 14
initial state :  (1, 0)
initial action :  2
Epsiode n° 15
initial state :  (1, 0)
initial action :  3
Epsiode n° 16
initial state :  (1, 0)
initial action :  1
Epsiode n° 17
initial state :  (1, 0)
initial action :  1
Epsiode n° 18
initial state :  (1, 0)
initial action :  2
Epsiode n° 19
initial state :  (1, 0)
initial action :  1
Epsiode n° 20
initial state :  (1, 0)
initial action :  0
Epsiode n° 21
initial state :  (1, 0)
initial action :  3
Epsiode n° 22
initial state :  (1, 0)
initial action :  1
Epsiode n° 23
initial state :  (1, 0)
initial action :  1
Epsiode n° 24
initial state :  (1, 0)
initial action :  2
Epsiode n° 25
initial state :  (1, 0)
initial action :  3
Epsiode n° 26
initial state :  (1, 0)
initial action :  2
Epsiode n° 27
initial state :  (1, 0)
initial action :  0
Epsiode n° 28
initial state :  (1, 0)
initial action :  0
Epsiode n° 29
initial state :  (1, 0)
initial action :  2
Epsiode n° 30
initial state :  (1, 0)
initial action :  0
Epsiode n° 31
initial state :  (1, 0)
initial action :  0
Epsiode n° 32
initial state :  (1, 0)
initial action :  0
Epsiode n° 33
initial state :  (1, 0)
initial action :  3
Epsiode n° 34
initial state :  (1, 0)
initial action :  1
Epsiode n° 35
initial state :  (1, 0)
initial action :  1
Epsiode n° 36
initial state :  (1, 0)
initial action :  2
Epsiode n° 37
initial state :  (1, 0)
initial action :  1
Epsiode n° 38
initial state :  (1, 0)
initial action :  1
Epsiode n° 39
initial state :  (1, 0)
initial action :  1
Epsiode n° 40
initial state :  (1, 0)
initial action :  2
Epsiode n° 41
initial state :  (1, 0)
initial action :  3
Epsiode n° 42
initial state :  (1, 0)
initial action :  2
Epsiode n° 43
initial state :  (1, 0)
initial action :  0
Epsiode n° 44
initial state :  (1, 0)
initial action :  2
Epsiode n° 45
initial state :  (1, 0)
initial action :  0
Epsiode n° 46
initial state :  (1, 0)
initial action :  2
Epsiode n° 47
initial state :  (1, 0)
initial action :  2
Epsiode n° 48
initial state :  (1, 0)
initial action :  1
Epsiode n° 49
initial state :  (1, 0)
initial action :  2
Epsiode n° 50
initial state :  (1, 0)
initial action :  0
Epsiode n° 51
initial state :  (1, 0)
initial action :  2
Epsiode n° 52
initial state :  (1, 0)
initial action :  3
Epsiode n° 53
initial state :  (1, 0)
initial action :  0
Epsiode n° 54
initial state :  (1, 0)
initial action :  2
Epsiode n° 55
initial state :  (1, 0)
initial action :  1
Epsiode n° 56
initial state :  (1, 0)
initial action :  3
Epsiode n° 57
initial state :  (1, 0)
initial action :  1
Epsiode n° 58
initial state :  (1, 0)
initial action :  1
Epsiode n° 59
initial state :  (1, 0)
initial action :  1
Epsiode n° 60
initial state :  (1, 0)
initial action :  1
Epsiode n° 61
initial state :  (1, 0)
initial action :  0
Epsiode n° 62
initial state :  (1, 0)
initial action :  3
Epsiode n° 63
initial state :  (1, 0)
initial action :  0
Epsiode n° 64
initial state :  (1, 0)
initial action :  3
Epsiode n° 65
initial state :  (1, 0)
initial action :  0
Epsiode n° 66
initial state :  (1, 0)
initial action :  3
Epsiode n° 67
initial state :  (1, 0)
initial action :  3
Epsiode n° 68
initial state :  (1, 0)
initial action :  3
Epsiode n° 69
initial state :  (1, 0)
initial action :  1
Epsiode n° 70
initial state :  (1, 0)
initial action :  2
Epsiode n° 71
initial state :  (1, 0)
initial action :  0
Epsiode n° 72
initial state :  (1, 0)
initial action :  3
Epsiode n° 73
initial state :  (1, 0)
initial action :  1
Epsiode n° 74
initial state :  (1, 0)
initial action :  2
Epsiode n° 75
initial state :  (1, 0)
initial action :  1
Epsiode n° 76
initial state :  (1, 0)
initial action :  3
Epsiode n° 77
initial state :  (1, 0)
initial action :  1
Epsiode n° 78
initial state :  (1, 0)
initial action :  0
Epsiode n° 79
initial state :  (1, 0)
initial action :  1
Epsiode n° 80
initial state :  (1, 0)
initial action :  1
Epsiode n° 81
initial state :  (1, 0)
initial action :  2
Epsiode n° 82
initial state :  (1, 0)
initial action :  0
Epsiode n° 83
initial state :  (1, 0)
initial action :  1
Epsiode n° 84
initial state :  (1, 0)
initial action :  1
Epsiode n° 85
initial state :  (1, 0)
initial action :  3
Epsiode n° 86
initial state :  (1, 0)
initial action :  2
Epsiode n° 87
initial state :  (1, 0)
initial action :  2
Epsiode n° 88
initial state :  (1, 0)
initial action :  1
Epsiode n° 89
initial state :  (1, 0)
initial action :  0
Epsiode n° 90
initial state :  (1, 0)
initial action :  3
Epsiode n° 91
initial state :  (1, 0)
initial action :  1
Epsiode n° 92
initial state :  (1, 0)
initial action :  2
Epsiode n° 93
initial state :  (1, 0)
initial action :  3
Epsiode n° 94
initial state :  (1, 0)
initial action :  3
Epsiode n° 95
initial state :  (1, 0)
initial action :  3
Epsiode n° 96
initial state :  (1, 0)
initial action :  0
Epsiode n° 97
initial state :  (1, 0)
initial action :  0
Epsiode n° 98
initial state :  (1, 0)
initial action :  0
Epsiode n° 99
initial state :  (1, 0)
initial action :  0

tresor found !!!
```