import os, shutil, sys
from generate_page import generate_pages_recursive
DEBUG = True
def pointless_copy_function(src, dst):
    ls = os.listdir(src)
    for i in ls:
        path = os.path.join(src, i)
        if os.path.isfile(path):
            shutil.copy(path, dst)
            if DEBUG:
                print(f"copying {i} to {dst}")
        if os.path.isdir(path):
            dstpath = os.path.join(dst, i)
            os.mkdir(dstpath)
            if DEBUG:
                print(f"creating dir {dstpath}")
            pointless_copy_function(path, dstpath)

def main():
    if len(sys.argv) >1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    print(f"basepath: {basepath}")

    if DEBUG:
        print(f"Current dir: {os.getcwd()}")

    # delete & recreate public dir
    if os.path.exists("docs/"):
        shutil.rmtree("docs/")
        if DEBUG:
            print("Deleted public dir")

    os.mkdir("docs/")
    if DEBUG:
        print("Creating public dir")

    pointless_copy_function("static/","docs/")
    generate_pages_recursive("content/", "template.html", "docs/",basepath)
    

if __name__ == "__main__":
    main()
