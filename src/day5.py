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

def sum_middle_elements(update_list: List[List[str]]) -> int:
    return sum(int(update[len(update) // 2]) for update in update_list)

def main():
    data = read_all_lines("./src/day5-input.txt")
    rules, update_list = parse_rules_and_update_list(data)
    valid_updates = select_valid_updates(rules, update_list)
    print("Sum of middle elements:", sum_middle_elements(valid_updates))


if __name__ == "__main__":
    main()
