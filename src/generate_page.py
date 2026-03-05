from blocks import markdown_to_blocks, markdown_to_html_node
import os

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for b in blocks:
        if b.startswith("# "):
            return b[2:]
    raise Exception("title not found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as md_file:
        md = md_file.read()
    with open(template_path, "r") as template_file:
        template = template_file.read()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    
    dst_dir = os.path.dirname(dest_path)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)

    template_file.close()
    md_file.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    ls = os.listdir(dir_path_content)
    for i in ls:
        path = os.path.join(dir_path_content, i)
        if os.path.isfile(path):
            dstfile = os.path.join(dest_dir_path,i.replace(".md",".html"))
            generate_page(path, template_path,dstfile,basepath)
        if os.path.isdir(path):
            dstpath = os.path.join(dest_dir_path, i)
            os.makedirs(dstpath)
            generate_pages_recursive(path, template_path, dstpath,basepath)
