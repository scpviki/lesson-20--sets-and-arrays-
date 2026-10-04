set1= {"apple", "banana", "mango" , "apple", "grape"}
set2= {"mango", "kiwi", "banana", "kiwi"}

print("basket 1 is ", set1)
print("basket 2 is ", set2)


set1.add("orange")

print("basket 1 after printing orange is", set1)

common_fruits=set1.intersection(set2) 

print("the fruits in both baskets are ", common_fruits)

#arrays
import array as arr
fruit_count=arr.array("i",[3,5,2,4])

print("fruit count array is",fruit_count)


fruit_count.insert(2,1)

fruit_count.append(8)

print("fruit count after adding items is", fruit_count)

count_of_4 = fruit_count.count(4)
print("numbwer of time 4 appears is", count_of_4)
fruit_count.reverse()
print("reverse fruit array is ", fruit_count)