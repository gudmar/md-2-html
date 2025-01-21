
test_cases_headings = [
    { 
        "description": 'h1 should work',
        "input": '# I am h1',
        "expected": '<h1 class="h1">I am h1</h1>',
    },
    {
        'description': 'When # is not the first character of the line, it is not heading',
        'input': ' # not h',
        'expected': ' # not h'
    },
    {
        "description": 'Backshlash before hash is no h1',
        "input": '\# I am not h1',
        "expected": r'\# I am not h1'
    },
    {
        "description": 'h2 should work',
        "input": '## I am h1',
        "expected": '<h2 class="h2">I am h2</h2>',
    },
    {
        "description": 'h3 should work',
        "input": '### I am h3',
        "expected": '<h3 class="h3">I am h3</h3>',
    },
    {
        "description": 'h4 should work',
        "input": '#### I am h4',
        "expected": '<h4 class="h4">I am h4</h4>',
    },
    {
        "description": 'h5 should work',
        "input": '##### I am h5',
        "expected": '<h5 class="h5">I am h5</h5>',
    },
    {
        "description": 'h6 should work',
        "input": '###### I am h6',
        "expected": '<h6 class="h6">I am h6</h6>',
    },
    {
        "description": 'h1 withoult space after # is not h1',
        "input": '#I am not h1',
        "expected": '#I am not h1'
    },
    {
        "description": 'h1 with 2 spaces is h1',
        "input": '#  I am h1',
        "expected": '<h1 class="h1"> I am h1</h1>',
    },
    {
        "description": 'h1 with line end is not h1',
        "input": '''#
I am h1''',
        "expected": '#h1 with line end is not h1'
    }
]


test_cases_bold = [
    {
        'description': 'Two stars wrapper, no space is bold',
        'input': '**bold text**',
        'expected': '<span class="bold"></span>',
    },
    {
        'description': 'Two stars wrapper with backshlash before them is not bold',
        'input': '\**bold text**',
        'expected': '**bold text**',
    },
    {
        'description': 'not backslash character before two stars is still bold',
        'input': 'a**bold text**',
        'expected': 'a<span class="italic">bold text</span>'
    },
    {
        'description': '2 stars wrapper with new line is not bold',
        'input': '''**
bold text**''',
        'expected': '''**
bold text**''',
    },
]

test_cases_strikethrough = [] # similar to bold and italic, renders to <s>

test_cases_italic = [
    {
        'description': 'Star wrapper, no space is italic',
        'input': '*italic text*',
        'expected': '<span class="italic"></span>',
    },
    {
        'description': 'backshlash before star is not italic',
        'input': '\*italic text*',
        'expected': '*italic text*',
    },
    {
        'description': 'Star, new line and text is not italic',
        'input': '''*
not italic text*''',
        'expected': '''*
not italic text*''',
    },
    {
        'description': 'star, backslash, star text is italic',
        'input': r'*\*italic**',
        'expected': '<span class="italic">*italic</span>*'
    },
    {
        'description': 'letter before single star is italic',
        'input': 'a*italic text*a',
        'expected': 'a<span class="italic">italic text</span>a'
    },
    {
        'description': 'white space after last character before star is still italic',
        'input': '*italic *',
        'expected': '<span class="italic">italic </span>'
    }
]

test_cases_ordered_lists = [
    {
        'description': 'starting with a number, a dot and space starts an ordered list',
        'input': '3. list',
        'expected': '''<ol><li>list</li></ol>'''
    },
    {
        'description': 'Three lines starting with a number, dot and a space are 3 list items',
        'input': '''2. item 1
4. item 2
6. item 3''',
        'expected': '''<ol><li>item 1</li><li>item 2</li><li>item 3</li></ol>'''
    },
    {
        'description': 'Items that are in the same line create only single list item',
        'input': '1. item 1 2. item 2 3. item 3',
        'expected': '<ol><li>item 1 2. item 2 3. item 3</li></ol>'
    },
    {
        'description': 'Ordered list item, and second item in new line, but no space between dot and firs character is a single line item',
        'input': '''1. item 1
2.item 2''',
        'expected': '<ol><li>item 1 2. item 2</li></ol>'
    },
    {
        'description': 'indentions before next list items make nested lists',
        'input': '''1. parent
    2. child
           3. grand child
            4. grand grand child
''',
    'expected': '<ol><li>parent<ol><li>child<ol><li>grand child<ol><li>grand grand child</li></ol></li></ol></li></ol></li></ol>'
    }
],

test_cases_unordered_lists = [
    {
        'description': 'starting with a minus and space starts an unordered list',
        'input': '- list',
        'expected': '''<ul><li>list</li></ul>'''
    },
    {
        'description': 'Three lines starting with a minus and a space are 3 list items',
        'input': '''- item 1
- item 2
- item 3''',
        'expected': '''<ul><li>item 1</li><li>item 2</li><li>item 3</li></ul>'''
    },
    {
        'description': 'Items that are in the same line create only single list item',
        'input': '- item 1 - item 2 - item 3',
        'expected': '<ul><li>item 1 - item 2 - item 3</li></ul>'
    },
    {
        'description': 'Unordered list item, and second item in new line, but no space between minus and firs character is a single line item',
        'input': '''- item 1
-item 2''',
        'expected': '<ul><li>item 1 2. item 2</li></ul>'
    },
    {
        'description': 'indentions before next list items make nested lists',
        'input': '''- parent
    - child
           - grand child
            - grand grand child
''',
    'expected': '<ul><li>parent<ul><li>child<ul><li>grand child<ul><li>grand grand child</li></ul></li></ul></li></ul></li></ul>'
    }
],

test_cases_rule = [
    {
        "description": 'Three minus signs make a rule',
        "input": '---',
        "expected": '<hr>'
    },
    {
        "description": 'More then 3 minuses in a line make a rule',
        "input": '------',
        "expected": '<hr>'
    },
    {
        "description": 'Any character in the middle of the line is not a rule',
        "input": '---f---',
        "expected": '---f---',
    },
    {
        'description': 'Starting with a character and then minuses is not a rule',
        'input': 'f---',
        'expected': 'f---'
    },
    {
        "description": 'backslash starting the line is an escape and no hr is created',
        "input": r'\---',
        'expected': r'\---'
    },
    {
        'description': 'a character ending minuses is not a rule',
        'input': '---s',
        'expected': '---s'
    },
    {
        'description': 'a backslash in the middle is not a rule, and it disappears',
        'input': r'--\-',
        'expected': '---'
    },
    {
        'description': 'a backslash at the end spoils the rule, but does not disappear',
        'input': r'---\\',
        'expected': r'---\\'
    },
]

test_cases_new_line = [
    {
        "description": '3 lines are 3 divs',
        "input": '''line 1
line 2
line 3''',
        "expected": '<div class="new-line">line 1</div><div class="new-line">line 2</div><div class="new-line">line 3</div>'
    }
]

test_cases_pre = []

test_cases_code = []

test_cases_table = [
    {
        'description': ''
    }
]

test_cases_checkboxes = []

