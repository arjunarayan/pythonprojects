def countEvenAndOdd(numList):
    odd_count = 0
    even_count = 0
    for num in numList:
        if num % 2 == 1:
            odd_count += 1
        else:
            even_count += 1
    return {"odd" : odd_count,
            "even:": even_count}


print(countEvenAndOdd([]))
