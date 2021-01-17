import re
import collections
import pprint

from typing import DefaultDict
from typing import Dict
from typing import List


class Day7():

    def get_children_bags(self, file: List[str]) -> DefaultDict[str, List[str]]:
        """
        Returns DefaultDict with children mapped to parents
        """
        parents_bags = []

        for line in file:
            parents_bags.append(re.split(' contain |, ', line))

        children = collections.defaultdict(list)
        for bags in parents_bags:
            for i in range(len(bags) - 1):
                child_regex = re.compile(r"^(\d+) (\w+) (\w+) (\w+)")
                child_match = child_regex.match(bags[i + 1])

                if child_match:
                    child = re.sub(r"[0-9] | (bag.?\.?)", "", bags[i + 1])
                    parent = re.sub(r"(bag.?)", "", bags[0])
                    children[child.strip()].append(parent.strip())

        return children

    def get_parents_bags(self, file: List[str]) -> DefaultDict[str, List[str]]:
        """
        Returns DefaultDict with parents mapped to children
        """
        parents_bags = []

        for line in file:
            parents_bags.append(re.split(' contain |, ', line))

        # create default dict
        parents = collections.defaultdict(list)
        for bags in parents_bags:
            for i in range(len(bags) - 1):
                parent = re.sub(r"(bag.?)", "", bags[0])
                # Only match allowed children, remove text like "no other bags" and filter
                # out number
                child_regex = re.compile(r"^(\d+) (\w+) (\w+) (\w+)")
                child_match = child_regex.match(bags[i + 1])

                if child_match:
                    child = re.sub(r"[0-9] | (bag.?\.?)", "", bags[i + 1])
                    num_regex = re.compile(r"[0-9]")
                    num_match = num_regex.match(bags[i + 1])
                    parents[parent.strip()].append((int(num_match[0]), child.strip()))

        return parents

    def depth_first_search(self, graph, node, visited):
        """
        Search a graph depth first in part1 (children to parents)
        """
        if node not in visited:
            # print(node)
            visited.add(node)
            if node in graph:
                for child in graph[node]:
                    self.depth_first_search(graph, child, visited)

    def breadth_first_search(self, graph, root):
        """
        Search a graph breadth first in part 1 (children to parents)
        """
        q = [] # queue
        visited = set() # dont search same node again...
        q.append(root) # start search att root
        while len(q) != 0:
            bag = q.pop()
            
            if bag not in visited:
                visited.add(bag)
                if bag in graph:
                    for child in graph[bag]:
                        q.append(child)
                    else:
                        continue
                        
        return visited

    def part2_depth_first_search(self, graph, node: str, visited):
        """
        Search a graph depth first in part2 (parents to children)
        """
        n = 1
        if node not in visited:
            # print(node)
            visited.add(node)
            if node in graph:
                for multiplier, child in graph[node]:
                    n += multiplier * self.part2_depth_first_search(graph, child, visited)
        return n

    def solution_part1(self, file):
        """Solutin part 1 Using Depth First Search"""
        visited = set()
        self.depth_first_search(self.get_children_bags(file), 'shiny gold', visited)
        return visited - {'shiny gold'}

    def solution_part2(self, file):
        """Solution part 2 using DFS"""
        visited = set()
        out = self.part2_depth_first_search(self.get_parents_bags(file), 'shiny gold', visited)
        return out - 1  # 'shiny gold' should not be counted...

    @staticmethod
    def read_input_file(filename):
        file = []
        with open(filename) as my_file:
            for line in my_file:
                file.append(line.rstrip())
        return file


# Test input from Day7
test_file = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags."
]

if __name__ == '__main__':
    day7 = Day7()
    # Given test
    pprint.pprint("Solution Test Part1: " + str(len(day7.solution_part1(test_file))))
    pprint.pprint("Solution Test Part2: " + str((day7.solution_part2(test_file))))
    # My solution
    file = Day7.read_input_file('day7_input.txt')
    pprint.pprint("Solution Test Part1: " + str(len(day7.solution_part1(file))))
    pprint.pprint("Solution Test Part2: " + str((day7.solution_part2(file))))
