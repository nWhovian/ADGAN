import time
from options.train_options import TrainOptions
from data.data_loader import CreateDataLoader
from models.models import create_model
from util.visualizer import Visualizer
from tqdm import tqdm
import os
from util import html

opt = TrainOptions().parse()
data_loader = CreateDataLoader(opt)
dataset = data_loader.load_data()
dataset_size = len(data_loader)
print('#training images = %d' % dataset_size)

model = create_model(opt)
visualizer = Visualizer(opt)
total_steps = 0

web_dir = "results/train/images"

webpage = html.HTML(web_dir, 'Experiment = 1')

for epoch in range(opt.epoch_count, opt.niter + opt.niter_decay + 1):
    epoch_start_time = time.time()
    epoch_iter = 0

    with tqdm(enumerate(dataset)) as tepoch:
        for i, data in tepoch:
            tepoch.set_description(f"Epoch {epoch}")

            iter_start_time = time.time()
            visualizer.reset()
            total_steps += opt.batchSize
            epoch_iter += opt.batchSize
            model.set_input(data)
            model.optimize_parameters()

            visuals = model.get_current_visuals()
            img_path = f"epoch_{epoch}_iteration_{i}.jpg"
            img_path = [img_path]
            print(img_path)
            visualizer.save_images(webpage, visuals, img_path)

            errors = model.get_current_errors()
            tepoch.set_postfix({'pair_L1loss': errors['pair_L1loss'].data, 'pair_GANloss': errors['pair_GANloss'].data, 'origin_L1': errors['origin_L1'].data,
                                'perceptual': errors['perceptual'].data, 'CXLoss': errors['CXLoss'].data})

            if total_steps % opt.display_freq == 0:
                save_result = total_steps % opt.update_html_freq == 0
                visualizer.display_current_results(model.get_current_visuals(), epoch, save_result)

            # if total_steps % opt.print_freq == 0:
            #     t = (time.time() - iter_start_time) / opt.batchSize
            #     visualizer.print_current_errors(epoch, epoch_iter, errors, t)
            #     if opt.display_id > 0:
            #         visualizer.plot_current_errors(epoch, float(epoch_iter) / dataset_size, opt, errors)

            if total_steps % opt.save_latest_freq == 0:
                print('saving the latest model (epoch %d, total_steps %d)' %
                      (epoch, total_steps))
                model.save('latest')

    if epoch % opt.save_epoch_freq == 0:
        print('saving the model at the end of epoch %d, iters %d' %
              (epoch, total_steps))
        model.save('latest')
        model.save(epoch)

    print('End of epoch %d / %d \t Time Taken: %d sec' %
          (epoch, opt.niter + opt.niter_decay, time.time() - epoch_start_time))
    model.update_learning_rate()
