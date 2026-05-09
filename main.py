x = 10

def outer():
    x = 20
    def inner():
        nonlocal x
        x = 30
        print("Inner x:", x)
    inner()
    print("Outer x:", x)

outer()
print("Global x:", x)
```

Kodni ishlatib ko'rish uchun quyidagilarni amalga oshiring:

1. Kodni yozib, keyin uni ishlab ko'ring.
2. `outer()` funksiyasini chaqiring.
3. `inner()` funksiyasining `x` o'zgaruvchisini ko'ring.
4. `outer()` funksiyasining `x` o'zgaruvchisini ko'ring.
5. Global `x` o'zgaruvchisini ko'ring.
