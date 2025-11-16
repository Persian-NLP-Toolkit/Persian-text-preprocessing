#   pip install preproc-pkg[formalizer] -c constraints/py38-cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu

from preproc_pkg import create_formal_pipeline

if __name__ == "__main__":
    informal = "اسمم محمده، می‌خوایم بریم بیرون؛ دوستم منتظرم وایستاده."
    pipe = create_formal_pipeline()  # model_name = PardisSzah/PersianTextFormalizer
    print("Informal :", informal)
    print("Formal   :", pipe(informal))
