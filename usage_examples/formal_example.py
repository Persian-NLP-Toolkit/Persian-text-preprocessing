from preproc_pkg import create_formal_pipeline

if __name__ == "__main__":
    informal = "اسمم محمده، میخوایم بریم بیرون، دوستم منتظرم وایستاده."
    pipe = create_formal_pipeline()
    print("Informal :", informal)
    print("Formal   :", pipe(informal))
