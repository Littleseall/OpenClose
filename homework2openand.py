cookbook = {}

with open('cook_book.txt', encoding='utf-8') as file:
    current_recipe = ''

    for line in file:
        line = line.strip()

        if line.isdigit():
            continue
        elif line and '|' not in line:
            cookbook[line] = []
            current_recipe = line
        elif line and '|' in line:
            ingredient_name, quantity, unit = line.split(" | ")
            cookbook[current_recipe].append({
                'ingredient': ingredient_name,
                'amount': int(quantity),
                'unit': unit
            })

print(cookbook)


#Задание2:
def get_shopping_list(selected_dishes, servings_count):
    shopping_list = {}

    for dish in selected_dishes:
        if dish in cookbook:
            ingredients = cookbook[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient']
                total_amount = ingredient['amount'] * servings_count
                unit = ingredient['unit']

                if name in shopping_list:
                    shopping_list[name]['amount'] += total_amount
                else:
                    shopping_list[name] = {'unit': unit, 'amount': total_amount}
        else:
            print(f"Рецепт '{dish}' не найден в списке.")

    return shopping_list

result = get_shopping_list(['Запеченный картофель', 'Фахитос'], 2)
print(result)


#Задание 3:
def combine_files(file_list, output_filename):
    combined_content = []

    for filename in file_list:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            combined_content.append((filename, len(lines), lines))

    combined_content.sort(key=lambda x: x[1])

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for name, count, lines in combined_content:
            output_file.write(f"{name}\n{count}\n")
            output_file.writelines(lines)


input_files = ['1.txt', '2.txt']
output_file = '3.txt'
combine_files(input_files, output_file)