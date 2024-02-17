import pypandoc

input_file = 'openapi3.json'
output_file = 'output.html'

# Convert OpenAPI 3 JSON to HTML
pypandoc.convert_file(input_file, 'html', outputfile=output_file)