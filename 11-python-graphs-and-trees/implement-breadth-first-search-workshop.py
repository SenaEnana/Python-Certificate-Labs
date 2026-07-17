def gen_parentheses(pairs):
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'
    if pairs < 1:
        return 'The number of pairs should be at least 1'    
    
    return []