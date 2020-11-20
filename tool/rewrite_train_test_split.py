import os

root_fashion_dir = '../deepfashion'


def rewrite(name, name1):
    split = open(os.path.join(root_fashion_dir, name), 'r')
    lines = []
    for line in split:
        line = line.strip()
        if line.endswith('.jpg'):
            c = line[7:]
            if (c[:3] == "MEN"):
                line = 'img/' + 'MEN/' + c[3:]
            else:
                line = 'img/' + 'WOMEN/' + c[5:]
            id = line.index('id', 7)
            line = line[:id] + '/id_' + line[id + 2:id + 10] + '/' + line[id + 10: id + 14] + '_' + line[id + 14:]
            print(line)
            lines.append(line)

    with open(os.path.join(root_fashion_dir, name1), 'w') as f:
        for item in lines:
            f.write("%s\n" % item)


rewrite('train.lst', 'train_new.lst')
rewrite('test.lst', 'test_new.lst')
