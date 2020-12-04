
def create_model(opt):
    model = None
    print(opt.model)

    if opt.model == 'adgan':
        assert opt.dataset_mode == 'keypoint'
        from .adgan import TransferModel
        model = TransferModel()
    else:
        raise ValueError("Model [%s] not recognized." % opt.model)
    model.initialize(opt)
    print("model [%s] was created" % (model.name()))
    return model
