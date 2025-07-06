def fizzBuzz(n: int) -> str:
    # lookup ={
    #     'Fizz' : 0,
    #     'Buzz' : 0,
    # }
    lookup = ['Fizz', 'Buzz', 'Bazz']
    result = []
    for x in range(1, n+1):
        answer = ''
        if (x % 3) == 0:
            answer = answer + lookup[0]
        if (x % 5) == 0:
            answer = answer + lookup[1]
        if (x % 7) == 0:
            answer = answer + lookup[2]    
        if answer == '':
            result.append(str(x))
            continue
        result.append(answer)
    return result

print(fizzBuzz(105))


