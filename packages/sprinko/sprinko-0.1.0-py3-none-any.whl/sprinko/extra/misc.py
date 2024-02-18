import re
def unpack_dict_to_py_var(data : dict):
    return ''.join(f"{k} = {v}\n" for k, v in data.items())

def replace_ctx_get_calls(text):
    # This pattern matches 'ctx.get('any_key')' and captures 'any_key' in a group for replacement
    pattern = r"ctx\.get\((['\"])([^'\"]+)\1\)"
    # Replace the matched pattern with the captured group, effectively removing the 'ctx.get('')' part
    replaced_text = re.sub(pattern, r'\2', text)
    
    return replaced_text

    