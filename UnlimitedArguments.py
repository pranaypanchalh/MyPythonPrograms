def func(*values):
    for i in values:
        print(i)
    print(type(values))

func(1,23,"Hilo",45,687)