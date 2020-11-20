import os

# path for downloaded fashion images
root_fashion_dir = '../deepfashion'
assert len(root_fashion_dir) > 0, 'please give the path of raw deep fashion dataset!'

train_images = []
train_f = open(os.path.join(root_fashion_dir, 'train_new.lst'), 'r')
for lines in train_f:
    lines = lines.strip()
    if lines.endswith('.jpg'):
        train_images.append(lines)

test_images = []
test_f = open(os.path.join(root_fashion_dir, 'test_new.lst'), 'r')
for lines in test_f:
    lines = lines.strip()
    if lines.endswith('.jpg'):
        test_images.append(lines)

train_path = os.path.join(root_fashion_dir, 'train')
if not os.path.exists(train_path):
    os.mkdir(train_path)

# for item in train_images:
#     id = item.index('id', 7)
#     if (item[4:3] == "MEN"):
#         line = train_path + '/' + 'fashion' + 'MEN' + item[8: id - 1]
#     else:
#         line = train_path + '/' + 'fashion' + 'WOMEN' + item[10: id - 1]
#     line = line + 'id' + item[id + 3: id + 11] + item[id + 12: id + 16] + item[id + 17:]
#
#     from_ = os.path.join(root_fashion_dir, item)
#     to_ = os.path.join(line)
#     os.system('cp %s %s' % (from_, to_))

test_path = os.path.join(root_fashion_dir, 'test')
if not os.path.exists(test_path):
    os.mkdir(test_path)

for item in test_images:
    id = item.index('id', 7)
    if (item[4:3] == "MEN"):
        line = test_path + '/' + 'fashion' + 'MEN' + item[8: id - 1]
    else:
        line = test_path + '/' + 'fashion' + 'WOMEN' + item[10: id - 1]
    line = line + 'id' + item[id + 3: id + 11] + item[id + 12: id + 16] + item[id + 17:]

    from_ = os.path.join(root_fashion_dir, item)
    to_ = os.path.join(line)
    os.system('cp %s %s' % (from_, to_))
