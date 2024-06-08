# Ստեղծել բառարան երեք բանալի-արժեք զույգերով, որտեղ բանալիները ուսանողների անուններն են, իսկ արժեքները՝ նրանց գնահատականները։
# Ավելացնել նոր ուսանող և նրա գնահատականը բառարանում։ Այնուհետև տպել բոլոր ուսանողների անունները և նրանց գնահատականները։
# Փոփոխել կամայական ուսանողի գնահատականը և ջնջել մեկ այլ ուսանողի ամբողջությամբ։


students_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

students_grades["David"] = 92

print("Initial students and their grades:", students_grades)

students_grades["Bob"] = 95

del students_grades["Charlie"]

print("Final students and their grades:", students_grades)



# Ստեղծել երկու set տարբեր արժեքներով, միավորեք դրանք և տպեք վերջնական արդյունքը։

set1 = {1, 2, 3}
set2 = {3, 4, 5}


merged_set = set1.union(set2)


print("Merged set:", merged_set)



# Գրել ծրագիր, որը ցիկլերի միջոցով կտպի հետևյալ պատկերը էկրանին:

n = 5

for i in range(1, n + 1):
    
    print('*' * i)




# Գրեք ծրագիր, որը որպես մուտքային արժեք կստանա տող և կտպի բաղաձայնների և ձայնավորների քանակը(կարող եք վերցնել անգլերեն այբուբենը)։

input_string = input("Enter a string: ")

vowels = "aeiouAEIOU"

vowel_count = sum(1 for char in input_string if char in vowels)
consonant_count = sum(1 for char in input_string if char.isalpha() and char not in vowels)

print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")


