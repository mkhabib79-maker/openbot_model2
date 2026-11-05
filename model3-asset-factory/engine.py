import os
import json

MONETAG_SCRIPT_SRC = "https://alwingulla.com" 

def generate_all_tools_and_hub(config_path, template_path, output_dir):
    # 1. تمام ٹولز کا ڈیٹا لوڈ کریں
    with open(config_path, 'r', encoding='utf-8') as f:
        tools_list = json.load(f)
        
    with open(template_path, 'r', encoding='utf-8') as f:
        template_raw = f.read()

    os.makedirs(output_dir, exist_ok=True)
    cards_html = ""

    # 2. ہر ٹول کو باری باری جنریٹ کریں
    for config in tools_list:
        output_html = template_raw
        
        for key, value in config.items():
            placeholder = f"{{{{ {key} }}}}"
            output_html = output_html.replace(placeholder, str(value))

        # مونیٹائزیشن اسکرپٹ انجیکشن
        ad_script_block = f'\n<!-- Monetag Integration -->\n<script src="{MONETAG_SCRIPT_SRC}" data-zone="8888888" defer></script>'
        if "</head>" in output_html:
            output_html = output_html.replace("</head>", f"{ad_script_block}\n</head>")

        file_name = f"{config['TOOL_SLUG']}.html"
        final_output_path = os.path.join(output_dir, file_name)
        
        with open(final_output_path, 'w', encoding='utf-8') as f:
            f.write(output_html)
            
        print(f"✔️ Compiled Multi-Asset: {final_output_path}")

        # ہوم پیج کے لیے کارڈز کا ڈیزائن تیار کرنا
        tool_url = f"assets/tools/{file_name}"
        cards_html += f"""
        <div class="bg-white/70 backdrop-blur-md p-6 rounded-2xl shadow-md border border-white/30 flex flex-col justify-between hover:shadow-xl transition-all duration-300">
            <div>
                <h3 class="text-xl font-bold text-slate-800 mb-2">{config['TOOL_HEADING']}</h3>
                <p class="text-sm text-slate-500 mb-4">{config['TOOL_DESCRIPTION']}</p>
            </div>
            <a href="{tool_url}" class="block text-center bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold p-3 rounded-xl hover:from-blue-700 hover:to-indigo-700 transition">
                Launch Tool →
            </a>
        </div>
        """

    # 3. اب مین انڈیکس ڈیش بورڈ (index.html) فائل تیار کریں
    hub_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>B2B Growth Micro-SaaS Hub</title>
    <script src="https://jsdelivr.net"></script>
    <script src="{MONETAG_SCRIPT_SRC}" data-zone="8888888" defer></script>
</head>
<body class="bg-gradient-to-br from-slate-50 to-slate-200 min-h-screen text-slate-800">
    <div class="max-w-6xl mx-auto px-4 py-12">
        <header class="text-center mb-16">
            <h1 class="text-4xl md:text-5xl font-black tracking-tight bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent mb-4">
                B2B Free Tools Directory
            </h1>
            <p class="text-slate-600 max-w-xl mx-auto">
                Boost your data optimization, outreach math, and analytics using our free micro-utility services.
            </p>
        </header>
        
        <!-- dynamic multi-tool tools dashboard grid placement -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            {cards_html}
        </div>
    </div>
</body>
</html>"""

    # فائنل index.html کو عام پبلک فولڈر کی جڑ (public/index.html) میں سیو کریں
    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(hub_html)
    print("✔️ Successfully compiled Central Index Explorer Hub Dashboard: public/index.html")

if __name__ == "__main__":
    generate_all_tools_and_hub(
        config_path='model3-asset-factory/manifest.json',
        template_path='model3-asset-factory/templates/base_tool.html',
        output_dir='public/assets/tools'
    )
