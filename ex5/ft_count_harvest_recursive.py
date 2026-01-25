def ft_count_harvest_recursive():
    i = 1
    days = int(input("Days until harvest:"))
    def recursive(day , i):
        if (day == 0):
            print("Harvest time!")
            return
        print("Day", i)
        recursive(day -1 , i + 1)
    recursive(days , i)
ft_count_harvest_recursive()
