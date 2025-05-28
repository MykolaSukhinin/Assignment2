def select(grades: list, passgrade =60) -> list: 

    """
   Функція приймає на вчід список з дійних чисел та повертає від фільтрований список із значень за введене число
    """
    result =[]
    for ele in grades:
        if ele >= passgrade:
            result.append(ele)
    return result 



greatbook = {"Kolya": [90, 54,88, 3, 100],
              "Sonya": [54, 43, 88, 90, 6],
                "Ruslan":[12, 99, 88, 45]}

for key in greatbook:
   a=select( greatbook[key])
   print (f"{key}:", *a,  f"Average : {sum(a)/len(a)}")

    






