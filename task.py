with open("/home/gofreelab/DAA/sandhi-splitter/data/model") as f:
    with open("/home/gofreelab/anaconda3/lib/python3.7/site-packages/sandhisplitter/models/model.json", "w") as f1:
        for line in f:
            f1.write(line)