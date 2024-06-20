import nbformat
import openai
import random

# Set OpenAI API key
openai.api_key = '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'  # Replace this with your actual OpenAI API key

# Load the notebook
notebook_path = 'C:\\Users\\PRATHAM GUPTA\\Documents\\SampleNotebook.ipynb'  # Update with the path to your notebook
with open(notebook_path, 'r') as f:
    nb = nbformat.read(f, as_version=4)

def get_variation(text, role='user'):
    prompt = f"Generate a variation of the following {role} conversation while retaining the same functionality and flow:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def get_code_variation(code):
    prompt = f"Generate a variation of the following code while retaining the same functionality:\n\n{code}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def get_variation_with_function_call(text, function_name):
    prompt = f"Generate a variation of the following conversation involving the function '{function_name}':\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        functions=[
            {
                "name": function_name,
                "description": "Function to handle specific task."
            }
        ]
    )
    return response['choices'][0]['message']['content']

def vary_cell(cell):
    if cell['cell_type'] == 'markdown':
        cell['source'] = get_variation(cell['source'], role='assistant')
    elif cell['cell_type'] == 'code':
        cell['source'] = get_code_variation(cell['source'])
    return cell

def vary_function_call_cell(cell):
    if cell['cell_type'] == 'code' and 'function_name' in cell['metadata']:
        function_name = cell['metadata']['function_name']
        cell['source'] = get_variation_with_function_call(cell['source'], function_name)
    return cell

def vary_notebook(nb):
    for cell in nb['cells']:
        if 'function_name' in cell['metadata']:
            cell = vary_function_call_cell(cell)
        else:
            cell = vary_cell(cell)
    return nb

new_nb = vary_notebook(nb)

# Save the new variations to a new notebook
new_notebook_path = 'C:\\Users\\PRATHAM GUPTA\\Documents\\SampleNotebook_Variation.ipynb'  # Update with the path to save the new notebook
with open(new_notebook_path, 'w') as f:
    nbformat.write(new_nb, f)
