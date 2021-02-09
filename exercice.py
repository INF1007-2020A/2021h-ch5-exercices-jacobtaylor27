#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    return (number**2)**0.5


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    nom = []
    for i in prefixes:
        nom.append(i + suffixe)
    return nom


def prime_integer_summation() -> int:
    sum = 0 
    i = 0
    num = 2
    isPrime = True
    # while i < 100:
    #     if isPrime:
    #         num += 1
    #         sum += i
    #     else:
    #         i += 1
    return sum


def factorial(number: int) -> int:
    facto = number
    while number > 1:
        number -= 1
        facto *= number
    return facto


def use_continue() -> None:
    for i in range(11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    array = []
    for group in groups:
        if len(group) >= 10 or len(group) <= 3:
            array.append(False)
            continue
        temp = False
        temp2 = False

        for age in group:
            if age != 25:
                if age < 18:
                    array.append(False)
                    break

                elif age == 50:
                    temp = True

                elif age > 70:
                    temp2 = True

                elif temp and temp2:
                    array.append(False)
                    break

        # array.append(True)
        # continue
        
    return array


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
