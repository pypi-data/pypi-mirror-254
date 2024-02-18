# (P)ython (R)ecognizable (O)bject (N)otation #

The natural python extension to json. Parse and dump python objects to
string or file. Support all those annoyingly missing features: tuples,
complex, non-string keys, trailing commas, single qoute strings...

I wasn't first, or did it the best, but I nailed the name!


```
>>> import pron
>>> obj = pron.loads('''{1+2j:[3,"4",("monkey","business")],}''')
>>> print(pron.dumps(obj, indent=4, suppress=[tuple]))
{
    (1+2j): [
        3,
        '4',
        ('monkey', 'business')
    ]
}
```
