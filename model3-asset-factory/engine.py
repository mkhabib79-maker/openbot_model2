import os
import json

MONETAG_SCRIPT_SRC = "https://alwingulla.com" 

def generate_all_tools(config_path, template_path, output_dir):
    # 1. Load the list configuration array
    with open(config_path, 'r', encoding='utf-8') as f:
        tools_list = json.load(f)
        
    with open(template_path, 'r', encoding='utf-8') as f:
        template_raw = f.read()

    os.makedirs(output_dir, exist_ok=True)

    # 2. Iterate through every tool entry dynamically
    for config in tools_list:
        output_html = template_raw
        
        for key, value in config.items():
            placeholder = f"{{{{ {key} }}}}"
            output_html = output_html.replace(placeholder, str(value))

        # 3. Monetization script compilation
        ad_script_block = f"""
        <!-- Programmatic Monetag Ad Integration -->
        <script src="{MONETAG_SCRIPT_SRC}" data-zone="8888888" defer></script>
        """
        if "</head>" in output_html:
            output_html = output_html.replace("</head>", f"{ad_script_block}\n</head>")

        # 4. Save output individual file
        file_name = f"{config['TOOL_SLUG']}.html"
        final_output_path = os.path.join(output_dir, file_name)
        
        with open(final_output_path, 'w', encoding='utf-8') as f:
            f.write(output_html)
            
        print(f"✔️ Compiled Multi-Asset: {final_output_path}")

if __name__ == "__main__":
    generate_all_tools(
        config_path='model3-asset-factory/manifest.json',
        template_path='model3-asset-factory/templates/base_tool.html',
        output_dir='public/assets/tools'
    )
