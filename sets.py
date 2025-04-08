n = int(input())


sample_set = set(map(int, input().split())) 


N = int(input())

for _ in range(N ): 
    commands = input().split()

    
    cmd= commands[0]
    match cmd : 
        case "pop": 
            if sample_set : 
                sample_set.pop()
            
        case "remove":
            args = int(commands[1]) 
            if args in sample_set: 
                sample_set.remove(args)
        case "discard": 
            args = int(commands[1])
            sample_set.discard(args)
    
    

print(sum(sample_set))

