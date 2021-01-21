# zen of python 


The Zen of Python, by Tim Peters

1. Beautiful is better than ugly.
1. Explicit is better than implicit.
1. Simple is better than complex.
1. Complex is better than complicated.
1. Flat is better than nested.
1. Sparse is better than dense.
1. Readability counts.
1. Special cases aren't special enough to break the rules.
1. Although practicality beats purity.
1. Errors should never pass silently.
1. Unless explicitly silenced.
1. In the face of ambiguity, refuse the temptation to guess.
1. There should be one-- and preferably only one --obvious way to do it.
1. Although that way may not be obvious at first unless you're Dutch.
1. Now is better than never.
1. Although never is often better than *right* now.
1. If the implementation is hard to explain, it's a bad idea.
1. If the implementation is easy to explain, it may be a good idea.
1. Namespaces are one honking great idea -- let's do more of those!


## 1. Beautiful is better than guly. 

## 17 & 18. implementation and idea 

## 19. Namespaces

``` python 
def chase():
    import menagerie.models.cat as cat
    import menagerie.models.dog as dog
    
    dog.chase(cat)
    cat.chase(mouse)

```


## Thanks 

* https://gist.github.com/evandrix/2030615