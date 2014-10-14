enforcer
========

Python library and script which can be used to build entropy control loops.

#Script Example:#

Make a list of files you want.
```
echo -e "a\nb\nc" > /tmp/goal_files
```

```
cat /tmp/goal_files
a
b
c
```

Make a bunch of files you don't want.
```
enforce andrewguy9$ touch 1 2 3
```

```
ls
1    2    3
```

Now run the enforcer. It will remove the files you didn't want, and create the ones you wanted.
```
enforce --current ls --goal cat /tmp/goal --remove rm '${KEY}' --add touch '${KEY}'
Not converged
```

```
ls
a    b    c
```

On subsequent run, it returns converged to tell you that no work was required.
```
enforce --current ls --goal cat /tmp/goal --remove rm '${KEY}' --add touch '${KEY}'
Converged
```

```
ls
a    b    c
```
