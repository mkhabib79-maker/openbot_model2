import os
import json

# Paste your real Monetag Tag/Script URL or Zone ID between these quotes when ready
MONETAG_SCRIPT_SRC = "https://alwingulla.com" 

def generate_all_tools_and_hub(config_path, template_path, output_dir):
    # 1. Loading Configuration Array and Template
    with open(config_path, 'r', encoding='utf-8') as f:
        tools_list = json.load(f)
        
    with open(template_path, 'r', encoding='utf-8') as f:
        template_raw = f.read()

    os.makedirs(output_dir, exist_ok=True)
    cards_html = ""

    # 2. Iterate through every tool entry dynamically
    for config in tools_list:
        output_html = template_raw
        
        for key, value in config.items():
            placeholder = f"{{{{ {key} }}}}"
            output_html = output_html.replace(placeholder, str(value))

        # Automated Monetization Injection Layer
        ad_script_block = f'\n<!-- Monetag Integration -->\n<script src="{MONETAG_SCRIPT_SRC}" data-zone="3563306" defer></script>'
        if "</head>" in output_html:
            output_html = output_html.replace("</head>", f"{ad_script_block}\n</head>")

        file_name = f"{config['TOOL_SLUG']}.html"
        final_output_path = os.path.join(output_dir, file_name)
        
        with open(final_output_path, 'w', encoding='utf-8') as f:
            f.write(output_html)
            
        print(f"✔️ Compiled Multi-Asset: {final_output_path}")

        # Generating HTML Card interface components with fixed path string formatting
        tool_url = f"assets/tools/{file_name}"
        cards_html += f"""
        <div class="bg-white/70 backdrop-blur-md p-6 rounded-2xl shadow-md border border-white/30 flex flex-col justify-between hover:shadow-xl transition-all duration-300">
            <div>
                <h3 class="text-xl font-bold text-slate-800 mb-2">{config['TOOL_HEADING']}</h3>
                <p class="text-sm text-slate-500 mb-4">{config['TOOL_DESCRIPTION']}</p>
            </div>
            <a href="{tool_url}" class="block text-center bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold p-3 rounded-xl hover:from-blue-700 hover:to-indigo-700 transition shadow-md shadow-blue-500/20">
                Launch Tool →
            </a>
        </div>
        """

    # 3. Create central dashboard entry point using the stable CDN injection layer
    hub_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>B2B Growth Micro-SaaS Hub</title>
    <script src="https://tailwindcss.com"></script>
    <script src="{MONETAG_SCRIPT_SRC}" data-zone="8888888" defer></script>
    <style>
        .glass {{
            background: rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
    </style>
</head>
<body class="bg-gradient-to-br from-slate-50 to-slate-200 min-h-screen text-slate-800 antialiased flex flex-col justify-between">
    <div class="max-w-6xl mx-auto px-4 py-12 flex-grow w-full">
        <header class="text-center mb-16">
            <span class="px-3 py-1 text-xs font-semibold text-blue-600 bg-blue-100 rounded-full uppercase tracking-wider">Ecosystem Active</span>
            <h1 class="text-4xl md:text-5xl font-black tracking-tight bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent mb-4 mt-3">
                B2B Free Tools Directory
            </h1>
            <p class="text-slate-600 max-w-xl mx-auto text-sm md:text-base">
                Boost your data optimization, outreach math, and analytics using our free micro-utility services.
            </p>
        </header>
        
        <!-- Interactive Tool Grid Layout -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {cards_html}
        </div>
    </div>

    <!-- Central Traffic Loop Footer Platform Integration -->
    <footer class="p-6 text-center border-t border-slate-200 glass text-xs text-slate-500 w-full mt-12">
        <p>Powered by B2B Suite | Need raw automated data? 
            <a href="https://rapidapi.com" target="_blank" class="text-blue-600 font-bold hover:underline">
                Access our Model 2 Lead Generation API Storefront
            </a>
        </p>
    </footer>
</body>
</html>"""

    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(hub_html)
    print("✔️ Successfully compiled Central Index Explorer Hub Dashboard: public/index.html")

if __name__ == "__main__":
    generate_all_tools_and_hub(
        config_path='model3-asset-factory/manifest.json',
        template_path='model3-asset-factory/templates/base_tool.html',
        output_dir='public/assets/tools'
    )
