list1=["|_|","|_|","|_|"]
list2=["|_|","|_|","|_|"]
list3=["|_|","|_|","|_|"]
map=[list1,list2,list3]
print("hiding ur treasure!x marks the spot.")
position=input()
letter=position[0].lower()
abc=["a" ,"b","c"]
letter_index=abc.index(letter)
number_index=int(position[1])-1
map[number_index][letter_index]="x"

print(f"{list1}\n{list2}\n{list3}")