numbers = [ 1.4142, 2.7182, 2.7182, 3.1415, 2.7182, 1.4142 ]
numbers2 = [ 1.4142, 2.7182, 3.1415] 

# counters is a dictionary which maps each number in the numbers
# array to its number of occurrences
counters = { (x, numbers.count(x)) for x in numbers2 }
 
for (x, count) in counters:
    print("%f: %d" % (x, count))
