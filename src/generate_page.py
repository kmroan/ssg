from blocks import markdown_to_blocks, markdown_to_html_node
import os

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for b in blocks:
        if b.startswith("# "):
            return b[2:]
    raise Exception("title not found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as md_file:
        md = md_file.read()
    with open(template_path, "r") as template_file:
        template = template_file.read()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    # Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    
    dst_dir = os.path.dirname(dest_path)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)

    template_file.close()
    md_file.close()
