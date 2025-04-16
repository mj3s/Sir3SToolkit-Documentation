import re
import logging
from sphinx.application import Sphinx

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)

def convert_comments_to_docstring(code):
    comment_pattern = re.compile(r'#\s*={100}\n#\s*Method\s*:\s*(.*?)\n#\s*Input\s*:\s*(.*?)\n#\s*Output\s*:\s*(.*?)\n#\s*Description\s*:\s*(.*?)\n#\s*={100}', re.DOTALL)
    
    def replace_comment(match):
        method = match.group(1).strip()
        input_desc = match.group(2).strip()
        output_desc = match.group(3).strip()
        description = match.group(4).strip()
        
        docstring = f'"""\nMethod: {method}\n\nInput:\n    {input_desc}\n\nOutput:\n    {output_desc}\n\nDescription:\n    {description}\n"""'
        logger.debug(f'Converted comment to docstring:\n{docstring}')
        return docstring
    
    code_with_docstrings = comment_pattern.sub(replace_comment, code)
    return code_with_docstrings

def preprocess_source(app, docname, source):
    print(f'Preprocessing {docname}')
    logger.debug(f'Preprocessing {docname}')
    transformed_source = convert_comments_to_docstring(source[0])
    source[0] = transformed_source
    
    # Save the transformed source to a file for inspection
    output_file = f'transformed_{docname}.py'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(transformed_source)
    print(f'Saved transformed source to {output_file}')
    logger.debug(f'Saved transformed source to {output_file}')

def setup(app: Sphinx):
    app.connect('source-read', preprocess_source)
    print("sphinx_preprocess extension loaded")
    return {'version': '0.1'}
