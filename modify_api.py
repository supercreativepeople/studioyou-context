#!/usr/bin/env python3

# Read the extracted HTML file
with open('/Users/supercreativepeople/Documents/studioyou-context/archetypes_extracted.html', 'r') as f:
    content = f.read()

# Find and display the current getApiUrl function
start = content.find('const getApiUrl')
end = content.find('};', start) + 2
current_function = content[start:end]
print("CURRENT FUNCTION:")
print(current_function)
print("\n" + "="*60 + "\n")

# Replace the placeholder URL with the Cloud Run endpoint
old_url = 'https://studioyou-api-default.example.com'
new_url = 'https://studioyou-api-198959034459.us-east1.run.app'

modified_content = content.replace(old_url, new_url)

# Display the modified function
start = modified_content.find('const getApiUrl')
end = modified_content.find('};', start) + 2
new_function = modified_content[start:end]
print("MODIFIED FUNCTION:")
print(new_function)
print("\n" + "="*60 + "\n")

# Save the modified file back
with open('/Users/supercreativepeople/Documents/studioyou-context/archetypes_extracted.html', 'w') as f:
    f.write(modified_content)

print("✅ File updated successfully!")
