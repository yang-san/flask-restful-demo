def min_length_str(min_length):
    def validate(s):
        if not s:
            raise Exception('password required !')
        
        elif not isinstance(s,(int, str)):
            raise Exception('password format error')
        
        if len(str(s)) >= min_length:
            return str(s)
        else:
            raise Exception(f'String must be at least {min_length} characters long !')

    return validate