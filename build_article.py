import requests
import shutil
import re
import os
from pathlib import Path
import markdown
import time
from datetime import datetime

def frm(dir_path):
    try:
        shutil.rmtree(dir_path)
    except Exception as e:
        print(f"Error: {e}")

def mk_dir(path):
    dest_dir = os.path.dirname(path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)


def get_all_md_file_paths_from(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
              file_paths.append(os.path.join(root, file))
    return file_paths

def get_md_lines(md_file_path):
  try:
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
      return md_file.readlines()
  except FileNotFoundError:
    print(f"Error: The file '{md_file_path}' was not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

def get_title(md_lines):
  for line in md_lines:
    if line.startswith("#"):
       return line.replace("#", "").strip()
  return None

def get_author(md_lines):
  for line in md_lines:
    if line.startswith("- author:"):
       return line.replace("- author:", "").strip()
  return None

def get_last_modified_date(file_path):
    timestamp = os.path.getmtime(file_path)
    modified_date = datetime.fromtimestamp(timestamp)
    return modified_date.strftime('%Y-%m-%d')

def get_first_url(md_lines):
    url_pattern = re.compile(r'https?://[^)\s ]+')
    for line in md_lines:
        match = url_pattern.search(line)
        if match:
            return match.group() .strip() 
    return None

def is_image_url(url):
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.svg')
    return url.lower().endswith(image_extensions)

def get_og_img(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        html = response.text
        og_img_pattern = re.compile(r'<meta\s+property="og:image"\s+content="([^"]*)"', re.IGNORECASE)
        match = og_img_pattern.search(html)
        if match:
            return match.group(1)  # Return the content of the og:image tag
        else:
            return None  # Return None if og:image is not found
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def md_to_html(md_file_path, html_file_path):
        pub_date = get_last_modified_date(md_file_path)
        md_lines = get_md_lines(md_file_path)
        img_url =  get_first_url(md_lines)
        author = get_author(md_lines)
        tag_img_og = ""
        tag_img_banner = ""
        tag_author = ""
        if(author is not None):
          tag_author = f" by {author}"
        if (img_url is not None and not is_image_url(img_url) ):
          img_url = get_og_img(img_url)
        if (img_url is not None):
          tag_img_og = f'<meta property="og:image" content="{img_url}" />'
          tag_img_banner = f'<img id="banner" src="{img_url}" alt="article banner image" />'
        title = get_title(md_lines)
        html_body = markdown.markdown(  "\n".join(md_lines))
        html_content = f"""<!DOCTYPE html>
<html  lang="en">
<head>
<meta charset='utf-8'>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta property="og:title" content="{title}" />
<meta property="og:type" content="article" />
{tag_img_og}
<style>
body {{
  
    font-family: Arial, sans-serif;
    line-height: 1.5;
    margin: 0;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}}
p{{
    text-align: justify;
}}
section{{
    margin: 0 1em;

    margin-bottom: 25vh;
max-width: 40em;
}}
code, strong{{
background: #e7e7e7;
padding: 2px .3em;
border-radius: .2em;
}}
img{{
width:100%;
max-width: 40em;
}}
h1{{
margin: 2em 0;
text-align: left;
border-bottom: solid 1px;
padding-bottom: 1em;
}}
#article_metadata{{
font-style: italic;
font-size: .8em;
}}

</style>
</head>
<body>
{tag_img_banner}
<section>
<div id="article_metadata"><date>{pub_date}</date> by Cedric Bonjour  </div>
{html_body}
</section>
</body>
</html>"""
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)




def run_on_dir(dir):
  frm("./out/")
  mk_dir("./out/")
  md_files = get_all_md_file_paths_from(dir)


  for file_path in md_files:
    print(file_path)
    basename = os.path.basename(file_path).split(".")[0]
    md_to_html(file_path, f"./out/{basename}.html" )

run_on_dir("./article")


