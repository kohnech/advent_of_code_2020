import unittest
import day7

# Test input from Day7
file = [
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

expected_part1 = {
    'bright white' : ['light red', 'dark orange'],
    'dark olive' : ['shiny gold'],
    'dotted black' : ['dark olive', 'vibrant plum'],
    'faded blue' : ['muted yellow', 'dark olive', 'vibrant plum'],
    'muted yellow' : ['light red', 'dark orange'],
    'shiny gold' : ['bright white', 'muted yellow'],
    'vibrant plum' : ['shiny gold']
}

expected_part2 = {
    'light red' : [(1, 'bright white'), (2, 'muted yellow')],
    'dark orange' : [(3, 'bright white'), (4,  'muted yellow')],
    'bright white' : [(1, 'shiny gold')],
    'muted yellow' : [(2, 'shiny gold'), (9, 'faded blue')],
    'shiny gold' : [(1, 'dark olive') , (2, 'vibrant plum')],
    'dark olive' :  [(3, 'faded blue') , (4, 'dotted black')],
    'vibrant plum' :  [(5, 'faded blue') , (6, 'dotted black')]
    }

file_part2 = [
    'shiny gold bags contain 2 dark red bags.',
    'dark red bags contain 2 dark orange bags.',
    'dark orange bags contain 2 dark yellow bags.',
    'dark yellow bags contain 2 dark green bags.',
    'dark green bags contain 2 dark blue bags.',
    'dark blue bags contain 2 dark violet bags.',
    'dark violet bags contain no other bags.'
]

class TestDay7(unittest.TestCase):

    def test_get_children_bags(self):
        """
        Test that we get expected result for given input
        """
        cut = day7.Day7()
        out = cut.get_children_bags(file)
        self.assertEqual(out, expected_part1)
    

    def test_get_parents_bags(self):
        """
        Test that we get expected result for given input
        """
        cut = day7.Day7()
        out = cut.get_parents_bags(file)
        self.assertEqual(out, expected_part2)

    def test_depth_first_search(self):
        expected_part1 = {
        'bright white' : ['light red', 'dark orange'],
        'muted yellow' : ['light red', 'dark orange'],
        'shiny gold' : ['bright white', 'muted yellow'],
        'hello' :  ['world']
        }
        cut = day7.Day7()
        visited = set()
        cut.depth_first_search(expected_part1, 'shiny gold', visited)
        self.assertEqual({'shiny gold', 'muted yellow', 'dark orange', 'light red', 'bright white'}, visited)


    def test_solution_part1(self):
        """
        Test part 1
        """
        cut = day7.Day7()
        out = cut.solution_part1(file)
        self.assertEqual(out, {'muted yellow', 'dark orange', 'light red', 'bright white'})
        
    
    def test_solution_part2(self):
        """
        Test part 2
        """
        cut = day7.Day7()
        out = cut.solution_part2(file)
        self.assertEqual(32, out) 
        out = cut.solution_part2(file_part2)
        self.assertEqual(126, out)
    


if __name__ == '__main__':
    unittest.main()
