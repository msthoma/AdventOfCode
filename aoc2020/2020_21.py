from utils.utils import get_data, res_print2


def main():
    data = get_data().splitlines()
    all_allergens, edited_data = set(), []

    for line in data:
        ingredients, allergens = line.rstrip(")").split(" (contains ")
        ingredients, allergens = ingredients.split(" "), allergens.split(", ")
        for allergen in allergens:
            all_allergens.add(allergen)
        edited_data.append([ingredients, allergens])

    candidates_for_allergens = {}
    for allergen in all_allergens:
        candidates = None
        for line in edited_data:
            if allergen in line[1]:
                if not candidates:
                    candidates = set(line[0])
                else:
                    candidates = list(set(candidates) & set(line[0]))
        candidates_for_allergens[allergen] = candidates

    contain_allergen = set()
    for ingredients in candidates_for_allergens.values():
        for ing in ingredients:
            contain_allergen.add(ing)

    answer_a = 0
    for line in edited_data:
        for ing in line[0]:
            if ing not in contain_allergen:
                answer_a += 1

    determined, not_determined = {}, all_allergens.copy()

    while len(not_determined) != 0:
        new_candidates = {}
        for allergen, candidates in candidates_for_allergens.items():
            if len(candidates) == 1:
                not_determined.remove(allergen)
                determined[allergen] = candidates[0]
                for al in not_determined:
                    new_candidates[al] = candidates_for_allergens[al]
                    try:
                        new_candidates[al].remove(candidates[0])
                    except:
                        pass
                break
        candidates_for_allergens = new_candidates.copy()

    determined = dict(sorted(determined.items()))

    res_print2(answer_a, 1)
    res_print2(",".join(determined.values()), 2)


if __name__ == '__main__':
    main()
