Relook at main.py replace_text function line 6
new_str = re.sub(pattern, r'\g<1> ', data) "data" should be replaced with proper function input "text"
