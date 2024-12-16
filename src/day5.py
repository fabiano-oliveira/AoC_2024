from shared import read_all_lines
from typing import List, Tuple, Dict


def parse_rules_and_update_list(data: List[str]) -> Tuple[Dict[str, List[str]], List[List[str]]]:
    rules = {}
    update_list = []

    for line in data:
        line = line.strip()
        if "|" in line:
            rule = line.split("|")
            if rule[0] in rules:
                rules[rule[0]].add(rule[1])
            else:
                rules[rule[0]] = set([rule[1]])
        elif "," in line:
            update_list.append(line.split(","))

    return rules, update_list

def is_update_valid(rules: Dict[str, List[str]], update: List[str]) -> bool:
    for index, value in enumerate(update):
        if value in rules:
            invalid_preceding_values = rules[value]
            if len(set(update[:index]) & invalid_preceding_values) > 0:
                return False
    return True



def select_valid_updates(rules: Dict[str, List[str]], update_list: List[List[str]]) -> List[List[str]]:
    return [
        update 
        for update 
        in update_list
        if is_update_valid(rules, update)
    ]

def select_invalid_updates(rules: Dict[str, List[str]], update_list: List[List[str]]) -> List[List[str]]:
    return [
        update 
        for update 
        in update_list
        if not is_update_valid(rules, update)
    ]

def fix_invalid_updates(rules: Dict[str, List[str]], update_list: List[List[str]]) -> List[List[str]]:
    return [
        fix_invalid_update(rules, update) 
        for update 
        in update_list
    ]

def fix_invalid_update(rules: Dict[str, List[str]], update: List[str]) -> List[str]:
    is_invalid = True
    fixed_update = list(update)

    while is_invalid:
        is_invalid = False
        for index, value in enumerate(fixed_update):
            if value in rules:
                invalid_preceding_values = rules[value]
                invalid_set = set(fixed_update[:index]) & invalid_preceding_values
                if len(invalid_set) > 0:
                    is_invalid = True
                    should_insert_before = fixed_update.index(invalid_set.pop())
                    fixed_update.remove(value)
                    fixed_update.insert(should_insert_before, value)
                    break
    return fixed_update


def sum_middle_elements(update_list: List[List[str]]) -> int:
    return sum(int(update[len(update) // 2]) for update in update_list)

def main():
    data = read_all_lines("./src/day5-input.txt")
    rules, update_list = parse_rules_and_update_list(data)
    valid_updates = select_valid_updates(rules, update_list)
    print("Sum of middle elements:", sum_middle_elements(valid_updates))

    invalid_updates = select_invalid_updates(rules, update_list)
    fixed_updates = fix_invalid_updates(rules, invalid_updates)
    print("Sum of middle elements:", sum_middle_elements(fixed_updates))

if __name__ == "__main__":
    main()
